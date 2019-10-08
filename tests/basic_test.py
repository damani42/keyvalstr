import pytest

from keyvalstr.keyvalstr import KeyValStr


@pytest.fixture
def keyvalstr_object():
    return KeyValStr(
        'key1:val1,key2:val2,key3,key4:val4,default:default_value')


def test_get_value(keyvalstr_object):
    assert keyvalstr_object.get_value('key1') == 'val1'


def test_no_key(keyvalstr_object):
    assert keyvalstr_object.get_value('foo') is None


def test_no_key_part_str(keyvalstr_object):
    assert keyvalstr_object.get_value('ke') is None


def test_get_no_value_with_default_key(keyvalstr_object):
    assert keyvalstr_object.get_value('key3') == 'default_value'


def test_get_no_key(keyvalstr_object):
    assert keyvalstr_object.get_value('key5') is None


def test_empty_string():
    with pytest.raises(ValueError):
        KeyValStr('')


def test_no_string():
    with pytest.raises(ValueError):
        KeyValStr({'key': 'value'})


def test_strip():
    obj = KeyValStr('key1:val1, key2: val2,key3,key4:val4')
    assert obj.get_value('key2') == 'val2'


def test_get_no_value_with_default_key_from_obj():
    obj = KeyValStr(
        'key1:val1,key2:val2,key3,key4:val4',
        default_value='Default value from obj')

    assert obj.get_value('key3') == 'Default value from obj'


def test_get_no_value_no_default():
    obj = KeyValStr('key1:val1,key2:val2,key3,key4:val4')

    assert obj.get_value('key3') is None
