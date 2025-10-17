from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return (
            "scrna_seq_data_analysis_of_huvecs_treated_with_high_glucose_and_tnfalpha"
        )

    @property
    def long_name(self) -> str:
        return f"cellxgene.calandrelli_2020.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "endothelial cell (cell culture)",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "normal",
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
        return 59_605

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/42488ac3-85ec-4103-92f8-95907ff481c9.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
