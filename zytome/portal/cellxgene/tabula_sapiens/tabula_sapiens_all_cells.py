from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "tabula_sapiens_all_cells"

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
            "blood",
            "bone marrow",
            "brown adipose tissue",
            "buccal mucosa",
            "cardiac atrium",
            "cardiac ventricle",
            "chorioretinal region",
            "conjunctiva",
            "cornea",
            "coronary artery",
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
            "muscularis mucosae of stomach",
            "myometrium",
            "ocular surface region",
            "ovary",
            "parotid gland",
            "posterior part of tongue",
            "posterior segment of eyeball",
            "prostate gland",
            "retinal neural layer",
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
            "tongue",
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
        return 1_136_218

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/946fa48d-a0ac-4e5b-80fc-1d96cb5083a7.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
