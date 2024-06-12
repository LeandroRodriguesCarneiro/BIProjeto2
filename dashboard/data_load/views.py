from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

def data_load(request):
    if request.method == 'GET':
        df = pd.read_csv('..\\video_games_sales.csv')
        df['year'] = pd.to_datetime(df['year'], format='%Y')
        df['publisher'] = df['publisher'].fillna('Desconhecido')
        df.info()

        
        return HttpResponse('Dados carregados', status=200)
