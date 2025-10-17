from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "multiplexed_scrna_from_adult_lupus_samples"

    @property
    def long_name(self) -> str:
        return f"cellxgene.perez_2022.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "blood",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "normal",
            "systemic lupus erythematosus",
        ]

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
        return 1_263_676

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/d51627ad-0123-4eb9-82b0-75f017862307.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
