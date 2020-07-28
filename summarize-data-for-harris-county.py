"""
summarize-data-for-harris-county.py - Filter Dataset for Harris County, Texas. Summarize it
into a csv for each category.

Author: Wilson França de Souza
Email: wilson.franca.92@gmail.com
Date: 7/28/2020

"""

import os.path

from basefunctions import (
    writeToCSV,
    makedirIfNotExists,
    summarizeCsvDataForHarrisCounty,
    sumFilterByEventID,
)

# Dir Paths
source_dir = r"D:\Documents\Rice University\Work\Highways + Watersheds\StormEvents"
original_dir = os.path.join(source_dir, "StormEvents CSV", "N00_Original")
inprocess_dir = os.path.join(source_dir, "StormEvents CSV", "N01_InProcess")
makedirIfNotExists(original_dir)
makedirIfNotExists(inprocess_dir)

## Details
csvFolderDetails = os.path.join(original_dir, "details")
csvFileNameDetails = "StormEvents_details_summary.csv"

file_location_details, event_id_harris_county = summarizeCsvDataForHarrisCounty(
    csvFolder_Category=csvFolderDetails,
    output_fileName=csvFileNameDetails,
    output_path=inprocess_dir,
    county_fips="201",
    state_fips="48",
)

## Locations
csvFolderLocations = os.path.join(original_dir, "locations")
csvFileNameLocations = "StormEvents_locations_summary.csv"

sumFilterByEventID(
    csvFolder_Category=csvFolderLocations,
    output_fileName=csvFileNameLocations,
    output_path=inprocess_dir,
    event_id_harris_county_list=event_id_harris_county,
    event_id_column_number=2,
)

## Fatalities
csvFolderFatalities = os.path.join(original_dir, "fatalities")
csvFileNameFatalities = "StormEvents_fatalities_summary.csv"

sumFilterByEventID(
    csvFolder_Category=csvFolderFatalities,
    output_fileName=csvFileNameFatalities,
    output_path=inprocess_dir,
    event_id_harris_county_list=event_id_harris_county,
    event_id_column_number=4,
)
