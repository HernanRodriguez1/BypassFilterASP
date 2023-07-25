import argparse
import urllib.parse
from colorama import Fore, Style

print (Fore.RED + """\n

  ____                              _____ _ _ _            _        _    ____  ____  
 | __ ) _   _ _ __   __ _ ___ ___  |  ___(_) | |_ ___ _ __| |_     / \  / ___||  _ \ 
 |  _ \| | | | '_ \ / _` / __/ __| | |_  | | | __/ _ \ '__| __|   / _ \ \___ \| |_) |
 | |_) | |_| | |_) | (_| \__ \__ \ |  _| | | | ||  __/ |  | |_   / ___ \ ___) |  __/ 
 |____/ \__, | .__/ \__,_|___/___/ |_|   |_|_|\__\___|_|   \__| /_/   \_\____/|_|    
        |___/|_|                                                                     

Create By: Hernan Rodriguez | Team Offsec Peru \n""" + Style.RESET_ALL)


def encode_payload(payload):
    replacements = {"%3C": "%EF%BC%9C", "%3E": "%EF%BC%9E"}
    encoded_string = urllib.parse.quote(payload)

    for key, val in replacements.items():
        encoded_string = encoded_string.replace(key, val)

    return encoded_string

def perform_queries(input_file, output_file):
    with open(input_file, 'r') as file:
        with open(output_file, 'w') as out_file:
            for line in file:
                payload = line.strip()
                encoded_payload = encode_payload(payload)
                print(encoded_payload)
                out_file.write(encoded_payload + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="XSS Payload Encoder")
    parser.add_argument("-i", "--input_file", required=True, help="Input file with multiple payloads")
    parser.add_argument("-o", "--output_file", required=True, help="Output file to save the encoded payloads")
    args = parser.parse_args()

    perform_queries(args.input_file, args.output_file)
