from collections import defaultdict

import pandas as pandas


def get_correct_form_year(year) -> str:
    if year % 10 in [5, 6, 7, 8, 9, 0] or year in range(11, 20):
        return 'лет'
    else:
        return 'года' if year % 10 > 1 else 'год'


def get_drinks():
    excel_data_df = pandas.read_excel('test/wine3.xlsx', na_values=['N/A', 'NA'], keep_default_na=False)

    grouped_drinks = defaultdict(list)

    for drink in excel_data_df.to_dict(orient='records'):
        grouped_drinks[drink['Категория']].append(drink)
    return grouped_drinks
