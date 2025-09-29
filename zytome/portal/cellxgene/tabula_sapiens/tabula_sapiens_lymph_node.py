from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_lymph"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "inguinal lymph node",
            "lymph node",
            "mesenteric lymph node",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v3",
            "10x 5' v2",
            "Smart-seq2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 129_062

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/95536bb1-ffa2-4788-bf5b-149c55ccd8b1.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
