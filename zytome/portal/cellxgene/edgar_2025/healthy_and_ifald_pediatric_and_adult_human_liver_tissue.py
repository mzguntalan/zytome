from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "healthy_ifald_pediatric_and_adult_human_liver_tissue"

    @property
    def long_name(self) -> str:
        return f"cellxgene.edgar_2025.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
                "caudate lobe of liver",
                "left lobe of liver",
                "liver",
                "right lobe of liver",
                
        ]

    @property
    def diseases(self) -> list[str]:
        return [
                "intestinal failure–associated",
                "liver disease",
                "normal",
        ]

    @property
    def assays(self) -> list[str]:
        return [
                "10x 3' v2",
                "10x 3' v3",
                "10x 5' v1",
                "10x 5' v2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 81_001 

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/feca90bb-00df-4623-8398-1e3e6a90971d.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
