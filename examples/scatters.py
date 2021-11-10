# -*- coding:utf-8 -*-
import sys 
import pandas as pd
sys.path.append("..")
import xlsxviewer


df = pd.read_excel('./buildings.xlsx', engine='openpyxl')
xlsxviewer.genDataFrameScattersWithColumn(df, 'Name', ['HP'], ['level'], ['Hitpoints'], './buildings.html', 'lines', False)

df = pd.read_excel('./characters.xlsx', engine='openpyxl')
xlsxviewer.genDataFrameScattersWithColumn(df, 'Name', ['HP', 'DPS'], ['level', 'level'], ['Hitpoints', 'DPS'], './characters.html', 'lines', False)
