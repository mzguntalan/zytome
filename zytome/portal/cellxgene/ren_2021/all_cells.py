from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "all_cells"

    @property
    def long_name(self) -> str:
        return f"cellxgene.ren_2021.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
                "blood",
                "lung",
                "saliva",
               ]

    @property
    def diseases(self) -> list[str]:
        return ["normal", "	COVID-19"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v3",
            "10x 5' v2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 1_462_702 

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/891c6eef-a243-41a7-8b47-c8c1a224a193.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
