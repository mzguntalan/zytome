from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_muscle"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "muscle of abdomen",
            "muscle of pelvic diaphragm",
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
        return 46_772

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/5ff83121-2aed-4e2b-8037-ee23b702645c.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
