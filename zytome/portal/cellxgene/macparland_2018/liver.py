from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "liver"

    @property
    def long_name(self) -> str:
        return f"cellxgene.macparland_2018.{self.short_name}"

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
            "10x 3' v2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 8_444 

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/42e4c10d-34e4-41ea-928d-818bbf9f00be.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
