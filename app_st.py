
# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df_unified = pd.read_csv("PAE_unified_data.csv")

# Get a summary of the DataFrame
df_summary = df_unified.describe(include='all')

# Count the number of missing values in each column
missing_values = df_unified.isna().sum()

# Count the number of unique values in each column
unique_values = df_unified.nunique()

# Plot the distribution of each column
for col in df_unified.columns:
    if df_unified[col].dtype in ['int64', 'float64']:
        plt.figure(figsize=(10, 5))
        sns.histplot(data=df_unified, x=col, kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()
    else:
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df_unified, y=col, order=df_unified[col].value_counts().index)
        plt.title(f'Count of each category in {col}')
        plt.show()

df_summary, missing_values, unique_values
