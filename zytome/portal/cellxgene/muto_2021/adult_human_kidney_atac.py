from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "adult_human_kidney_atac"

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
            "10x scATAC-seq",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 27_034

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/43513175-baf7-4881-9564-c4daa2416026.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
