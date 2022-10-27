import pandas as pd
excel_table = pd.read_excel('distance.xlsx',header=2,usecols=range(1,10))
print(excel_table.values.tolist())