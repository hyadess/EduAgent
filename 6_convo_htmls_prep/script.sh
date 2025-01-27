#!/bin/bash

# Specify your CSV file path here
CSV_FILE="sets.csv"

# Check if the CSV file exists
if [ ! -f "$CSV_FILE" ]; then
    echo "CSV file $CSV_FILE not found!"
    exit 1
fi

# Read the CSV file, skipping the first line (header)
tail -n +2 "$CSV_FILE" | while IFS=',' read -r set_number num1 num2 num3 num4
do
    # Call the evaluator.py script with the set number and the extracted numbers as arguments
    python3 evaluator.py "$set_number" "$num1" "$num2" "$num3" "$num4"
done
