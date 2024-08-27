import pandas as pd
import time
import os
import matplotlib.pyplot as plt
import seaborn as sns  # Ensure you have this import for the color palette

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def travelcompare():
    df = pd.read_csv('Tourism.csv')
    df['Trips Ending March 2019'] = pd.to_numeric(df['Trips Ending March 2019'], errors='coerce')
    df['Trips Ending March 2024'] = pd.to_numeric(df['Trips Ending March 2024'], errors='coerce')
    df['Spend Ending March 2019'] = pd.to_numeric(df['Spend Ending March 2019'], errors='coerce')
    df['Spend Ending March 2024'] = pd.to_numeric(df['Spend Ending March 2024'], errors='coerce')
    df.fillna(0, inplace=True)
    df.to_csv('Tourism_cleaned.csv', index=False)

    new_df = pd.read_csv('Tourism_cleaned.csv')
    print(new_df)

    total_2019 = new_df['Trips Ending March 2019'].sum()
    total_2024 = new_df['Trips Ending March 2024'].sum()

    print(f'Total number of travelers in 2019: {total_2019}')
    print(f'Total number of travelers in 2024: {total_2024}')

    plt.figure(figsize=(8, 6))
    plt.bar(['2019', '2024'], [total_2019, total_2024], color=['blue', 'orange'])
    plt.xlabel('Year')
    plt.ylabel('Total Number of Travelers')
    plt.ylim(min(total_2019, total_2024) - 500, max(total_2019, total_2024) + 50)
    plt.title('Total Number of Travelers in 2019 vs. 2024')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.savefig('Travelers_Comparison.png')
    plt.show()

def spenddata():
    df = pd.read_csv('reasons4travel.csv')
    df['Trips Ending March 2019'] = pd.to_numeric(df['Trips Ending March 2019'], errors='coerce')
    df['Trips Ending March 2024'] = pd.to_numeric(df['Trips Ending March 2024'], errors='coerce')
    df['Spend Ending March 2019'] = pd.to_numeric(df['Spend Ending March 2019'], errors='coerce')
    df['Spend Ending March 2024'] = pd.to_numeric(df['Spend Ending March 2024'], errors='coerce')
    df.fillna(0, inplace=True)

    categories = df['Unnamed: 0']
    colors = sns.color_palette('hsv', len(categories))

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    for i, category in enumerate(categories):
        plt.bar(category, df.loc[i, 'Trips Ending March 2019'], color=colors[i], alpha=0.7, label=f'{category} 2019')
        plt.bar(category, df.loc[i, 'Trips Ending March 2024'], color=colors[i], alpha=0.4, label=f'{category} 2024')
    plt.xlabel('Category')
    plt.ylabel('Number of Trips')
    plt.title('Number of Trips in 2019 vs. 2024')
    plt.xticks(rotation=45, ha='right')

    plt.subplot(1, 2, 2)
    for i, category in enumerate(categories):
        plt.bar(category, df.loc[i, 'Spend Ending March 2019'], color=colors[i], alpha=0.7, label=f'{category} 2019')
        plt.bar(category, df.loc[i, 'Spend Ending March 2024'], color=colors[i], alpha=0.4, label=f'{category} 2024')
    plt.xlabel('Category')
    plt.ylabel('Amount Spent')
    plt.title('Amount Spent in 2019 vs. 2024')
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig('Trips_and_Spend_Comparison.png')
    plt.show()

def modeselection():
    while True:
        print('Select a mode to see data for your selected mode: \n 1. Trips Changing \n 2. Spending \n Type "exit" to leave.')
        mode = input('Enter your mode with the number or say "exit": ')

        if mode == '1':
            print('You have selected Trips Changing, please wait for the graph to load.')
            travelcompare()
            time.sleep(5)
            clear()

        elif mode == '2':
            print('You have selected Spending, please wait for the graph to load.')
            spenddata()
            time.sleep(5)
            clear()

        elif mode.lower() == 'exit':
            print('Exiting...')
            time.sleep(2)
            clear()
            print('Exited menu.')
            break

        else:
            print('Please select a valid option. This menu will reset in 3 seconds.')
            time.sleep(3)
            clear()

modeselection()
