from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "multiomics_single_cell_analysis_of_human_pancreatic_islets"

    @property
    def long_name(self) -> str:
        return f"cellxgene.fasolino_2022.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "islet of Langerhans",
        ]

    @property
    def diseases(self) -> list[str]:
        return [
            "normal",
            "type 1 diabetes mellitus",
        ]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v2",
            "10x 3' v3",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 69_645

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/5378ac26-e216-41e8-b171-a7f4d819a9ff.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
