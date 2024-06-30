from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, OuterRef, Subquery, Count

from data_load.models import Game, Genre, Publisher, Platform

def home(request):
    if request.method == 'GET':
        top_global_sales = Game.objects.values('name').annotate(total_global_sales=Sum('global_sales')).order_by('-total_global_sales')[:5]
        top_jp_sales = Game.objects.values('name').annotate(total_jp_sales=Sum('jp_sales')).order_by('-total_jp_sales')[:5]
        top_na_sales = Game.objects.values('name').annotate(total_na_sales=Sum('na_sales')).order_by('-total_na_sales')[:5]
        top_eu_sales = Game.objects.values('name').annotate(total_eu_sales=Sum('eu_sales')).order_by('-total_eu_sales')[:5]

        genre_totals = (
            Genre.objects.annotate(
                total_sales=Sum('game__global_sales')
            ).order_by('-total_sales')
        )

        publisher_totals = (
            Publisher.objects.annotate(
                total_sales=Sum('game__global_sales'),
                publisher_game_count=Count('game')
            ).order_by('-total_sales')
        )

        platform_totals = (
            Platform.objects.annotate(
                total_sales=Sum('game__global_sales')
            ).order_by('-total_sales')
        )

        chart_data_global_sales = [['Game', 'Top global sales']]
        for game in top_global_sales:
            chart_data_global_sales.append([game['name'], game['total_global_sales']])

        chart_data_jp_sales = [['Game', 'Top jp sales']]
        for game in top_jp_sales:
            chart_data_jp_sales.append([game['name'], game['total_jp_sales']])
        
        chart_data_na_sales = [['Game', 'Top na sales']]
        for game in top_na_sales:
            chart_data_na_sales.append([game['name'], game['total_na_sales']])

        chart_data_eu_sales = [['Game', 'Top eu sales']]
        for game in top_eu_sales:
            chart_data_eu_sales.append([game['name'], game['total_eu_sales']])

        
        context = {
            'top_global_sales': chart_data_global_sales,
            'top_jp_sales': chart_data_jp_sales,
            'top_na_sales': chart_data_na_sales,
            'top_eu_sales': chart_data_eu_sales,
            'genre_totals': genre_totals,
            'publisher_totals': publisher_totals,
            'platform_totals': platform_totals
        }

        return render(request, 'home.html', context)


def test(request):
    if request.method == 'GET':
        games = Game.objects.all()[:1000]

        context = {
            'games': games
        }

        return render(request, 'test.html', context)