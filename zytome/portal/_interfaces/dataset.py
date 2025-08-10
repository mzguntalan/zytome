from abc import ABC
from abc import abstractmethod
from typing import Literal

Handler = Literal[
    "CellXGene",
    "GTEx",
]


class DatasetInterface(ABC):
    @property
    @abstractmethod
    def short_name(self) -> str:
        """The short name responds to the name most visible when visiting this dataset's link"""
        ...

    @property
    @abstractmethod
    def long_name(self) -> str:
        """Roughly: <portal>-<dataset-name>-<dataset-subset-name>"""
        ...

    @property
    @abstractmethod
    def tissues(self) -> list[str]:
        """Tissue names"""
        ...

    @property
    @abstractmethod
    def diseases(self) -> list[str]:
        """Disease Names"""
        ...

    @property
    @abstractmethod
    def assays(self) -> list[str]:
        """Assays"""
        ...

    @property
    @abstractmethod
    def organism(self) -> str:
        """Organism Name"""
        ...

    @property
    @abstractmethod
    def num_cells(self) -> int:
        """Total number of cells in this dataset"""
        ...

    @property
    @abstractmethod
    def download_link(self) -> str: ...

    @property
    @abstractmethod
    def handler(self) -> Handler:
        """Tells explorer how to handle this dataset"""
