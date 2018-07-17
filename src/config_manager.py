from configparser import ConfigParser


class ConfigManager:
    @staticmethod
    def load_config(config_file="config.ini"):
        config = ConfigParser()
        with open(config_file, 'r') as fp:
            config.read_file(fp)
        return config

    @staticmethod
    def get_xgbparameters():
        config = ConfigManager.load_config()
        params = dict(config._sections['xgbparameters'])
        for k, v in params.items():
            if k == 'eta':
                params[k] = float(v)
            elif k != 'objective' and k != 'eval_metric':
                params[k] = int(v)
        return params