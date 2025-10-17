from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "guimaraes_2024"

    @property
    def long_name(self) -> str:
        return f"cellxgene.guimaraes_2024.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "blood",
            "breast",
            "colorectum",
            "liver",
            "lung",
            "ovary",
            "skin epidermis",
            "uvea",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "normal",
            "breast cancer",
            "colorectal cancer",
            "liver cancer",
            "lung cancer",
            "melanoma",
            "ovarian cancer",
            "uveal melanoma",
        ]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v1",
            "10x 3' v2",
            "10x 3' v3",
            "10x 5' v2",
            "inDrop",
            "Smart-seq2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 391_963

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/8377b008-13bf-45aa-9d5b-0680a997d76d.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
