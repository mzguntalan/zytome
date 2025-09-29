from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_pancreas"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "endocrine pancreas",
            "exocrine pancreas",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v3",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 14_140

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/58273b42-9c89-408c-b05d-6bca7a69f2a6.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
