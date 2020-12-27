from django.shortcuts import render
import requests

from github import GitHub
# Create your views here.

def home(request):
    return render(request, 'index.html')

def github(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Remaining'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    return render(request, 'getApi/github.html', {'search_result': search_result})
