from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_endothelium"

    @property
    def long_name(self) -> str:
        return f"cellxgene.tabula_sapiens.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "abdominal aorta",
            "adipose tissue",
            "anterior part of tongue",
            "anterior segment of eyeball",
            "aorta",
            "ascending colon",
            "bladder organ",
            "bone marrow",
            "brown adipose tissue",
            "buccal mucosa",
            "cardiac atrium",
            "cardiac ventricle",
            "chorioretinal region",
            "conjunctiva",
            "cornea",
            "coronary artery",
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
            "inferior vena cava",
            "inguinal lymph node",
            "jejunum",
            "kidney",
            "lacrimal gland",
            "large intestine",
            "left coronary artery",
            "left ovary",
            "liver",
            "lung",
            "lymph node",
            "mammary gland",
            "mesenteric lymph node",
            "mucosa of stomach",
            "muscle of abdomen",
            "muscle of pelvic diaphragm",
            "myometrium",
            "ovary",
            "parotid gland",
            "posterior part of tongue",
            "posterior segment of eyeball",
            "prostate gland",
            "right cardiac atrium",
            "right ovary",
            "sclera",
            "sigmoid colon",
            "skin of abdomen",
            "skin of body",
            "skin of chest",
            "small intestine",
            "spleen",
            "stomach",
            "stomach smooth muscle",
            "subcutaneous adipose tissue",
            "sublingual gland",
            "submandibular gland",
            "testis",
            "thoracic aorta",
            "thymus",
            "trachea",
            "uterus",
            "utricle of membranous labyrinth",
            "vasculature",
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
            "Smart-seq3",
        ]

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 73_195

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/f7c09c0d-b206-4e26-9764-09be32c0e4d4.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
