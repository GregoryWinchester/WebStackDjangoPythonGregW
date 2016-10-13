from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage' : "Bunnies and Dinos forever!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'name' : 'Peaches K. Winchester',
                    'year' : '2016'
                    }
    return render(request, 'rango/about.html', context=context_dict)