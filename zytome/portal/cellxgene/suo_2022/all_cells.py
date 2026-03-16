from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "all_cells"

    @property
    def long_name(self) -> str:
        return f"cellxgene.suo_2022.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "bone marrow",
            "gut wall",
            "kidney",
            "liver",
            "mesenteric lymph node",
            "skin of body",
            "spleen",
            "thymus",
            "yolk sac",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v2",
            "10x 5' v1",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 908_046

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/4eb0a1aa-216c-4f22-93ab-85e95ed70cbb.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
