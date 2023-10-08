import zipfile
import shutil

# Unzip
# if needed, set password with pwd
with zipfile.ZipFile('./files_1.zip', 'r') as zip_ref:
    zip_ref.extractall('./unziped', pwd=None)

# Zip
# Destination, Format, Folder
shutil.make_archive('./files_2', 'zip', './to_zip')