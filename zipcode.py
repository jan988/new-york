from uszipcode import SearchEngine, SimpleZipcode, ComprehensiveZipcode

import pandas as pd
df = pd.read_csv('nyc-rolling-sales.csv')


distinct_values = df['ZIP CODE'].unique()

zip_codes = distinct_values.tolist()
zip_code_info = []

search = SearchEngine()

def extract_fields(result):
    return {
        "Zipcode": result.zipcode,
        "population": result.population,
        "population_density": result.population_density,
        "housing_units": result.housing_units,
        "median_home_value": result.median_home_value,
        "median_household_income": result.median_household_income,
    }




for zip_code in zip_codes:
    result = search.by_zipcode(zip_code)
    if result:
        zip_code_info.append(extract_fields(result))


columns = ["Zipcode","population","population_density","housing_units","median_home_value","median_household_income"]

df = pd.DataFrame(zip_code_info, columns=columns)
df.to_csv('zip_code_info.csv', index=False)