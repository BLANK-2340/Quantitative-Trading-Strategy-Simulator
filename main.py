import pandas as pd

meld_data = pd.read_excel(r"C:\Users\armaa\Downloads\MELD final sheet.xlsx")
merged_data = pd.read_excel(r"C:\Users\armaa\Downloads\merged_excel_data.xlsx")


meld_emotions = meld_data['Emotion'].value_counts()
merged_emotions = merged_data['Emotion'].value_counts()

print("MELD Emotions Count:\n", meld_emotions)
print("IMOCAP Emotions Count:\n", merged_emotions)
meld_info = meld_data.dtypes
merged_info = merged_data.dtypes

print("MELD Data Types:\n", meld_info)
print("IMOCAP Data Types:\n", merged_info)

meld_missing = meld_data.isnull().sum()
merged_missing = merged_data.isnull().sum()

print("MELD Missing Values:\n", meld_missing)
print("IMOCAP Missing Values:\n", merged_missing)

#print the value

