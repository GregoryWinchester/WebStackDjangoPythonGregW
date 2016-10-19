from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

# Create your views here.
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage' : "Bunnies and Dinos forever!",
                    'categories' : category_list}
    
    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'name' : 'Peaches K. Winchester',
                    'year' : '2016'
                    }
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    contect_dict = {}
    
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    return render(request, 'rango/category.html', context_dict)