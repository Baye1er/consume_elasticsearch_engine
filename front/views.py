from django.shortcuts import render, redirect
import requests


# Create your views here.

def home(request):
    return render(request, 'home.html')


def not_found(request):
    search = request.GET.get("search")
    context = {
        'search': search
    }
    return render(request, 'error.html', context)


def index(request, *args, **kwargs):
    search = request.GET.get("search")
    print(search)
    url = 'http://127.0.0.1:8000/engine/'
    #url = 'http://127.0.0.1:9200/elastic_item/_search?size=176&pretty=true&q=*:*'
    response = requests.get(url)
    data = response.json()
    try:
        items = [item for item in data if (search in item['content'] or search in item['title'])]
        if items:
            return render(request, 'index.html', {'items': items, 'search': search})
        else:
            return redirect('not_found/')
    except TypeError:
        print('Void')
        return redirect('not_found/')
