# 📊 DATASUS Data Analysis – Income vs. Illiteracy

This repository contains an exploratory analysis of Brazilian census data aiming to investigate the potential relationship between income inequality and illiteracy rates, using information from DATASUS for the years 1991, 2000, and 2010. This project was developed as the final assignment for the Data Collection, Preparation, and Analysis course, which is part of the Data Science certification at PUCRS.

## 🧩 Hypothesis
Is there a relationship between income inequality and illiteracy rates?
This question guided our research. We explored demographic data segmented by municipality and race, allowing a deeper analysis of the evolution of these indicators over time.

## 🗂 Data Sources
The data was manually extracted from the Demographic and Socioeconomic System on DATASUS, since it was not available via PySUS:
Education – Census 1991, 2000, and 2010
Labor and Income – Census 1991, 2000, and 2010

## 🔧 Data Processing

The data was converted into CSV files and processed using Pandas.
We performed data cleaning, handled missing values, and standardized types.
The “race/color” column included undefined or missing values, which were treated as follows:
-1 for undefined
0 for no information

## 📈 Results
The analysis, conducted in Tableau, revealed that:
Illiteracy rates significantly decreased over the analyzed years.
Per capita income followed a linear growth pattern.
Conclusion: no direct relationship was identified between income and illiteracy rates.

## 👩🏼‍💻👨🏻‍💻 Developers
- Amanda Wilmsen amandac.wilmsen@gmail.com
- Lázaro Maciel 
