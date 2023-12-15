import argparse
import json

def json_to_lang(json_file_path, lang_file_path):
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    lang_data = ""
    
    for key, value in json_data.items():
        lang_data += f"{key}={value}\n"

    with open(lang_file_path, 'w') as lang_file:
        lang_file.write(lang_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON to .lang format")
    parser.add_argument("input", help="Path to the input JSON file")
    parser.add_argument("output", help="Path to the output .lang file")

    args = parser.parse_args()

    # Convert JSON to .lang
    json_to_lang(args.input, args.output)
