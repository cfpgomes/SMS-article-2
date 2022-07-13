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


def retrieve_quartile(row, df_quartiles):
    title = row['Publication Title']
    sourceID = row['SourceID']
    print(f'Title: {title}\nSourceID: {sourceID}')

    df_title_contains = df_quartiles[df_quartiles['Sourceid'] == sourceID]

    if df_title_contains.empty:
        print('Empty!')
        return None

    print(df_title_contains.iloc[0]['SJR Best Quartile'])

    return df_title_contains.iloc[0]['SJR Best Quartile']

# Main code


def main():
    df_quality = pd.read_csv('QualityChecklists.csv', sep=';', decimal=',')

    df_scimagojr = pd.read_csv('scimagojr 2021.csv', sep=';', decimal=',')

    df_quality['SSTOTAL'] = df_quality.apply(
        lambda row: row['SSTOTAL'] + random.uniform(-0.01, 0.01), axis=1)

    df_quality['SRTOTAL'] = df_quality.apply(
        lambda row: row['SRTOTAL'] + random.uniform(-0.01, 0.01), axis=1)

    df_quality['Quartile'] = df_quality.apply(
        lambda row: retrieve_quartile(row, df_scimagojr), axis=1).replace('-', np.nan)

    print(df_quality['SSTOTAL'])

    means = df_quality.groupby(by=['Quartile'], dropna=False)[['SSTOTAL','SRTOTAL']].mean()

    print(means)

    # fig = px.scatter(df_quality.fillna('Not a Journal'), x="SSTOTAL", y="SRTOTAL",
    #                  range_x=[0, 1], range_y=[0, 1], color='Quartile')
    # fig.show()


if __name__ == "__main__":
    main()
