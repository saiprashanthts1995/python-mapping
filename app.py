import argparse
from utils import read_config


def main(environment, name_of_file):

    config_details = read_config(environment, name_of_file)
    print(config_details)





if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Welcome to Coding",
                                     prog="app.py"
                                     )
    parser.add_argument('-e',
                        '--env',
                        dest="env",
                        required=True,
                        choices=['DEV', 'QA'],
                        help="Mention the environment"
                        )
    parser.add_argument('-f',
                        '--filename',
                        dest="filename",
                        required=True,
                        help="Mention the file name"
                        )

    args = parser.parse_args()
    env = args.env
    filename = args.filename
    print(args)
    main(env, filename)
