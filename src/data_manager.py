import numpy as np
from sklearn.model_selection import train_test_split

from src.consts import StateMapper
from src.exceptions import UnknownStateException


class DataManager:
    def __init__(self, config):
        self.config = config

    @staticmethod
    def clean_state(input):
        for k, v in StateMapper().items():
            if input in v:
                return k

        raise UnknownStateException('Unknown State: {}'.format(input))

    def get_test_data(self):
        delimiter = self.config.get('context', 'delimiter')
        data_location = self.config.get('context', 'train_location')
        return np.loadtxt(data_location, delimiter=delimiter, converters={
            9: lambda x: self.clean_state(x)
        })

    def get_validation_data(self):
        delimiter = self.config.get('context', 'delimiter')
        data_location = self.config.get('context', 'test_location')
        return np.loadtxt(data_location, delimiter=delimiter, converters={
            9: lambda x: self.clean_state(x)
        })

    def split_data(self, data):
        y_column = self.config.getint('context', 'y_column')
        x = data[:, 0:y_column]
        y = data[:, y_column]

        test_size = self.config.getfloat('hyperparameters', 'test_size')
        random_state = self.config.getint('hyperparameters', 'random_state')

        # x_train, x_test, y_train, y_test
        return train_test_split(x, y, test_size=test_size, random_state=random_state)