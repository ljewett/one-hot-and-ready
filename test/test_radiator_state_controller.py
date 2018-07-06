from subprocess import call

import pytest
from exceptions import UnknownStateException
from radiator_manager import RadiatorController

from src.config_manager import ConfigManager

default_args = {}


def test_get_data_able_to_load_training_data():
    rmm = RadiatorController(default_args)
    data = rmm.get_test_data()
    assert data.shape[1] == 10


def test_run_help_gets_help_message():
    exit_code = call(['./main.py help'], shell=True)
    assert exit_code is 0