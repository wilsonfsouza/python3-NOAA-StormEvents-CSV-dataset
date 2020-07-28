"""
table-join.py - Using Pandas Library to join the fatalaties, locations, and details tables
into a final csv file (EVENT_ID = Primary database key field).

Author: Wilson França de Souza
Email: wilson.franca.92@gmail.com
Date: 7/28/2020

"""

import os.path
import numpy as np
import pandas as pd
from basefunctions import makedirIfNotExists

# Dir Paths
source_dir = r"D:\Documents\Rice University\Work\Highways + Watersheds\StormEvents"
inProcess_dir = os.path.join(source_dir, "StormEvents CSV", "N01_InProcess")
final_dir = os.path.join(source_dir, "StormEvents CSV", "N02_Final")
makedirIfNotExists(final_dir)

# File Paths
fatalities_summary_csvPath = os.path.join(
    inProcess_dir, "StormEvents_fatalities_summary" + ".csv"
)
locations_summary_csvPath = os.path.join(
    inProcess_dir, "StormEvents_locations_summary" + ".csv"
)
details_summary_csvPath = os.path.join(
    inProcess_dir, "StormEvents_details_summary" + ".csv"
)
# Output Path
output_path = os.path.join(final_dir, "StormEvents_Harris_County.csv")

# Read CSV with Pandas
fatalities = pd.read_csv(fatalities_summary_csvPath)
locations = pd.read_csv(locations_summary_csvPath)
details = pd.read_csv(details_summary_csvPath)

# Set EVENT_ID as Index
fatalities.set_index("EVENT_ID", inplace=True)
locations.set_index("EVENT_ID", inplace=True)
details.set_index("EVENT_ID", inplace=True)

# Table join
details_locations_merge = pd.merge(details, locations, how="left", on="EVENT_ID")
table_join_all = pd.merge(
    details_locations_merge, fatalities, how="left", on="EVENT_ID"
)

# Export Dataframe as CSV
table_join_all.to_csv(output_path)
