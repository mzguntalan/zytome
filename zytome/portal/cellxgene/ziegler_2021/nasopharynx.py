from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "nasopharynx"

    @property
    def long_name(self) -> str:
        return f"cellxgene.ziegler_2021.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "nasopharynx",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "normal",
            "COVID-19",
            "long COVID-19",
            "respiratory failure",
        ]

    @property
    def assays(self) -> list[str]:
        return [
            "Seq-Well S3",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 32_588

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/0cbe9711-43f0-4d38-ac05-d1240944b401.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
