from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_skin"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "buccal mucosa",
            "skin of abdomen",
            "skin of body",
            "skin of chest",
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
        return 17_786

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/6b7622c2-4810-4bbb-856d-0fa7232d7c14.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
