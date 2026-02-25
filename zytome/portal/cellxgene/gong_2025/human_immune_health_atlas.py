from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "human_imune_health_atlas"

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
            "10x 3' v3",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 1_821_725 

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/39832a61-3df1-4f1f-971d-3c2a74539047.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
