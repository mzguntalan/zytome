from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "longitudinal"

    @property
    def long_name(self) -> str:
        return f"cellxgene.de_vrij_2024.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "blood",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "HIV infectious disease || visceral leishmaniasis",
        ]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 5' v1",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 12_822

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/3542dc7c-a8cb-47f1-820d-fe9754675119.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
