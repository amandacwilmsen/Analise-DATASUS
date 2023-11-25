# Importe as bibliotecas necessárias, 
import pandas as pd
import re

def generateDfResidentPopulationAndIlliteracy(path):
    df = pd.read_csv(path, sep=';')
    df['id'] = df['Município'].str.extract('(\d+)')
    df['Município'] = df['Município'].apply(lambda x: re.sub('\d+', '', x).strip())
    return df

def generateDfAvaregeIncomePerCapita(path):
    df = pd.read_csv(path, sep=';', decimal=',')
    df['id'] = df['Município'].str.extract('(\d+)')
    df['Município'] = df['Município'].apply(lambda x: re.sub('\d+', '', x).strip())
    return df

def generateDfAvaregeIncomePerCapitaColor(path):
    df = pd.read_csv(path, sep=';', decimal=',')
    df['id'] = df['Município'].str.extract('(\d+)')
    df['Município'] = df['Município'].apply(lambda x: re.sub('\d+', '', x).strip())

    df['Branca'] = df['Branca'].astype(str).str.replace(',', '.')
    df['Preta'] = df['Preta'].astype(str).str.replace(',', '.')
    df['Amarela'] = df['Amarela'].astype(str).str.replace(',', '.')
    df['Parda'] = df['Parda'].astype(str).str.replace(',', '.')
    df['Sem declaração'] = df['Sem declaração'].astype(str).str.replace(',', '.')
    df['Indígena'] = df['Indígena'].astype(str).str.replace(',', '.')

    # "..." significa dado não disponivel
    df['Branca'] = df['Branca'].replace('...', -1)
    df['Preta'] = df['Preta'].replace('...', -1)
    df['Amarela'] = df['Amarela'].replace('...', -1)
    df['Parda'] = df['Parda'].replace('...', -1)
    df['Sem declaração'] = df['Sem declaração'].replace('...', -1)
    df['Indígena'] = df['Indígena'].replace('...', -1)

    # "-" significa que não possui nenhuma pessoa da raça/cor especifica 
    df['Branca'] = df['Branca'].replace('-', 0)
    df['Preta'] = df['Preta'].replace('-', 0)
    df['Amarela'] = df['Amarela'].replace('-', 0)
    df['Parda'] = df['Parda'].replace('-', 0)
    df['Sem declaração'] = df['Sem declaração'].replace('-', 0)
    df['Indígena'] = df['Indígena'].replace('-', 0)

    
    df = df.drop('Total', axis=1)
    return df




df_resident_population_1991 = generateDfResidentPopulationAndIlliteracy("./resident-population-above-15-years/resident-population-1991.csv")
df_resident_population_1991.to_csv('resident-population-1991-treated.csv', index=False, header=False)

df_resident_population_2000 = generateDfResidentPopulationAndIlliteracy("./resident-population-above-15-years/resident-population-2000.csv")
df_resident_population_2000.to_csv('resident-population-2000-treated.csv', index=False, header=False)

df_resident_population_2010 = generateDfResidentPopulationAndIlliteracy("./resident-population-above-15-years/resident-population-2010.csv")
df_resident_population_2010.to_csv('resident-population-2010-treated.csv', index=False, header=False)


df_illiteracy_population_1991 = generateDfResidentPopulationAndIlliteracy("./illiteracy-above-15-years/illiteracy-population-1991.csv")
print(df_illiteracy_population_1991)
df_illiteracy_population_1991.to_csv('illiteracy-population-1991.csv', index=False, header=False)

df_illiteracy_population_2000 = generateDfResidentPopulationAndIlliteracy("./illiteracy-above-15-years/illiteracy-population-2000.csv")
print(df_illiteracy_population_2000)
df_illiteracy_population_2000.to_csv('illiteracy-population-2000.csv', index=False, header=False)

df_illiteracy_population_2010 = generateDfResidentPopulationAndIlliteracy("./illiteracy-above-15-years/illiteracy-population-2010.csv")
print(df_illiteracy_population_2010)
df_illiteracy_population_2010.to_csv('illiteracy-population-2010.csv', index=False, header=False)


df_average_income_per_capita_1991 = generateDfAvaregeIncomePerCapita("./average-income-per-capita/average-income-per-capita-1991.csv")
print(df_average_income_per_capita_1991)
df_average_income_per_capita_1991.to_csv('average-income-per-capita-1991.csv', index=False, header=False)

df_average_income_per_capita_2000 = generateDfAvaregeIncomePerCapita("./average-income-per-capita/average-income-per-capita-2000.csv")
print(df_average_income_per_capita_2000)
df_average_income_per_capita_2000.to_csv('average-income-per-capita-2000.csv', index=False, header=False)

df_average_income_per_capita_2010 = generateDfAvaregeIncomePerCapita("./average-income-per-capita/average-income-per-capita-2010.csv")
print(df_average_income_per_capita_2010)
df_average_income_per_capita_2010.to_csv('average-income-per-capita-2010.csv', index=False, header=False)

df_average_income_per_capita_1991_color = generateDfAvaregeIncomePerCapitaColor("./average-income-per-capita/avarege-income-per-capita-by-color/average-income-per-capita-1991.csv")
print(df_average_income_per_capita_1991_color)
df_average_income_per_capita_1991_color.to_csv('average-income-per-capita-1991-color.csv', index=False, header=False)

df_average_income_per_capita_2000_color = generateDfAvaregeIncomePerCapitaColor("./average-income-per-capita/avarege-income-per-capita-by-color/average-income-per-capita-2000.csv")
print(df_average_income_per_capita_2000_color)
df_average_income_per_capita_2000_color.to_csv('average-income-per-capita-2000-color.csv', index=False, header=False)

df_average_income_per_capita_1991_color = generateDfAvaregeIncomePerCapitaColor("./average-income-per-capita/avarege-income-per-capita-by-color/average-income-per-capita-1991.csv")
print(df_average_income_per_capita_1991_color)
df_average_income_per_capita_1991_color.to_csv('average-income-per-capita-1991-color.csv', index=False, header=False)

df_average_income_per_capita_2010_color = generateDfAvaregeIncomePerCapitaColor("./average-income-per-capita/avarege-income-per-capita-by-color/average-income-per-capita-2010.csv")
print(df_average_income_per_capita_2010_color)
df_average_income_per_capita_2010_color.to_csv('average-income-per-capita-2010-color.csv', index=False, header=False)