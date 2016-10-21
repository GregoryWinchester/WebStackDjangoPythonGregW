import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    
    python_pages = [
        {"title" : "Official Python Tutorial",
         "url" : "http://docs.python.org/2/tutorial/",
         "views" : 420},
        {"title" : "How to Think Like a Computer Scientist",
         "url" : "http://www.greenteapress.com/thinkpython/",
         "views" : 419},
        {"title" : "Learn Python in 10 Minutes",
         "url" : "http://www.korokithakis.net/tutorials/python/",
         "views" : 418}]
    
    django_pages = [
        {"title" : "Official Django Tutorial",
         "url" : "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views" : 417},
        {"title" : "Django Rocks",
         "url" : "http://www.djangorocks.com/",
         "views" : 416},
        {"title" : "How to Tango with Django",
         "url" : "http://www.tangowithdjango.com/",
         "views" : 415} ]
    
    other_pages = [
        {"title" : "Bottle",
         "url" : "http://bottlepy.org/docs/dev/",
         "views" : 414},
        {"title" : "Flask",
         "url" : "http://flask.pocoo.org",
         "views" : 413} ]
    
    go_pages = [
        {"title" : "Official Go Documentation",
         "url" : "https://golang.org/doc/",
         "views" : 412},
        {"title" : "Go Tutorial",
         "url" : "http://www.tutorialspoint.com/go/",
         "views" : 411} ]
    
    cats = {"Python": {"pages" : python_pages, "views" : 128, "likes" : 64},
            "Django" : {"pages" : django_pages, "views" : 63, "likes" : 32},
            "Go" : {"pages" : go_pages, "views" : 30, "likes" : 29},
            "Other Frameworks" : {"pages" : other_pages, "views" : 61, "likes" : 16} }
    
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])
            
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
            
def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url     
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c
    
# start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()