from src.utils import read_json, create_objects_from_json
import pytest
import os
from config import ROOT_DIR

path = os.path.join(ROOT_DIR, 'data', 'data.json')


def test_read_json_not_found():
    path_none = os.path.join(ROOT_DIR, 'data', 'none.json')
    with pytest.raises(FileNotFoundError):
        read_json(path_none)


def test_read_json():
    count_name = []
    for i in read_json(path):
        count_name.append(i['username'])
    assert len(read_json(path)) == len(count_name)


def test_read_json_second():
    assert len(read_json(path)) == 4


def test_create_objects_from_json():
    assert create_objects_from_json(read_json('data/data.json'))[0].username == 'Ivan'
    assert create_objects_from_json(read_json('data/data.json'))[3].username == 'Поп'
    assert len(create_objects_from_json(read_json('data/data.json'))[0].task_list) == 2
