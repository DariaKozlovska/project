import argparse
import json
import os
import yaml

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
    except Exception as e:
        print("Error: ", e)

def yaml_file(file_path):
    if not os.path.exists(file_path):
        print("File not found: ", file_path)
        return None

    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except yaml.YAMLError as e:
        print("Error decoding YAML: ", e)
    except Exception as e:
        print("Error: ", e)
    
    return None

def main():
    args = get_args()
    input_file = args.input_file
    output_file = args.output_file

    if input_file.lower().endswith('.json'):
        load_function = json_file
    elif input_file.lower().endswith('.yaml') or input_file.lower().endswith('.yml'):
        load_function = yaml_file
    else:
        print("Unsupported file format. Currently, only .json, .yaml/.yml, and .xml files are supported for reading.")
        return

    data = load_function(input_file)
    if data is None:
        print("Failed to load data.")
        return


    if output_file.lower().endswith('.json'):
        save_json(data, output_file)
    else:
        print("Unsupported file format. Currently, only .yaml/.yml, .json, and .xml files are supported for writing.")
        return

    print("Data successfully saved to ", output_file)

if __name__ == "__main__":
    main()