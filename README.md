# Projet AAA

To run main.r, you will need to install Pault Pearson's ```TDA Mapper``` and and Christopher Gandrud's ```igraph```

```
library(devtools)
devtools::install_github("paultpearson/TDAmapper")
devtools::install_github("christophergandrud/networkD3")
```


# Naming conventions

 Naming convention:
 `[filter_value_id]_[num_intervals_x]_[num_intervals_y]_[percent_overlap]_[num_bins].html`

 1. PCA1 + PCA2
 2. PCA1 + angles
 3. tsne
 4. PCA1 + PCA2 - order
 5. PCA1 + angles - order
 6. tsne - order
