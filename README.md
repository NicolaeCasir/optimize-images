# Image Optimizer
I had to process (optimize, resize, crete thumbnails and delete) more than 150k images.

The easiest way was to create this python script.

## Usage
1. Install [PIL](https://pillow.readthedocs.io/en/stable/installation.html)
    ```
    pip install Pillow
    ```
    or
    ```
    python3 -m pip install Pillow
    ```
2. Edit file `main.py`:
    ```python
    location = "images/"  # Folder to parse
    valid_ext = [".jpg", "jpeg", ".gif", ".png"]  #  Allowed extensions
    total = processed = removed = 0  # Counters
    img_size = (1600, 1200)  # Width, height for image crop
    thumbnail = (350, 260)  # Width, height for thumbnail
    quality = 60  # Quality of saved images
    min_width = 500  # Min with for image to process
    log_nr = 5  # Every X files, Log total processed
    ```
3. Run script:
```
python main.py
```
or
``` 
python3 main.py
```
