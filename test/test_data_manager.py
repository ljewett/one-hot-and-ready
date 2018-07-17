import pytest

from src.config_manager import ConfigManager
from src.data_manager import DataManager
from src.exceptions import UnknownStateException


def test_clean_state_throws_error_on_unknown_value():
    with pytest.raises(UnknownStateException):
        DataManager.clean_state(b'UnknownState')


def test_clean_state_handles_default():
    """
    1 Rad Flow
    2 Fpv Close
    3 Fpv Open
    4 High
    5 Bypass
    6 Bpv Close
    7 Bpv Open
    """
    assert DataManager.clean_state(b'Rad Flow') == 1
    assert DataManager.clean_state(b'Radiator Flow') == 1
    assert DataManager.clean_state(b'Fpv Close') == 2
    assert DataManager.clean_state(b'Fpv Open') == 3
    assert DataManager.clean_state(b'High') == 4
    assert DataManager.clean_state(b'Bypass') == 5
    assert DataManager.clean_state(b'Bpv Close') == 6
    assert DataManager.clean_state(b'Bpv Open') == 7


def test_get_data_able_to_load_training_data():
    data_manager = DataManager(ConfigManager.load_config())
    data = data_manager.get_test_data()

    assert data.shape[1] == 10


def test_split_data():
    data_manager = DataManager(ConfigManager.load_config())
    data = data_manager.get_test_data()

    x_train, x_test, y_train, y_test = data_manager.split_data(data)
    assert x_train.shape[0] == y_train.shape[0]
    assert x_test.shape[0] == y_test.shape[0]


def test_get_data_able_to_load_testing_data():
    data_manager = DataManager(ConfigManager.load_config())
    data = data_manager.get_validation_data()

    assert data.shape[1] == 10