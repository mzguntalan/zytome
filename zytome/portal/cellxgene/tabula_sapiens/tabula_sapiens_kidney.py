from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_kidney"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return ["cortex of kidney", "kidney"]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v3",
            "Smart-seq2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 11_376

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/01e3402f-a625-4c4d-b94a-bc5996f738f7.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
