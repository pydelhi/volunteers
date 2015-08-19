#!/usr/bin/python
import json
import sys
from os.path import dirname, join


def main(argv):
    if len(argv) < 1:
        print ("Takes a json filename as input name, and overites that file with "
               "formated json. \n"
               "Usage: python sort.py <file_name1> [filename2] ... [filenameN]")
    for filename in argv:
        data_file = join(dirname(__file__), filename)

        with open(data_file, 'r+') as file:
            raw_data = file.read()
            parsed_data = json.loads(raw_data)
            parsed_data.sort()
            output = json.dumps(parsed_data, indent=4, sort_keys=True)
            file.seek(0)
            file.write(output)

if __name__ == "__main__":
    main(sys.argv[1:])
