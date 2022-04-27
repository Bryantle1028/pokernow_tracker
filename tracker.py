import collections
import pandas as pd
import os

EXISTING_LEDGER = 'existing_ledger.csv'
DEFAULT_DOWNLOAD_PATH = '/Users/bryantle/Downloads/'

def main():
    player_stats = collections.defaultdict(dict)

    download_path = input("Please enter download path (Enter for default path): ")
    download_path = DEFAULT_DOWNLOAD_PATH if not download_path else download_path

    # use regex to read anything that matches ledger_*.csv and delete later
    new_ledger_df = pd.read_csv('ledger_*.csv')

    # possibly use groupby for just the net values
    for row in new_ledger_df.iterrows():
        

    # check for existing ledger
    existing_file = os.find(EXISTING_LEDGER)
    if not existing_file:

if __name__ == '__main__':
    main()
