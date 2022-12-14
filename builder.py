from typing import Optional, List, Iterable

from functions import filter_query, map_query, unique_query, sort_query, limit_query, filter_regex

FILE_NAME = 'data/apache_logs.txt'
CMD_TO_FUNCTION = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
    'regex': filter_regex,
}

def iter_file(file_name: str) -> Iterable:
    with open(file_name) as file:
        for row in file:
            yield row

def query_builder(cmd, value, data=None) -> List:
    if data is None:
        prepared_data = iter_file(FILE_NAME)
    else:
        prepared_data = data
    result = CMD_TO_FUNCTION[cmd](param=value, data=prepared_data)
    return list(result)
