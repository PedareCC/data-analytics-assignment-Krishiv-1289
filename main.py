import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read the CSV file into a DataFrame
df = pd.read_csv('Tourism.csv')

#Print the DataFrame. You can delete this later. 
#print(dataframe)

#tourism_dataframe = pd.read_csv('Tourism.csv')

#total_2019 = tourism_dataframe['Trips Ending March 2019'].sum()

#total_2024 = tourism_dataframe['Trips Ending March 2024'].sum()

#print(f'2019: {total_2019} \n 2024: {total_2024}')

#Travel patterns from dif countries
#step one is generate one bar graph for china that shows 2019 v 2024

row_index = 14
column1 = 'Trips Ending March 2019'
column2 = 'Trips Ending March 2024'

row_data = df.loc[row_index, [column1, column2]]

#Plot the bar graph
#write me a menu item that allows the user to select a row and then plot a bar graph for that row

plt.figure(figsize=(8, 6))
plt.bar(row_data.index, row_data.values, color=['blue', 'green'])
plt.xlabel('Columns')
plt.ylabel('Values')
plt.title(f'Bar Graph for Row {row_index}')
plt.show()
