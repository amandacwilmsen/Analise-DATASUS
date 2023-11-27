   # Importe as bibliotecas necessárias, 
import pandas as pd
import re

def generateDfIlliteracyAboveFifteen(path):
    # Read the CSV file with the correct delimiter
    df = pd.read_csv(path, sep=',')

    # Extract ID and clean 'Município' column
    df['id'] = df['Município'].str.extract('(\d+)')
    df['Município'] = df['Município'].apply(lambda x: re.sub('\d+', '', x).strip())
    column_order = ['id', 'Município', 'População não alfabetizada', 'Ano']
    df = df[column_order]

    return df


def generateDfPopulationAboveFifteen(path):
    # Read the CSV file with the correct delimiter
    df = pd.read_csv(path, sep=',')

    # Extract ID and clean 'Município' column
    df['id'] = df['Município'].str.extract('(\d+)')
    df['Município'] = df['Município'].apply(lambda x: re.sub('\d+', '', x).strip())
    column_order = ['id', 'Município', 'População de 15 anos ou mais', 'Ano']
    df = df[column_order]

    return df

def generateDfAverageIncomePerCapita(path):
    # Read the CSV file
    df = pd.read_csv(path, sep=',', decimal=',')
    
    # Extract ID and clean 'Município' column
    df['id'] = df['Município'].str.extract('(\d+)')
    df['Município'] = df['Município'].apply(lambda x: re.sub('\d+', '', x).strip())

    # Reorder columns to have 'id' before 'Município'
    column_order = ['id', 'Município', 'Renda média domic. per capita', 'Ano']
    df = df[column_order]
    return df

def generateDfAverageIncomePerCapitaColor(path):
    # Read the CSV file
    df = pd.read_csv(path, sep=',', decimal=',')
    
    # Extract ID and clean 'Município' column
    df['id'] = df['Município'].str.extract('(\d+)')
    df['Município'] = df['Município'].apply(lambda x: re.sub('\d+', '', x).strip())

    # Replace commas with dots and handle special symbols
    for column in ['Branca', 'Preta', 'Amarela', 'Parda', 'Sem declaração', 'Indígena', 'Total', 'Ano']:
        df[column] = df[column].astype(str).str.replace(',', '.')
        df[column] = df[column].replace('...', -1)
        df[column] = df[column].replace('-', 0)
        df[column] = df[column].astype(float)

    # Drop the 'Total' column
    df = df.drop('Total', axis=1)

    # Reorder columns to have 'id' before 'Município'
    column_order = ['id', 'Município'] + [col for col in df.columns if col not in ['id', 'Município']]
    df = df[column_order]

    return df


df_resident_population = generateDfPopulationAboveFifteen("./resident-population-above-15.csv")
df_resident_population.to_csv('resident-population-treated.csv', index=False, header=True)


df_illiteracy_population = generateDfIlliteracyAboveFifteen("./illiteracy-above-15.csv")
df_illiteracy_population.to_csv('illiteracy-population-treated.csv', index=False, header=True)

df_average_income_per_capita = generateDfAverageIncomePerCapita("./average-income-per-capita.csv")
df_average_income_per_capita.to_csv('average-income-per-capita-treated.csv', index=False, header=True)


df_average_income_per_capita_color = generateDfAverageIncomePerCapitaColor("./color-average-income-per-capita.csv")
df_average_income_per_capita_color.to_csv('color-average-income-per-capita-treated.csv', index=False, header=True)