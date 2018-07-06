from enum import Enum

from src.labeled_set import LabeledSet


class Mode(Enum):
    TRAIN = 'train'
    VALIDATE = 'validate'
    PREDICT = 'predict'
    HELP = 'help'


class StateMapper(dict):
    def __init__(self):
        super().__init__({
            1: LabeledSet('Rad Flow', {b'Rad Flow', b'Radiator Flow'}),
            2: LabeledSet('Fpv Close', {b'Fpv Close', b'Flow Proportioning Valve Close'}),
            3: LabeledSet('Fpv Open', {b'Fpv Open', b'Flow Proportioning Valve Open'}),
            4: LabeledSet('High', {b'High'}),
            5: LabeledSet('Bypass', {b'Bypass'}),
            6: LabeledSet('Bpv Close', {b'Bpv Close', b'Bipropellant Valve Close'}),
            7: LabeledSet('Bpv Open', {b'Bpv Open', b'Bipropellant Valve Open'})
        })
