import pandas as pd
import random
print("imports successfull")

'''
Get csv and convert to a dataframe

get a random term from a specific column of csv

'''

INSULT_DATABASE = pd.read_csv("insults.csv", header = None)

#print(INSULT_DATABASE.head())

#returns random term from the appropriate column
def get_random_term (col):
    randRow = random.randint(col, len(INSULT_DATABASE.index)-1)
    term = INSULT_DATABASE.iloc[randRow, col]
    print("new term is: " + str(term))
    return term
