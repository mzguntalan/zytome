from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "adult_human_kidney_rna"

    @property
    def long_name(self) -> str:
        return f"cellxgene.muto_2021.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "cortex of kidney",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

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
        return 19_985

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/ff2e21de-0848-4346-8f8b-4e1741ec4b39.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
