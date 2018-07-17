#!/usr/bin/env python

from argparse import ArgumentParser

from src.consts import Mode
from src.radiator_state_controller import RadiatorStateController


def get_args():
    parser = ArgumentParser()

    parser.add_argument("mode", type=Mode)

    parser.add_argument('-d', '--data', type=float, nargs=9, required=False)

    parser.add_argument('-i', '--generate-images', action='store_true')

    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()

    if args.mode is not Mode.HELP:
        rmm = RadiatorStateController(args)
        rmm.run()