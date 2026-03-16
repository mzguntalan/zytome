from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "global"

    @property
    def long_name(self) -> str:
        return f"cellxgene.dominguez_2022.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "blood",
            "bone marrow",
            "caecum",
            "duodenum",
            "ileum",
            "jejunal epithelium",
            "jejunum lamina propria",
            "liver",
            "lung",
            "mesenteric lymph node",
            "omentum",
            "sigmoid colon",
            "skeletal muscle tissue",
            "spleen",
            "thoracic lymph node",
            "thymus",
            "transverse colon",
           ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
                "10x 3' v3",
                "10x 5' v1",
                "10x 5' v2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 329_762 

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/f4a41bce-b0ea-4c88-a3c3-55492dbd15d5.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
