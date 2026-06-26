from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "all_cells"

    @property
    def long_name(self) -> str:
        return f"cellxgene.litvinukova_2020.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "apex of heart",
            "heart left ventricle",
            "heart right ventricle",
            "interventricular septum",
            "left cardiac atrium",
            "right cardiac atrium",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v2",
            "10x 3' v3",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 486_134

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/a7f6822d-0e0e-451e-9858-af81392fcb9b.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
