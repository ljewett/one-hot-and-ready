import pytest

from src.config_manager import ConfigManager


def test_load_config_default_finds_config():
    config = ConfigManager.load_config()
    assert config is not None


def test_load_config_has_necessary_items():
    config = ConfigManager.load_config()
    assert config.has_option('xgbparameters', 'objective')
    assert config.has_option('xgbparameters', 'eta')
    assert config.has_option('xgbparameters', 'max_depth')
    assert config.has_option('xgbparameters', 'num_class')

    assert config.has_option('context', 'model_location')
    assert config.has_option('context', 'train_location')
    assert config.has_option('context', 'test_location')


def test_get_xgbparameters_correctly_casts_items_to_numbers():
    params = ConfigManager.get_xgbparameters()
    for k, v in params.items():
        if k == 'objective' or k == 'eval_metric':
            assert isinstance(v, str)
        elif k == 'eta':
            assert isinstance(v, float)
        else:
            assert isinstance(v, int)


def test_missing_config_throws_error():
    with pytest.raises(FileNotFoundError):
        ConfigManager.load_config("does not exist")