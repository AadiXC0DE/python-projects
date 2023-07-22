import json
import csv

def json_to_csv(input_file, output_file):
    # Read JSON data 
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    # Extract the header fields from the JSON data
    header = data[0].keys()

    # Write CSV data to the output file
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)

        # Write the header row
        writer.writeheader()

        
        for item in data:
            writer.writerow(item)

if __name__ == "__main__":
    input_file_path = "data.json"
    output_file_path = "output.csv"
    json_to_csv(input_file_path, output_file_path)
    print(f"Conversion successful. Output saved to '{output_file_path}'")
