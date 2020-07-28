"""
basefunctions.py - Core functions for this project.

Author: Wilson França de Souza
Email: wilson.franca.92@gmail.com
Date: 7/28/2020

"""

import sys
import os
import csv
import glob


def writeToCSV(output_fileName: str, output_path: str, dataList: list):
    file_location = os.path.join(output_path, output_fileName)
    with open(file_location, "w", newline="") as csvFile:
        writer = csv.writer(csvFile)
        for row in dataList:
            writer.writerow(row)
    return file_location


def extractCategoryfromCSVName(filename: str, separator1: str, separator2: str):
    # Example filename = "StormEvents_locations-ftp_v1.0_d2005_c20200518"
    ## [1] = locations-ftp | [0] = locations
    category = filename.split(separator1)[1].split(separator2)[0]
    return category


def makedirIfNotExists(path_to_folder: str):
    if os.path.exists(path_to_folder):
        pass
    else:
        os.mkdir(path_to_folder)


def summarizeCsvDataForHarrisCounty(
    csvFolder_Category: str,
    output_fileName: str,
    output_path: str,
    county_fips="201",
    state_fips="48",
):
    list_of_rows_harris_county = []
    event_id_harris_county = []
    for src_name in glob.glob(os.path.join(csvFolder_Category, "*.csv")):
        absolute_path = os.path.abspath(src_name)
        with open(absolute_path, "r") as fileIn:
            csv_reader = csv.reader(fileIn)
            header = next(csv_reader)
            if header not in list_of_rows_harris_county:
                list_of_rows_harris_county.append(header)
            for row in csv_reader:
                if row[9] == state_fips and row[14] == county_fips:
                    list_of_rows_harris_county.append(row)
                    if row[7] not in event_id_harris_county:
                        event_id_harris_county.append(row[7])
    file_location = writeToCSV(
        output_fileName, output_path, dataList=list_of_rows_harris_county,
    )
    return file_location, event_id_harris_county


def sumFilterByEventID(
    csvFolder_Category: str,
    output_fileName: str,
    output_path: str,
    event_id_harris_county_list: list,
    event_id_column_number: int,
):
    list_of_rows_harris_county = []
    for src_name in glob.glob(os.path.join(csvFolder_Category, "*.csv")):
        absolute_path = os.path.abspath(src_name)
        with open(absolute_path, "r") as fileIn:
            csv_reader = csv.reader(fileIn)
            header = next(csv_reader)
            if header not in list_of_rows_harris_county:
                list_of_rows_harris_county.append(header)
            for row in csv_reader:
                if row[event_id_column_number] in event_id_harris_county_list:
                    list_of_rows_harris_county.append(row)
    file_location = writeToCSV(
        output_fileName, output_path, dataList=list_of_rows_harris_county,
    )
    return file_location
