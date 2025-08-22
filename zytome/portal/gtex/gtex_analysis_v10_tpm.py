from zytome.portal._interfaces.dataset import Handler
from zytome.portal.gtex.base import GTExBulkInterface


class Dataset(GTExBulkInterface):
    @property
    def short_name(self) -> str:
        return "adult_bulk_tissues"

    @property
    def long_name(self) -> str:
        return f"gtex.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
            "",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

    @property
    def assays(self) -> list[str]:
        return []

    @property
    def organism(self) -> str:
        return "Homo sapiens"

    @property
    def num_cells(self) -> int:
        return 0

    @property
    def download_link(self) -> str:
        return "https://storage.googleapis.com/adult-gtex/bulk-gex/v10/rna-seq/GTEx_Analysis_v10_RNASeQCv2.4.2_gene_tpm.gct.gz"

    @property
    def handler(self) -> Handler:
        return "GTEx"

    @property
    def metadata_link(self) -> str:
        return "https://storage.googleapis.com/adult-gtex/annotations/v10/metadata-files/GTEx_Analysis_v10_Annotations_SampleAttributesDS.txt"

    @property
    def gencode_link(self) -> str:
        return "https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_40/gencode.v40.annotation.gtf.gz"
