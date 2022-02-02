import requests
import json

import urllib.parse

from django.shortcuts import redirect, render
from .models import Stock
from .forms import StockForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(
            f'https://cloud.iexapis.com/stable/stock/{ticker}/quote?token=pk_c06698a456be48b3926f6f4d439a8141'
        )

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...'

        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

    # pk_c06698a456be48b3926f6f4d439a8141


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added"))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        output = []

        for item in ticker:
            api_request = requests.get(f'https://cloud.iexapis.com/stable/stock/{item.ticker}/quote?token=pk_c06698a456be48b3926f6f4d439a8141')

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = 'Error...'

        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Deleted!"))
    return redirect(delete_stock)

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})