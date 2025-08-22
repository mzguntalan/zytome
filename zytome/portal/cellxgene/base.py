from abc import ABC
from abc import abstractmethod
from typing import Literal

from zytome.portal._interfaces.dataset import DatasetInterface


class CellXGeneInterface(ABC, DatasetInterface):
    pass
