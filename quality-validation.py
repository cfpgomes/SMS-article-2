# Code to validate quality assessment of articles.

# For plots.
from tkinter.messagebox import NO
from pip import main
import plotly.express as px

# For csv reading.
import pandas as pd

# For maths.
import numpy as np

# For fuzzy markers
import random

# Functions
def retrieve_quartile(row, dic_quartiles_dfs):
    title = row['Publication Title']
    sourceID = row['SourceID']
    year = row['Publication Year']
    if (year == 2022):
        return None

    print(f'Title: {title}\nSourceID: {sourceID}')
    df_quartiles = dic_quartiles_dfs[f'{year}']

    df_title_contains = df_quartiles[df_quartiles['Sourceid'] == sourceID]

    if df_title_contains.empty:
        print('Empty!')
        return None

    print(f'Article from year {year}')
    print(df_title_contains.iloc[0][f'SJR Best Quartile'])

    return df_title_contains.iloc[0]['SJR Best Quartile']

def retrieve_conference(row, dic_conferences_dfs):
    title = row['Publication Title']
    conferenceID = row['ConferenceID']
    year = row['Publication Year']
    if (year == 2022):
        return None

    print(f'Title: {title}\ConferenceID: {conferenceID}')
    df_conferences = dic_conferences_dfs[f'{year}']

    df_title_contains = df_conferences[df_conferences[0] == conferenceID]

    if df_title_contains.empty:
        print('Empty!')
        return None

    print(f'Article from year {year}')
    print(df_title_contains.iloc[0][4])

    return df_title_contains.iloc[0][4]

# Main code
def main():
    df_quality = pd.read_csv('QualityChecklists.csv', sep=',', decimal='.')

    dic_scimagojr_dfs = {}
    dic_scimagojr_dfs['2021'] = pd.read_csv(
        'scimagojr 2021.csv', sep=';', decimal=',', quotechar="\"")
    dic_scimagojr_dfs['2020'] = pd.read_csv(
        'scimagojr 2020.csv', sep=';', decimal=',', quotechar="\"")
    dic_scimagojr_dfs['2019'] = pd.read_csv(
        'scimagojr 2019.csv', sep=';', decimal=',', quotechar="\"")
    dic_scimagojr_dfs['2018'] = pd.read_csv(
        'scimagojr 2018.csv', sep=';', decimal=',', quotechar="\"")
    dic_scimagojr_dfs['2017'] = pd.read_csv(
        'scimagojr 2017.csv', sep=';', decimal=',', quotechar="\"")
    dic_scimagojr_dfs['2016'] = pd.read_csv(
        'scimagojr 2016.csv', sep=';', decimal=',', quotechar="\"")
    dic_scimagojr_dfs['2015'] = pd.read_csv(
        'scimagojr 2015.csv', sep=';', decimal=',', quotechar="\"")
    dic_scimagojr_dfs['2014'] = pd.read_csv(
        'scimagojr 2014.csv', sep=';', decimal=',', quotechar="\"")
    dic_scimagojr_dfs['2013'] = pd.read_csv(
        'scimagojr 2013.csv', sep=';', decimal=',', quotechar="\"")
    dic_scimagojr_dfs['2012'] = pd.read_csv(
        'scimagojr 2012.csv', sep=';', decimal=',', quotechar="\"")
    dic_scimagojr_dfs['2011'] = pd.read_csv(
        'scimagojr 2011.csv', sep=';', decimal=',', quotechar="\"")

    df_quality['SSTOTAL'] = df_quality.apply(
        lambda row: row['SSTOTAL'] + random.uniform(-0.01, 0.01), axis=1)

    df_quality['SRTOTAL'] = df_quality.apply(
        lambda row: row['SRTOTAL'] + random.uniform(-0.01, 0.01), axis=1)

    df_quality['Quartile'] = df_quality.apply(
        lambda row: retrieve_quartile(row, dic_scimagojr_dfs), axis=1).replace('-', np.nan)

    print(df_quality['SSTOTAL'])

    means = df_quality.groupby(by=['Quartile'], dropna=False)[
        ['SSTOTAL', 'SRTOTAL']].mean()

    print(means)

    fig = px.scatter(df_quality.fillna('Not a Journal'), x="SSTOTAL", y="SRTOTAL",
                     range_x=[0, 1], range_y=[0, 1], color='Quartile')
    fig.write_image("scimagojr.pdf")

    
    dic_CORE_dfs = {}
    dic_CORE_dfs['2021'] = pd.read_csv(
        'CORE 2021.csv', sep=',', quotechar="\"", header=None)
    dic_CORE_dfs['2020'] = pd.read_csv(
        'CORE 2020.csv', sep=',', quotechar="\"", header=None)
    dic_CORE_dfs['2019'] = pd.read_csv(
        'CORE 2020.csv', sep=',', quotechar="\"", header=None)
    dic_CORE_dfs['2018'] = pd.read_csv(
        'CORE 2018.csv', sep=',', quotechar="\"", header=None)
    dic_CORE_dfs['2017'] = pd.read_csv(
        'CORE 2017.csv', sep=',', quotechar="\"", header=None)
    dic_CORE_dfs['2016'] = pd.read_csv(
        'CORE 2017.csv', sep=',', quotechar="\"", header=None)
    dic_CORE_dfs['2015'] = pd.read_csv(
        'CORE 2017.csv', sep=',', quotechar="\"", header=None)
    dic_CORE_dfs['2014'] = pd.read_csv(
        'CORE 2014.csv', sep=',', quotechar="\"", header=None)
    dic_CORE_dfs['2013'] = pd.read_csv(
        'CORE 2013.csv', sep=',', quotechar="\"", header=None)
    dic_CORE_dfs['2012'] = pd.read_csv(
        'CORE 2013.csv', sep=',', quotechar="\"", header=None)
    dic_CORE_dfs['2011'] = pd.read_csv(
        'CORE 2013.csv', sep=',', quotechar="\"", header=None)

    print(dic_CORE_dfs['2011'])


    df_quality['Conference'] = df_quality.apply(
        lambda row: retrieve_conference(row, dic_CORE_dfs), axis=1).replace('-', np.nan)

    print(df_quality['SSTOTAL'])

    means = df_quality.groupby(by=['Conference'], dropna=False)[
        ['SSTOTAL', 'SRTOTAL']].mean()

    print(means)

    fig = px.scatter(df_quality.fillna('Not a Conference'), x="SSTOTAL", y="SRTOTAL",
                     range_x=[0, 1], range_y=[0, 1], color='Conference')
    fig.write_image("CORE.pdf")

if __name__ == "__main__":
    main()
