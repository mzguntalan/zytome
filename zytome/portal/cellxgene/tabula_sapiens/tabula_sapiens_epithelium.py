from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_epithelium"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "anterior part of tongue",
            "anterior segment of eyeball",
            "ascending colon",
            "bladder organ",
            "buccal mucosa",
            "cardiac atrium",
            "cardiac ventricle",
            "chorioretinal region",
            "conjunctiva",
            "cornea",
            "cortex of kidney",
            "crista ampullaris",
            "duodenum",
            "endocrine pancreas",
            "endometrium",
            "exocrine pancreas",
            "eye",
            "eyelid",
            "heart",
            "heart right ventricle",
            "ileum",
            "jejunum",
            "kidney",
            "lacrimal gland",
            "large intestine",
            "left ovary",
            "liver",
            "lung",
            "mammary gland",
            "mucosa of stomach",
            "muscle of abdomen",
            "muscle of pelvic diaphragm",
            "myometrium",
            "ocular surface region",
            "ovary",
            "parotid gland",
            "posterior part of tongue",
            "posterior segment of eyeball",
            "prostate gland",
            "right ovary",
            "sclera",
            "sigmoid colon",
            "skin of abdomen",
            "skin of body",
            "skin of chest",
            "small intestine",
            "stomach",
            "stomach smooth muscle",
            "sublingual gland",
            "submandibular gland",
            "testis",
            "thymus",
            "tongue",
            "trachea",
            "uterus",
            "utricle of membranous labyrinth",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return [
            "10x 3' v3",
            "10x 5' v2",
            "Smart-seq2",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 228_032

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/d4893228-f6d9-4252-9a95-7c2c97780067.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
