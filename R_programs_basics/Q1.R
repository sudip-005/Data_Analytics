
df <- read.csv("data.csv")

colSums(is.na(df))

df_clean <- na.omit(df)

df$Age[is.na(df$Age)] <- mean(df$Age, na.rm=TRUE)

mode_value <- names(sort(table(df$Gender), decreasing=TRUE))[1]
df$Gender[is.na(df$Gender)] <- mode_value

df <- df[!duplicated(df), ]
