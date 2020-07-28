"""
extract-gz-to-csvs.py - Extract all csv files from .gzip into the related category folder.

Author: Wilson França de Souza
Email: wilson.franca.92@gmail.com
Date: 7/28/2020

"""

# Import modules
import gzip
import glob
import os.path
from basefunctions import extractCategoryfromCSVName, makedirIfNotExists

# Directory Paths
source_dir = r"D:\Documents\Rice University\Work\Highways + Watersheds\StormEvents"
stormEventsCsv_dir = os.path.join(source_dir, "StormEvents CSV")
makedirIfNotExists(stormEventsCsv_dir)
dest_dir = os.path.join(stormEventsCsv_dir, "N00_Original")
makedirIfNotExists(dest_dir)


# Search for files with *.gz extension in a folder
for src_name in glob.glob(os.path.join(source_dir, "*.gz")):
    base = os.path.basename(src_name)
    category = extractCategoryfromCSVName(base, "_", "-")
    category_folder_path = os.path.join(dest_dir, category)
    makedirIfNotExists(category_folder_path)
    dest_name = os.path.join(category_folder_path, base[:-3])
    # Extract and export the csv
    with gzip.open(src_name, "rb") as infile:
        with open(dest_name, "wb") as outfile:
            for line in infile:
                outfile.write(line)
