# Final Project - Analyzing Catalunya's Economy

## Introduction:
The idea behind this project is to understand the Catalan economy better. In order to do that, I have downloaded financial data from all Catalan companies with over 300k in Revenue in 2019 (pre-covid).
The goal is to understand how are these companies spread around the Catalan territory so we can find out which regions are more important to the overall economy, also showing which regions have potential to grow in the future.

## Data Extraction:
To extract the data I used Sabi, which is a database with all info about Spanish and Portuguese companies, public and private. Many financial information is available but there is a limit in the data that you can download so I chose: Activity, Zip Code, Revenue, EBITDA, Net Income, Assets and Equity. With this data we can bet more information like Liabilities (Assets - Equity).
![sabi](https://user-images.githubusercontent.com/114917673/205076452-dc9182d3-5f88-42d5-9ea0-44bd5666f176.JPG)


In order to get the region of the company I had to do more research. The issue is that there was no table online that connected the zip-code with the region. But I was able to find one that connected Zip-Code to Town-Code, an another that connected Town-Codes to Regions. Joining these two, I was able to join the resulting table to the original dataframe and get the region of the company.

## Visualization:
The majority of the visualization is on Tableau, except for the following graph that visualizes the distribution of the Revenue:

![Revenue](https://user-images.githubusercontent.com/114917673/205076754-940ddcb8-a1a1-433f-9bdd-e1390e79ebe8.JPG)
