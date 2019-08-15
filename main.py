import os
from PIL import Image, ImageOps
import datetime

location = "images/"  # Folder to parse
valid_ext = [".jpg", "jpeg", ".png"]  # Allowed extensions
total = processed = removed = 0  # Counters
img_size = (1600, 1200)  # Width, height for image crop
thumbnail = (350, 260)  # Width, height for thumbnail
quality = 60  # Quality of saved images
min_width = 500  # Min with for image to process
log_nr = 1000  # Every X files, Log total processed
start_time = datetime.datetime.now()  # Start datetime


def parse_folders(folder):
    global total, processed, removed, min_width, log_nr, quality

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        filename, file_extension = os.path.splitext(path)
        if file_extension in valid_ext:
            image = Image.open(path)
            width, height = image.size

            if width < min_width:
                # If image width is less than min_width, remove!
                os.remove(path)
                removed += 1
            else:
                # Check if is landscape
                if width > height:
                    # Check if image width is bigger than our width
                    if width >= img_size[0]:
                        # Crop Image
                        original = ImageOps.fit(image, img_size, method=Image.ANTIALIAS, bleed=0.0, centering=(0.5, 0.5))
                        # Optimize image, set quality to 60% and save
                        original.save(filename + file_extension, optimize=True, quality=quality)
                    else:
                        # Just optimize, set quality to 60% and save
                        image.save(filename + file_extension, optimize=True, quality=quality)
                # If image is in portrait mode
                elif height > width:
                    if height >= img_size[1]:
                        original = ImageOps.fit(image, tuple(reversed(img_size)), method=Image.ANTIALIAS, bleed=0.0, centering=(0.5, 0.5))
                        original.save(filename + file_extension, optimize=True, quality=quality)
                    else:
                        image.save(filename + file_extension, optimize=True, quality=quality)
                # If image is square
                else:
                    image.save(filename + file_extension, optimize=True, quality=quality)
                # Count processed images
                processed += 1

                # Create thumbnail
                thumb = ImageOps.fit(image, thumbnail, method=Image.ANTIALIAS, bleed=0.0, centering=(0.5, 0.5))
                thumb.save(filename + "-thumbnail" + file_extension, optimize=True, quality=quality)

            # Count total images
            total += 1
            if total % log_nr == 0:
                print(str(datetime.datetime.now()) + ": ===== Processed " + str(total) + " images ...")
        if os.path.isdir(path):
            # If is folder instead of file, parse this folder
            parse_folders(path)


print(str(datetime.datetime.now()) + ": Parsing folder \"" + location + "\"...")
parse_folders(location)
print(str(datetime.datetime.now()) + ": Done...")
print("Total parsed: " + str(total) + " images.")
print("Processed: " + str(processed) + " images.")
print("Removed: " + str(removed) + " images")
elapsed_seconds = (datetime.datetime.now() - start_time).total_seconds()
print("Elapsed time: " +
      str("%.3f" % elapsed_seconds) + " seconds. Aprox. " +
      str(int(elapsed_seconds / 60)) + " minutes.")
print("Bye bye...")
