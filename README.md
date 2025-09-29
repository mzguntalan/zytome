# zytome

![Version 0.0.26](https://img.shields.io/badge/version-0.0.26-lightblue)

Zytome is work-in-progress / work-as-i-go library for conveniently downloading data from several sources, filtering, modifying, and manipulating gene expression datasets. This library will grow as I continue to work with gene expression data and will contain essential functionality that are used frequently.

## Sample Usage

```python
# portal is static library that records basic information about datasets
#    like name, tissues, assays, etc
# explorer is the main library for dealing with data
from zytome import portal, explorer

# cellxgene and gtex will be the primary target for now
from zytome.portal.cellxgene.human_oral_and_craniofacial_cell_atlas import oral_and_craniofacial_atlas

# downloads the data to your ENV VAR called Z_ZYTOME_DIR
# by default it creates a .zytome dir at `./` your current working directory
dX = explorer.load_data_from_portal(oral_and_craniofacial_atlas.Dataset())

# dX.filter takes filter functions as parameter
# explorer.make_filter is a utility function for making common filters
# you can make your own filters which are Callable[[AnnData], AnnData]
dX = dX.filter(explorer.make_filter(feature_types=["protein_coding"])

# common attributes are available such as tissues, assays, organism, disease, etc
tissues = dX.tissues

# .raw_normalized_by_feature_length gives you a numpy array
# .raw is also available (raw counts)
cells_by_types = [
    dX.filter(
        explorer.make_filter(
            max_cells=5_00,
            tissues=[tissue]
            )
    ).raw_normalized_by_feature_length
    for tissue in tissues
]

# these will give you gene names
gene_names = dX.feature_names

# this will give you the convention name like ensembl_id
gene_name_convention = dX.feature_name_name
```

## Installation

```bash
pip install --upgrade z-zytome
```
