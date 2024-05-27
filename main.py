import argparse

def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input_file")
    arg_parser.add_argument("output_file")
    return arg_parser.parse_args()

