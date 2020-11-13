import numpy as np
import pandas as pd
# 1-Object creation
# Creating a Series by passing a list of values, letting pandas create a default integer index:
print("-------------------------------Creating a Series ---------------------------------------------")
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

print("-------------------------------Creating a DataFrame ---------------------------------------------")
# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
dates = pd.date_range('20200101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
print(df2.dtypes)
# 2-Viewing data
print("------------------------------- Viewing data  ---------------------------------------------")
# Here is how to view the top and bottom rows of the frame:
print(df.head())
print(df.tail(3))
print("------------------------------- Viewing index + columns  ---------------------------------------------")
print(df.index)
print(df.columns)
print("--------- describe() shows a quick statistic summary of your data  --------------------")
print(df.describe())
# Transposing your data:
print(df.T)
# Sorting by an axis:
print(df.sort_index(axis=1, ascending=False))
# Sorting by values:
print(df.sort_values(by='B'))

# 3 Selection
print("------------------------------- Getting data  ---------------------------------------------")
# Selecting a single column, which yields a Series, equivalent to df.A:
print(df['A'])
# Selecting via [], which slices the rows.
print(df[0:3])
print(df['20200102':'20200104'])
# Selection by label
# Selecting on a multi-axis by label:
print(df.loc[:, ['A', 'B']])
print(df.loc['20200102':'20200104', ['A', 'B']])

# Selection by position
print(df.iloc[3])
print(df.iloc[3:5, 0:2])
# Boolean indexing
print(df[df['A'] > 0])
print(df[df > 0])
# Pivot tables
print("------------------------------- Pivot tables ---------------------------------------------")
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
print(df)
print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))
