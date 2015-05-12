from django.shortcuts import render

def home(request):
    return render(request, 'toutatis/home.html', {
        'request': request
    })
