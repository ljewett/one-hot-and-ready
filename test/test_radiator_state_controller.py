from subprocess import call

from src.radiator_state_controller import RadiatorStateController


def test_run_help_gets_returns_exit_zero():
    exit_code = call(['./main.py help'], shell=True)
    assert exit_code is 0


def test_radiator_state_controller():
    args = {}
    RadiatorStateController(args)
