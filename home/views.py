from django.shortcuts import render

# Create your views here.


def home(request):
    name = request.GET['acc']
    region = request.GET['reg']

    return render(request, 'homepage.html', {
        'name': name,
        'region': region
    })
