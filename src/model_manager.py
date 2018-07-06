import xgboost as xgb

from src.exceptions import ModelNotFound


class ModelManager:
    def __init__(self, config):
        self.config = config

    def save_model(self, model):
        model_location = self.config.get('context', 'model_location')
        model.save_model(model_location)

    def load_model(self):
        model_location = self.config.get('context', 'model_location')

        try:
            bst = xgb.Booster()
            bst.load_model(model_location)
            return bst
        except Exception as e:
            print(e)
            raise ModelNotFound("Model file was unable to Load")