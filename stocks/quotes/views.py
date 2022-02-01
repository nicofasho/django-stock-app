from django.shortcuts import render


def home(request):
    import requests
    import json

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
    return render(request, 'add_stock.html', {})