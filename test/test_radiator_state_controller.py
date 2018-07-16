from subprocess import call

from src.radiator_state_controller import RadiatorStateController

default_args = {}


def test_run_help_gets_help_message():
    exit_code = call(['./main.py help'], shell=True)
    assert exit_code is 0