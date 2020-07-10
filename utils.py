import json
import pandas as pd
import xlrd


def read_config(env, file):
    with open('config.json') as config_file:
        content = json.load(config_file)
    return content[env.upper()][file.upper()]


def read_source_file():
    pass


def read_mapping_document():
    pass


if __name__ == '__main__':
    # print(read_config('DEV', 'IRIS'))
    pass
