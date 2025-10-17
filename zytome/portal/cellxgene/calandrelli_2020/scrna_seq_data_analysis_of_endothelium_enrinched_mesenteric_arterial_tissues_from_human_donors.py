from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "scrna_seq_data_analysis_of_endothelium_enriched_mesenteric_arterial_tissues_from_human_donors"

    @property
    def long_name(self) -> str:
        return f"cellxgene.calandrelli_2020.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "mesenteric artery",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "normal",
            "type 2 diabetes mellitus",
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
        return 11_243

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/71a7abad-0f7c-45e5-b465-1b32a4a47a56.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
