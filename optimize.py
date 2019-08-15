import os
from PIL import Image, ImageOps
import datetime

location = "for_optimization/"  # Folder to parse
valid_ext = [".jpg", "jpeg", ".png"]  # Allowed extensions
processed = 0  # Counters
quality = 60  # Quality of saved images
log_nr = 5  # Every X files, Log total processed
start_time = datetime.datetime.now()  # Start datetime


def parse_folders(folder):
    global processed, log_nr, quality

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        filename, file_extension = os.path.splitext(path)
        if file_extension in valid_ext:
            try:
                image = Image.open(path)
                image.save(filename + file_extension, optimize=True, quality=quality)
            except Exception as e:
                print("\n******* EXCEPTION *******")
                print("*")
                print("* " + str(e))
                print("*")
                print("******* EXCEPTION *******\n")

            processed += 1
            if processed % log_nr == 0:
                print(str(datetime.datetime.now()) + ": ===== Processed " + str(processed) + " images ...")
        if os.path.isdir(path):
            # If is folder instead of file, parse this folder
            parse_folders(path)


print(str(datetime.datetime.now()) + ": Parsing folder \"" + location + "\"...")
parse_folders(location)
print(str(datetime.datetime.now()) + ": Done...")
print("Total processed: " + str(processed) + " images.")
elapsed_seconds = (datetime.datetime.now() - start_time).total_seconds()
print("Elapsed time: " +
      str("%.3f" % elapsed_seconds) + " seconds. Aprox. " +
      str(int(elapsed_seconds / 60)) + " minutes.")
print("Bye bye...")
