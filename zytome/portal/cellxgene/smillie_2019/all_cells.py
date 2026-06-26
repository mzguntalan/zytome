from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "all_cells"

    @property
    def long_name(self) -> str:
        return f"cellxgene.smillie_2019.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "caecum epithelium",
            "colonic epithelium",
            "mucosa of transverse colon",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v1",
            "10x 3' v2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 34_772

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/e373cf41-e123-4c98-a8bb-a531c7bbedd2.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
