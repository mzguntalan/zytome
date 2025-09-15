from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_eye"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "anterior segment of eyeball",
            "chorioretinal region",
            "conjunctiva",
            "cornea",
            "eye",
            "eyelid",
            "lacrimal gland",
            "ocular surface region",
            "posterior segment of eyeball",
            "retinal neural layer",
            "sclera",
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
        return 34_273

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/aee26289-b7d2-4643-a32b-6cbc45749f9a.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
