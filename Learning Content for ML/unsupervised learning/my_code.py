import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df = pd.read_excel('University_Clustering.xlsx')

df.head()

df.shape

"""
Columns details - 

| Column       | Meaning                                                                                                               | Data Type          | Example             |
| ------------ | --------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------- |
| UnivID   | Unique ID assigned to each university. It is only an identifier and usually not useful for machine learning.          | Integer            | 1, 2, 3             |
| Univ     | Name of the university.                                                                                               | Categorical (Text) | Brown, CalTech, CMU |
| State    | State where the university is located.                                                                                | Categorical        | RI, CA, NY          |
| SAT      | Average SAT score of admitted students. Higher value means academically stronger students.                            | Numerical          | 1310, 1415          |
| Top10    | Percentage of admitted students who were in the top 10% of their high school class.                               | Numerical (%)      | 89, 100             |
| Accept   | Acceptance rate (percentage of applicants admitted). Lower means the university is more selective.                    | Numerical (%)      | 22, 59              |
| SFRatio  | Student-to-Faculty Ratio. It tells how many students are assigned to one faculty member. Smaller is generally better. | Numerical          | 6, 13               |
| Expenses | Annual cost of studying at the university (tuition, housing, etc.).                                                   | Numerical          | 22704, 63575        |
| GradRate | Graduation rate (% of students who successfully graduate). Higher is better.                                          | Numerical (%)      | 94, 81              |
"""

df.info()

df.isnull().sum()

df[df['SAT'].isnull()]

# for i in df.select_dtypes(np.number).columns:
#     df[i].plot(kind="box",subplots=True)
#     plt.show()


df['SAT'].describe()

df['SAT'] = df['SAT'].fillna(df.SAT.mean())

df.info()

df['GradRate'] = df['GradRate'].fillna(df['GradRate'].mean())

# univid is useless deleting it
df= df.drop(columns="UnivID")

cat = df.select_dtypes("object").columns
num = df.select_dtypes(np.number).columns

cat
num

# now creating a transformer

transformer = ColumnTransformer(
    [
        ("cat",OneHotEncoder(),cat),
        ("num",StandardScaler(),num)
    ]
)

transformer.set_output(transform="pandas")

# creating a pipeline
clean_df = transformer.fit_transform(df)

clean_df

df['State'].value_counts()

clean_df.describe()

