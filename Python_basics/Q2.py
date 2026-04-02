from sklearn.impute import SimpleImputer

num_imputer = SimpleImputer(strategy='mean')
df[['Age']] = num_imputer.fit_transform(df[['Age']])

cat_imputer = SimpleImputer(strategy='most_frequent')
df[['Gender']] = cat_imputer.fit_transform(df[['Gender']])
