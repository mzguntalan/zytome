from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "lung_atlas_10x"

    @property
    def long_name(self) -> str:
        return f"cellxgene.travaglini_2020.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
                "blood",
                "lung",
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
        return 65_662 

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/fb57b6c0-a71f-4d57-bd15-d5a6fe04a4fd.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
