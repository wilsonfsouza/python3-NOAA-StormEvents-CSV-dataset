# Introduction
This project aimed to extract and summarize information from [NOAA Historical Storm Events Dataset](ftp://ftp.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/) into a final CSV file for Harris County, Texas.

# Table of Contents
- [Technologies used](#technologies-used)
- [Workspace Setup](#workspace-setup)
- [Python Scripts](#python-scripts)
    - [Description](#description)
    - [Order](#order)
    - [Folder Structure](#folder-structure)

# Technologies used:

- python 3.7.3
### Code Editor:
- VS Code.
### Libraries:
- csv
- glob
- gzip
- numpy 1.19.1
- pandas 1.0.5
- sys
- os

# Workspace Setup
### 1. Install virtualenv globally using this [tutorial](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/).

### 2. Create a Virtual Environment and activate it
In the desired folder, create and activate your virtual environment.
```bash
# Virtualenv modules installation (Windows based systems)
$ virtualenv --no-site-packages env

# Activate Virtualenv
$ .\env\Scripts\activate

# Virtualenv modules installation (Unix based systems - Linux/Mac)
$ virtualenv --no-site-packages env
### OR
$ virtualenv --python=/usr/bin/python3 --no-site-packages env

# Activate Virtualenv
$ source env/bin/activate
```

### 3. Install modules
```bash
# Install modules
$ pip3 install -r requirements.txt
```

# Python Scripts

### Description:
- `basefunctions.py` = Script contains all core functions for this task.

- `extract-gz-to-csv.py` = Extract all csv files from .gzip into the related category folder.

- `summarize-data-for-harris-county.py` = Filter Dataset for Harris County, Texas. Summarize it into a csv for each category.

- `table-join.py` = Using Pandas Library to join the fatalaties, locations, and details tables into a final csv file (**EVENT_ID** = Primary database key field).

### Order:
Run scripts in this order:

1.`extract-gz-to-csv.py` >
2.`summarize-data-for-harris-county.py` >
3.`table-join.py`

### Folder Structure:

You will need to pass the source directory, which is where your scripts and dataset are located. Then, the following structure will be created.

- Source Dir
    - Scripts
    - .gzip files
    - StormEvents CSV (*new*)
        - N00_Original (*new*)
        - N01_InProcess (*new*)
            - details (*new*)
            - locations (*new*)
            - fatalities (*new*)
        - N02_Final (*new*)

Made with :heart: by [Wilson Franca](https://www.linkedin.com/in/wilsonfranca-env-engineer/) :wave: