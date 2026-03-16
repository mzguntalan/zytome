from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "all_cells"

    @property
    def long_name(self) -> str:
        return f"cellxgene.guilliams_2022.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
                "liver",
               ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v3",
            "10x 3' v2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 167_598 

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/fe4bc7fc-0035-4ebb-919b-2d9097ec5dd4.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
