install.packages("mice")
library(mice)
imputed_data <- mice(df, method='pmm', m=5)
df <- complete(imputed_data)
