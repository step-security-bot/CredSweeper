import os

from credsweeper.app import CredSweeper
from credsweeper.common.constants import ThresholdPreset
from credsweeper.file_handler import ContentProvider, ByteContentProvider, DiffContentProvider, StringContentProvider, \
    DataContentProvider, \
    TextContentProvider
from credsweeper.ml_model.ml_validator import MlValidator
from credsweeper.validations.apply_validation import ApplyValidation

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

__all__ = [
    'ApplyValidation',  #
    'ByteContentProvider',  #
    'ContentProvider',  #
    'CredSweeper',  #
    'DataContentProvider',  #
    'DiffContentProvider',  #
    'MlValidator',  #
    'StringContentProvider',  #
    'TextContentProvider',  #
    'ThresholdPreset',  #
    '__version__'
]

__version__ = "1.4.2"
