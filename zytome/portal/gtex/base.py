from abc import ABC
from abc import abstractmethod
from typing import Literal

from zytome.portal._interfaces.dataset import DatasetInterface


class GTExBulkInterface(DatasetInterface):
    """For GTEX Bulk Tissue"""

    @property
    @abstractmethod
    def metadata_link(self) -> str: ...
