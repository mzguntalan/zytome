from zytome.portal._interfaces.dataset import DatasetInterface as Api
from zytome.portal._interfaces.dataset import Handler


class Dataset(Api):
    @property
    def short_name(self) -> str:
        return "all_neurons"

    @property
    def long_name(self) -> str:
        return f"cellxgene.siletti_2023.{self.short_name}"

    @property
    def tissues(self) -> list[str]:
        return [
                "accessory basal amygdaloid nucleus",
"agranular insular cortex",
"anterior cortical amygdaloid nucleus",
"anterior nuclear group",
"anterior olfactory nucleus",
"basolateral amygdaloid nuclear complex",
"bed nucleus of stria terminalis",
"body of caudate nucleus",
"Brodmann (1909) area 13",
"Brodmann (1909) area 14",
"Brodmann (1909) area 19",
"Brodmann (1909) area 23",
"Brodmann (1909) area 24",
"Brodmann (1909) area 25",
"Brodmann (1909) area 32",
"Brodmann (1909) area 35",
"Brodmann (1909) area 38",
"Brodmann (1909) area 40",
"Brodmann (1909) area 43",
"Brodmann (1909) area 46",
"central amygdaloid nucleus",
"centromedian nucleus of thalamus",
"cerebellar nuclear complex",
"cerebellar vermis",
"cerebrocerebellum",
"claustrum of brain",
"corticomedial nuclear complex",
"cuneus cortex",
"dentate gyrus of hippocampal formation",
"dorsal tegmental nucleus",
"epithalamus",
"extrastriate cortex",
"globus pallidus",
"granular insular cortex",
"gray matter of midbrain",
"hippocampal field",
"hypothalamus",
"inferior frontal gyrus",
"inferior olivary complex",
"inferior temporal gyrus",
"intralaminar nuclear group",
"lateral amygdaloid nucleus",
"lateral entorhinal cortex",
"lateral geniculate body",
"lateral nuclear group of thalamus",
"lateral posterior nucleus of thalamus",
"mammillary body",
"medial dorsal nucleus of thalamus",
"medial entorhinal cortex",
"medial geniculate body",
"medial zone of hypothalamus",
"median tuberal portion",
"midbrain nucleus",
"midbrain tectum",
"middle temporal gyrus",
"nucleus accumbens",
"nucleus of dorsal thalamus",
"nucleus of medulla oblongata",
"parabrachial nucleus",
"perirhinal cortex",
"piriform cortex",
"pontine nuclear group",
"pontine reticular formation",
"pontine tegmentum",
"posterior parahippocampal gyrus",
"preoptic area",
"pretectal region",
"primary auditory cortex",
"primary motor cortex",
"primary somatosensory cortex",
"primary visual cortex",
"pulvinar nucleus",
"putamen",
"red nucleus",
"retrosplenial region",
"rostral CA3",
"septal nuclear complex",
"spinal cord",
"subicular complex",
"substantia innominata",
"substantia nigra",
"subthalamic nucleus",
"superior parietal cortex",
"superior temporal gyrus",
"supraoptic nucleus",
"temporal fusiform gyrus",
"uncal CA1",
"ventral anterior nucleus of thalamus",
        ]

    @property
    def diseases(self) -> list[str]:
        return ["normal"]

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
        return 2_480_956 

    @property
    def download_link(self) -> str:
        return "https://datasets.cellxgene.cziscience.com/a71efd3c-765c-466b-8eca-0b29024094d4.h5ad"

    @property
    def handler(self) -> Handler:
        return "CellXGene"
