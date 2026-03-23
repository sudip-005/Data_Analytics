summary(df)

cor(df[sapply(df, is.numeric)])

boxplot(df$Age)
