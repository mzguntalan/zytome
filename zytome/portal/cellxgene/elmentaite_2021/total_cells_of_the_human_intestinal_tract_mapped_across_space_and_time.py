from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "total_cells_of_the_human_intestinal_tract_mapped_across_space_and_time"

    @property
    def long_name(self) -> str:
        return f"cellxgene.elmentaite_2021.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "ascending colon",
            "caecum",
            "colon",
            "descending colon",
            "duodenum",
            "ileum",
            "jejunum",
            "large intestine",
            "lymph node",
            "mesenteric lymph node",
            "rectum",
            "sigmoid colon",
            "small intestine",
            "transverse colon",
            "vermiform appendix",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "normal",
            "Crohn disease",
        ]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v2",
            "10x 5' v2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 428_469

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/f574f4fb-154e-4ba5-ae85-fd652f2b6a03.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
