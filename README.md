# win10.lock-screen.pictures
I usually like the lock screen pictures and like to have them as wallpapers, so I made this small script to copy them to `Pictures/tmp`. Running the script once or twice a week will usually grab all the pictures that have been used for the lock screen.

## Usage
Just run the script from console

`> python main.py`

To save files to a different folder than `tmp`, just add the folder name at the end

`> python main.py otherFolder`

## Requirements
Package requires [Python](https://www.python.org/downloads/) with [Pillow](https://pillow.readthedocs.io/en/latest/installation.html#basic-installation) installed. If you don't care, just run `> pip install pillow` after you have installed Python