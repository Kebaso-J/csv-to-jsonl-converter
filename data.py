import csv
import json

def convert_csv_to_jsonl(csv_file, jsonl_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        with open(jsonl_file, 'w') as jsonl:
            for row in csv_reader:
                jsonl.write(json.dumps(row) + '\n')


csv_file = r'path_to_csv_file'
jsonl_file = r'path_to_where_jsonl_will_be_stored'
convert_csv_to_jsonl(csv_file, jsonl_file)