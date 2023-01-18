import pandas as pd
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


df = pd.read_csv('data-398-2018-08-30.csv')
CONTENT = [i for i in df[['Name', 'Street', 'District']].values]


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
