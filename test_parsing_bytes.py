import pytest
from main import get_parsed_data

def test_parsed_data():
    get_parsed = {'field1': 'Medium', 'field2': '00', 'field3': '01', 'field4': '70', 'field5': '00', 'field6': '01', 'field7': '00', 'field8': 'Medium', 'field9': '00', 'field10': '00'}
    assert get_parsed_data() == get_parsed, 'функция должна вернуть структуру'

