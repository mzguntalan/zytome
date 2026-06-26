from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "immunobiology_aging_cohort_pbmc_profiling"

    @property
    def long_name(self) -> str:
        return f"cellxgene.gong_2025.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "blood",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal", "cytomegalovirus infection"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x gene expression flex",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 3_758_514

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/86a284b2-abab-403d-bd1a-e5c7378a53fa.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
