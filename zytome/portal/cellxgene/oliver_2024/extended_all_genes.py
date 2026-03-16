from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "extended_all_genes"

    @property
    def long_name(self) -> str:
        return f"cellxgene.oliver_2024.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "ascending colon",
            "body of stomach",
            "buccal mucosa",
            "caecum",
            "colon",
            "colonic epithelium",
            "colonic mucosa",
            "descending colon",
            "duodenal epithelium",
            "duodenum",
            "epithelium of esophagus",
            "epithelium of rectum",
            "epithelium of small intestine",
            "epithelium of stomach",
            "esophagus",
            "gingiva",
            "ileal epithelium",
            "ileum",
            "ileum lamina propria",
            "intestine",
            "jejunum",
            "labial gland",
            "lamina propria of mucosa of colon",
            "lamina propria of small intestine",
            "mesenteric lymph node",
            "parotid gland",
            "periodontium",
            "pyloric antrum",
            "pylorus",
            "rectosigmoid junction",
            "rectum",
            "sigmoid colon",
            "small intestine",
            "stomach",
            "transverse colon",
            "vermiform appendix",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "normal",
            "colorectal cancer",
            "Crohn disease",
            "gastric cancer",
            "inflammatory bowel disease",
            "ulcerative colitis",
        ]

    @property
    def assays(self) -> list[str]:
        return [
            "`10x 3' v1",
            "10x 3' v2",
            "10x 3' v3",
            "10x 5' transcription profiling",
            "10x 5' v1",
            "10x 5' v2`",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 1_358_573

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/a0a6b5b8-afb9-4911-a1c5-ce1c9b6aa057.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
