import numpy as np
import xgboost as xgb

from src.config_manager import ConfigManager
from src.consts import Mode, StateMapper
from src.data_manager import DataManager
from src.imager import Imager
from src.model_manager import ModelManager


class RadiatorStateController:
    def __init__(self, args):
        self.args = args
        self.config = ConfigManager.load_config()

        self.data_manager = DataManager(self.config)
        self.model_manager = ModelManager(self.config)

    def run(self):
        mode = self.args.mode
        model = None if mode == Mode.TRAIN else self.model_manager.load_model()
        {
            Mode.TRAIN: self.train_model,
            Mode.VALIDATE: self.validate_model,
            Mode.PREDICT: self.predict_state,
        }.get(mode)(model)

    def train_model(self, _):
        params = ConfigManager.get_xgbparameters()
        data = self.data_manager.get_test_data()

        x_train, x_test, y_train, y_test = self.data_manager.split_data(data)
        xg_train = xgb.DMatrix(x_train, label=y_train)
        xg_test = xgb.DMatrix(x_test, label=y_test)

        watchlist = [(xg_train, 'train'), (xg_test, 'test')]

        num_rounds = self.config.getint('hyperparameters', 'num_rounds')

        model = xgb.train(params, xg_train, num_rounds, watchlist)

        self.model_manager.save_model(model)

        self.validate_model(model, xg_test, y_test)

    def validate_model(self, model, xg_test=None, y_test=None):
        d_matrix = xg_test
        label = y_test

        if xg_test is None or y_test is None:
            data = self.data_manager.get_validation_data()
            y_column = self.config.getint('context', 'y_column')

            x = data[:, 0:y_column]
            label = data[:, y_column]

            d_matrix = xgb.DMatrix(x, label=label)

        prediction = model.predict(d_matrix)

        Imager.generate_heatmap(prediction, label)


        error_rate = np.sum(prediction != label) / label.shape[0]
        print('Error rate after training session is: {}'.format(error_rate))

    def predict_state(self, model):
        prediction = int(model.predict(xgb.DMatrix(self.args.data))[0])
        print(StateMapper().get(prediction).label)
