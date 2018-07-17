import pytest

from configparser import ConfigParser

from src.exceptions import ModelNotFound
from src.model_manager import ModelManager


def test_model_manager_missing_model_throws_model_not_found():
    config = ConfigParser()
    config.add_section("context")
    config.set("context", "model_location", "doesNotExist.txt")
    mManager = ModelManager(config)

    with pytest.raises(ModelNotFound):
        mManager.load_model()

