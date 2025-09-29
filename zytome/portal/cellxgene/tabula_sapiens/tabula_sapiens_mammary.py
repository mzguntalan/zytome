from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_mammary"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return ["mammary_gland"]

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
        return 30_936

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/a1c5ecd4-54a1-4a88-b4c8-518c8697cefc.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
