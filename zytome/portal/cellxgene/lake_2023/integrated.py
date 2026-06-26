from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "integrated"

    @property
    def long_name(self) -> str:
        return f"cellxgene.lake_2023.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "cortex of kidney",
            "kidney",
            "renal medulla",
            "renal papilla",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v3",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 304_652

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/25b62707-5933-415b-8000-3369ec4af23f.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
