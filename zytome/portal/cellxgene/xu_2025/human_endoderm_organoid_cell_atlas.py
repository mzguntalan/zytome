from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "human_endoderm_organoid_cell_atlas"

    @property
    def long_name(self) -> str:
        return f"cellxgene.xu_2025.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "alveolar sac (organoid)",
            "biliary system (organoid)",
            "bronchus (organoid)",
            "colon (organoid)",
            "common bile duct (organoid)",
            "corpus (organoid)",
            "duodenum (organoid)",
            "gallbladder (organoid)",
            "ileum (organoid)",
            "intestine (organoid)",
            "intrahepatic bile duct (organoid)",
            "liver (organoid)",
            "lung (organoid)",
            "lung epithelium (organoid)",
            "nasopharynx (organoid)",
            "pancreas (organoid)",
            "prostate gland (organoid)",
            "pyloric antrum (organoid)",
            "salivary gland epithelium (organoid)",
            "stomach (organoid)",
            "thyroid gland (organoid)",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v2",
            "10x 3' v3",
            "10x 5' v1",
            "10x multiome",
            "CEL-seq2",
            "Seq-Well S3",
            "Smart-seq",
            "SORT-seq",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 806_646

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/c49c8589-0221-4955-b547-270f8d67d13f.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
