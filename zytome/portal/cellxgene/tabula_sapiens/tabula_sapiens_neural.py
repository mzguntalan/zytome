from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_neural"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "anterior segment of eyeball",
            "ascending colon",
            "cornea",
            "duodenum",
            "eye",
            "heart",
            "heart right ventricle",
            "ileum",
            "lacrimal gland",
            "large intestine",
            "posterior segment of eyeball",
            "retinal neural layer",
            "right cardiac atrium",
            "sclera",
            "sigmoid colon",
            "small intestine",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v3",
            "Smart-seq2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 2_685

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/9e496fac-5ad3-48ed-9733-4c5445ae5f60.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
