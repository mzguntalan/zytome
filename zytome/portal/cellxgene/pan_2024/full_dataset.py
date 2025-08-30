from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "full_dataset"

    @property
    def long_name(self) -> str:
        return f"cellxgene.pan_2024.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "prefrontal cortex",
            "white matter of frontal lobe",
            "white matter of occipital lobe",
            "white matter of parietal lobe",
            "white matter of temporal lobe",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "normal",
            "Alzheimer disease",
            "leukoencephalopathy, diffuse hereditary, with spheroids",
        ]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v3",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 61_747

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/4cf7e49d-4d48-47d5-b091-56bd78fcbe4b.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
