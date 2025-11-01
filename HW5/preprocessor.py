
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler


class Preprocessor:
    def __init__(self, df):
        self.df = df.copy()

    def handle_missing_values(self):
        self.df.fillna(0, inplace=True)

    def handling_cat_cols(self, cols) :
        for c in cols:
          one_hot_encoded_df = pd.get_dummies(self.df[c], prefix=c)
          self.df = self.df.join(one_hot_encoded_df)
          self.df.drop(c, axis=1, inplace=True)

    def remove_junk_cols(self , cols):
        for c in cols:
          print(c)
          self.df.drop(c, axis=1, inplace=True)

    def normalize(self , cols , scaler):
        self.df[cols] = scaler.fit_transform(df[cols])

    def reduce_dimensions(self , n_comp):
        pca = PCA(n_components=n_comp)
        self.df = pca.fit_transform(self.df.to_numpy())
        self.df = pd.DataFrame(self.df)
        self.df.columns = self.df.columns.astype(str)

    def transform(self ,
                  cat_cols = ['Gender'],
                  junk_cols = ['CustomerID'],
                  numerical_cols = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)'] ,
                  scaler = MinMaxScaler() ,
                  n_comp = 2):
        self.handle_missing_values()
        self.handling_cat_cols(cat_cols)
        self.remove_junk_cols(junk_cols)
        self.normalize(numerical_cols , scaler)
        self.reduce_dimensions(n_comp)
        return self.df
