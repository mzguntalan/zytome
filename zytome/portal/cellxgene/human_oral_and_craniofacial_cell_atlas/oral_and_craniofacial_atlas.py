from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "oral_and_craniofacial_atlas"

    @property
    def long_name(self) -> str:
        return f"cellxgene.human_oral_and_craniofacial_cell_atlas.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "buccal mucosa",
            "dental pulp",
            "gingiva",
            "hard palate",
            "minor salivary gland",
            "mucosa of dorsum of tongue",
            "mucosa of lip",
            "parotid gland",
            "periodontium",
            "soft palate",
            "sublingual gland",
            "submandibular gland",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return ["10x 3' v2", "10x 3 v3"]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 246_103

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/96213940-ad67-4e1d-80bf-487aae104c43.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
