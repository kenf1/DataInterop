library(arrow)
library(magrittr)

#view files in target dir
list.files("./data")

time <- list()

time$start <- Sys.time()

#import parquet file
new_df <- arrow::read_parquet("./data/pl.parquet")

time$end <- Sys.time()

time$elapsed <- time$end - time$start
print(time$elapsed)

#obtain type of each col
col_types <- lapply(new_df,class) %>% unlist()
print(col_types)

rm(time,col_types)
gc()
