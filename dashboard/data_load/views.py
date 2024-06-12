from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

from .models import Game, Genre, Platform, Publisher

def data_load(request):
    if request.method == 'GET':
        df = pd.read_csv('..\\video_games_sales.csv')
        df['year'] = pd.to_datetime(df['year'], format='%Y')
        df['publisher'] = df['publisher'].fillna('Desconhecido')

        # Substitua valores NaN na coluna 'year' por None
        df['year'] = df['year'].where(df['year'].notna(), None)

        for index, row in df.iterrows():
            genre, created = Genre.objects.get_or_create(genre=row['genre'])
            platform, created = Platform.objects.get_or_create(platform=row['platform'])
            publisher, created = Publisher.objects.get_or_create(publisher=row['publisher'])

            Game.objects.create(
                name=row['name'],
                platform=platform,
                year=row['year'].year if not pd.isnull(row['year']) else None,  # Use None para valores NaN
                genre=genre,
                publisher=publisher,
                na_sales=row['na_sales'],
                eu_sales=row['eu_sales'],
                jp_sales=row['jp_sales'],
                other_sales=row['other_sales'],
                global_sales=row['global_sales']
            )

        return HttpResponse('Dados carregados', status=200)

def data_delete(request):
    if request.method == 'GET':
        Game.objects.all().delete()
        Genre.objects.all().delete()
        Platform.objects.all().delete()
        Publisher.objects.all().delete()

        return HttpResponse('Registros apagados com sucesso', status=200)