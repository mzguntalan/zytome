from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_vasculature"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "abdominal aorta",
            "aorta",
            "coronary artery",
            "inferior vena cava",
            "left coronary artery",
            "thoracic aorta",
            "vasculature",
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
        return 42_650

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/c542113b-cdb7-4a12-9c91-a7363256b872.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
