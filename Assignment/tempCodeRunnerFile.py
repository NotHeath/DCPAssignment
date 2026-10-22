rom pathlib import Path
import pandas as pd

here = Path(__file__).parent
datasheet = pd.read_csv(here / 'tuneindex.csv')

# datasheet.info()

mask = datasheet["title"].str.contains("The", case = False)
filtered = datasheet[mask]

print(filtered("title"))


# Tunes that start with the word "The"

print(datasheet(datasheet["title"].str.startswith("The")))