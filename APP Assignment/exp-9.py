
# Experiment No. 9
# Convert CSV File to JSON File

import csv
import json
import os

input_file = "students.csv"
output_file = "students.json"

try:
    # Check whether the input file exists
    if not os.path.isfile(input_file):
        print("Error: students.csv file not found.")
    else:
        # Read data from the CSV file
        with open(input_file, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # Remove extra spaces from column names and values
        cleaned_data = []

        for row in data:
            cleaned_row = {
                key.strip(): value.strip() if value else ""
                for key, value in row.items()
                if key is not None
            }
            cleaned_data.append(cleaned_row)

        # Write data to the JSON file
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(cleaned_data, json_file, indent=4)

        print("CSV data successfully converted to JSON.")
        print("Output saved in", output_file)

except (OSError, csv.Error, json.JSONDecodeError) as error:
    print("Error:", error)
