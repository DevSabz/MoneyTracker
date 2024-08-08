import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_descripion


# Class so I can use class methods to call the variable - Practicing basic OOP
class CSV:
    csv_file = "moneytracker_database.csv"
    columns=["date","amount","category", "description"]

    @classmethod
    def init_csv(cls):
        try:
            pd.read_csv(cls.csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.columns)
            df.to_csv(cls.csv_file, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):

# This is a python dictionary - Adds entry to database
        new_entry = {
            "date" : date,
            "amount": amount,
            "category": category,
            "description": description
        }

# This writes to the CSV from the dictionary
        with open(cls.csv_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(new_entry)
        print("Entry added successfully")
            
 
# Calls functions from data entry 
def add():
    CSV.init_csv()
    date = get_date("Enter the date of the transaction in dd-mm-yyyy ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_descripion()
    CSV.add_entry(date, amount, category, description)

add()