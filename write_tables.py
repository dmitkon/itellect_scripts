import pandas as pd

def write_table(tables, path):
    writer = pd.ExcelWriter(path, engine='openpyxl')

    for sheet_name in tables:
        tables[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

        for i, column in enumerate(tables[sheet_name]):
            column_width = max(tables[sheet_name][column].astype(str).map(len).max(), len(column))
            writer.sheets[sheet_name].column_dimensions[chr(i + 65)].width = column_width + 2

    writer.save()