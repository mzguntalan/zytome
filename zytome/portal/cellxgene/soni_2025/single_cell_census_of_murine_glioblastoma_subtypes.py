from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "single_cell_census_murine_glioblastoma_subtypes"

    @property
    def long_name(self) -> str:
        return f"cellxgene.soni_2025.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "brain",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "glioblastoma",
        ]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v3",
        ]

    @property
    def organism(self) -> str:
        return "Mus musculus"

    @property
    def num_cells(self) -> int:
        return 94_181

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/86afbf8c-e49c-4e71-9ba3-e07b571f1acf.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
