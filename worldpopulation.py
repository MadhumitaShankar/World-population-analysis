# -*- coding: utf-8 -*-
"""worldpopulation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eY9qiJjuG4qejQEGx_7mCdwfPtZfPj8h
"""

import pandas as pd

file_path = '/content/world_population.excel'
df = pd.read_csv(file_path)

column_info = df.dtypes.reset_index()
column_info.columns = ['Column Name', 'Data Type']

column_info['Entry Count'] = df.count().values

print(column_info)

numeric_columns = column_info[column_info['Data Type'].isin(['int64', 'float64'])]['Column Name']

# Plot histograms for numeric columns
for column in numeric_columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'{column}')
    plt.show()

import matplotlib.pyplot as plt
import seaborn as sns  # Add this import statement

# Your code to load the dataset and display column information

# Plot countplot for categorical columns
for column in categorical_columns:
    plt.figure(figsize=(12, 6))
    sns.countplot(x=column, data=df, palette='viridis')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.title(f' {column}')
    plt.xticks(rotation=45, ha='right')
    plt.show()