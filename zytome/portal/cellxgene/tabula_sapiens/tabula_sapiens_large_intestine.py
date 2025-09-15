from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_large_intenstine"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "ascending colon",
            "large intestine",
            "sigmoid colon",
        ]

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
        return 30_084

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/82e3b450-6704-43de-8036-af1838daa7df.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
