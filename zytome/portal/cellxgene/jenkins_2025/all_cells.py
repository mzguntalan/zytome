from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "all_cells"

    @property
    def long_name(self) -> str:
        return f"cellxgene.jenkins_2025.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "oropharynx",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "normal",
            "oropharynx squamous cell",
            "carcinoma",
        ]

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
        return 82_844

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/5ee8e8dd-6f0e-4336-aec8-f476b0b0089b.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
