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
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        print("Error decoding JSON: ", e)
    except Exception as e:
        print("An error occurred: ", e)

    return None

def save_json(data, file_path):
    try:
        if not os.path.exists(file_path):
            directory = os.path.dirname(file_path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            else:
                file_path = os.path.join(os.getcwd(), file_path)
                directory = os.path.dirname(file_path)
                os.makedirs(directory, exist_ok=True)
            with open(file_path, 'w') as file:
                file.write('{}\n')
            print("Created new JSON file: ", file_path)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print("Error: ", e)
