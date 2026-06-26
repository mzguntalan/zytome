from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "all_cells"

    @property
    def long_name(self) -> str:
        return f"cellxgene.reynolds_2021.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "dermis",
            "skin epidermis ",
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
        return 195_739

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/a195debd-2179-4626-be55-68fa6e05d19d.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
