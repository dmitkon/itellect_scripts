import pandas as pd

def write_table(sheets, path):
    writer = pd.ExcelWriter(path, engine='openpyxl')

    for sheet_name in sheets.keys():
        sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()