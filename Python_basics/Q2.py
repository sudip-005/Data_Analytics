from sklearn.impute import SimpleImputer

# Numerical Imputation
num_imputer = SimpleImputer(strategy='mean')
df[['Age']] = num_imputer.fit_transform(df[['Age']])

# Categorical Imputation
cat_imputer = SimpleImputer(strategy='most_frequent')
df[['Gender']] = cat_imputer.fit_transform(df[['Gender']])
