import json
import pandas as pd
import datetime
import os


def format_printer(message):
    print('='*50)
    print(f'{message}')
    print('=' * 50)


def udf_time(method1):
    def udf(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = method1(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f'Total time taken to the overall module is {end_time-start_time}')
        return result
    return udf


def udf_exception(method1):
    def udf(*args, **kwargs):
        try:
            flag = True
            result = method1(*args, **kwargs)
            flag = False
            return result
        except KeyError as e:
            print(f'Key {e} error is not present in {udf_exception.__name__} {os.name}')
        except Exception as e:
            print(e)
            print('hello')
        finally:
            if flag:
                print('Exiting the Module . Because of above issue')
                exit(1)
    return udf


def read_config(env, file):
    with open('config.json') as config_file:
        content = json.load(config_file)
    print('Config File Read Successfully')
    return content[env.upper()][file.upper()]


def read_source_file(env, file):
    config_contents = read_config(env, file)
    data = pd.read_csv(config_contents['SRC_FILE_NAME'],
                       sep=config_contents['FILE_DELIMITER'])
    print('Source File read successfully')
    return data


def read_mapping_document(env, file):
    config_contents = read_config(env, file)
    mapping_content = pd.read_excel(config_contents['MAPPING_FILE_NAME'],
                                    sheet_name="Mapping",
                                    usecols=config_contents['MAPPING_RANGE_COLUMNS'],
                                    skiprows=config_contents['MAPPING_SKIP_ROWS'],
                                    )
    print('Mapping Document read successfully')
    return mapping_content


def write_into_file(data, format_of_file, filename):
    if format_of_file.lower() == 'csv':
        data.to_csv(filename, index=False)
    elif format_of_file.lower() == 'excel':
        data.to_excel(filename, sheet_name='Data', index=False)
    elif format_of_file.lower() == 'text':
        data.to_csv(filename, index=False)
    elif format_of_file.lower() == 'parquet':
        data.to_parquet(filename, index=False)
    else:
        return False
    print(f'Writing of file {filename} completed. It is written as {format_of_file} file')
    return True



if __name__ == '__main__':
    # print(read_config('DEV', 'IRIS1'))
    # print(read_mapping_document('DEV', 'IRIS1'))
    print(read_source_file('DEV', 'IRIS'))

