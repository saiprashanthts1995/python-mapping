import argparse
from utils import read_source_file, read_mapping_document, udf_exception, udf_time


@udf_exception
@udf_time
def main(environment, name_of_file):
    data = read_source_file(environment, name_of_file)
    print(data)





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
