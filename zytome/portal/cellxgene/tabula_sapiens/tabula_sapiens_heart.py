from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_heart"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "cardiac atrium",
            "cardiac ventricle",
            "heart",
            "heart right ventricle",
            "right cardiac atrium",
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
        return 25_832

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/762edb8f-1207-4814-831e-99d7a801fdec.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
