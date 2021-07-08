import pandas as pd
import matplotlib.pyplot as plt

# COVID data
# Pull remote data from the Chicago Data Portal API
covid_chicago_url = 'https://data.cityofchicago.org/resource/2vhs-cf6b.json'
covid_df = pd.read_json(covid_chicago_url,  # Uses url to find/use data # This converts 'date' column to a nicer format
                        convert_dates=['date'])
# Set index to 'date' column
covid_df = covid_df.set_index('date')
# Save it to file for future access
covid_df.to_csv('covid-chicago.csv')
covid_df.head()

covid_df = pd.read_csv('covid-chicago.csv', index_col=0, parse_dates=True)
covid_df['total_doses_daily'].plot()
# Average by week #
covid_df['total_doses_daily'].rolling('7d').mean().plot()
population_url = 'https://data.cityofchicago.org/resource/85cm-7uqa.json'
pop_df = pd.read_json(population_url)
# Ignore zip code results and just select citywide totals
chicago_pop_df = pop_df[pop_df['geography_type'] == 'Citywide']
chicago_pop_df.head()
# Use most recent results - 2019
pop_2019_df = chicago_pop_df[chicago_pop_df['year'] == 2019]
# This shows you every column in your dataset,
# So you can select the data you're interested in
pop_2019_df.columns
for subgroup in ['_age_0_17',
                 '_age_18_29',
                 '_age_30_39',
                 '_age_40_49',
                 '_age_50_59',
                 '_age_60_69',
                 '_age_70_79',
                 '_age_12_17',
                 '_female',
                 '_male',
                 '_latinx',
                 '_asian_non_latinx',
                 '_black_non_latinx',
                 '_white_non_latinx',
                 ]:
    # Add up daily counts to get total num vaccinated
    vacc_column = 'vaccine_series_completed_daily' + subgroup
    vacc_total = covid_df[vacc_column].sum()
    # Divide by subgroup population
    pop_total = pop_2019_df['population' + subgroup]
    vacc_percent = vacc_total / pop_total
    print(subgroup, f'{int(100*vacc_percent)}%')
    # Outputs total number of people vaccinated in Chicago
vacc_total
