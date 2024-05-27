import argparse
import json
import os

def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input_file")
    arg_parser.add_argument("output_file")
    return arg_parser.parse_args()

def json_file(file_path):
    if not os.path.exists(file_path):
        print("File not found: ", file_path)
        return None

    try: 
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print("Error decoding JSON: ", e)
    except Exception as e:
        print("An error occurred: ", e)

    return None



