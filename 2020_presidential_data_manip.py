import os

import rpy2 
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
# atm, rpy 3.5.6 doesn't allow proper use of robjects, so use v3.5.4 instead

import numpy as np
import pandas as pd

from election_obj import Election
from state_obj import State

def csv_to_array(csv_data):
    return pd.read_csv(csv_data)

county_level_2020_presidential = pd.read_csv('2020_US_County_Level_Presidential_Results.csv')

def get_df_by_state(state):
    state_r_df = robjects.r('''
        results <- read.csv('2020_US_County_Level_Presidential_Results.csv')
        reqd_results <- data.frame(
            state_name=results$state_name, 
            county_fips=results$county_fips, 
            county_name=results$county_name, 
            votes_gop=results$votes_gop, 
            votes_dem=results$votes_dem, 
            total_votes=results$total_votes)
        state_results <- subset(reqd_results, state_name==''' + "'" + state + "'" + ''')
        ''')

    with localconverter(robjects.default_converter + pandas2ri.converter):
        state_pd_df = robjects.conversion.rpy2py(state_r_df)
    return state_pd_df

states_list = county_level_2020_presidential.loc[:, 'state_name'].drop_duplicates()

for i in range(states_list.size):
    current_state = states_list.iat[i]
    state_table = get_df_by_state(current_state)
    output_directory = current_state + '_county_level_2020_presidential_results.csv'
    state_table.to_csv('states_2020_county_level_presidential_data/'+output_directory, index=False)

# print(type(get_table_by_state('Tennessee')))

