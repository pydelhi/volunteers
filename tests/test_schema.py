import json
from os.path import dirname, join


def test_validate_json_files():
    files = ['teams.json', 'volunteers.json']
    for filename in files:
        data_file = join(dirname(dirname(__file__)), filename)

        # read and try to load them as json
        raw_data = open(data_file).read()
        json.loads(raw_data)
