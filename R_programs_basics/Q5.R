Q1 <- quantile(df$Age, 0.25)
Q3 <- quantile(df$Age, 0.75)
IQR <- Q3 - Q1
df <- df[df$Age >= (Q1 - 1.5*IQR) & df$Age <= (Q3 + 1.5*IQR), ]
