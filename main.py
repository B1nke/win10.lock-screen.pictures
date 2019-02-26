import os
import shutil
import sys

try:
  from PIL import Image
except ImportError:
  print("""Pillow is not installed, install it with 
> pip install pillow
https://pillow.readthedocs.io/en/latest/installation.html#basic-installation for more information""")
  sys.exit()

folder = "tmp"
if len(sys.argv) > 1:
  folder = sys.argv[1]

source_folder = os.path.join(os.getenv('LOCALAPPDATA'), 'Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets')
destination_folder = os.path.join('C:\\', os.getenv('HOMEPATH'), 'Pictures', folder)
min_file_size = 100*1000

if not os.path.exists(destination_folder):
  os.mkdir(destination_folder)

print("Checking for new images in", source_folder)
copied_files = 0

for filename in os.listdir(source_folder):
  original_file = os.path.join(source_folder, filename)
  fileSize = os.path.getsize(original_file)
  
  if fileSize > min_file_size:
    new_file = os.path.join(destination_folder, filename + '.png')

    if not os.path.isfile(new_file):
      width, height = Image.open(original_file).size
      
      if width > height:
        print("Copying file: ", filename)
        shutil.copy(original_file, new_file)
        copied_files += 1

print(copied_files,"files have been copied to", destination_folder)