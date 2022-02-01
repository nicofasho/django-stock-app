from django.shortcuts import render


def home(request):
    import requests
    import json

    # pk_c06698a456be48b3926f6f4d439a8141
    api_request = requests.get(
        'https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_c06698a456be48b3926f6f4d439a8141'
    )

    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = 'Error...'

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
