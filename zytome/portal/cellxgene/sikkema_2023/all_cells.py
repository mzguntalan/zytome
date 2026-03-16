from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "all_cells"

    @property
    def long_name(self) -> str:
        return f"cellxgene.sikkema_2023.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "lung",
            "lung parenchyma",
            "nose",
            "respiratory airway",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "normal",
            "chronic obstructive pulmonary disease",
            "chronic rhinitis",
            "COVID-19",
            "cystic fibrosis",
            "hypersensitivity pneumonitis",
            "interstitial lung disease",
            "lung adenocarcinoma",
            "lung large cell carcinoma",
            "lymphangioleiomyomatosis",
            "non-specific interstitial pneumonia",
            "pleomorphic carcinoma",
            "pneumonia",
            "pulmonary fibrosis",
            "pulmonary sarcoidosis",
            "squamous cell lung carcinoma",
        ]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v1",
            "10x 3' v2",
            "10x 3' v3",
            "10x 5' transcription profiling",
            "10x 5' v1",
            "10x 5' v2",
            "Drop-seq",
            "Seq-Well",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 2_282_447

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/dbb5ad81-1713-4aee-8257-396fbabe7c6e.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
