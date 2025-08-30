from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "inhibitory"

    @property
    def long_name(self) -> str:
        return f"cellxgene.dharshini_2024.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "Brodmann (1909) area 7",
            "Brodmann (1909) area 9",
            "Brodmann (1909) area 17 ",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal", "Alzheimer disease"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v3",
            "Drop-seq",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 79_294

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/bf7f3908-59dd-4560-9567-d754b1329eea.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
