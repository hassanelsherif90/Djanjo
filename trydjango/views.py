"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article
from django.template.loader import render_to_string




def home_view(request,*args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    print(args, kwargs)
    print(request)
    name = "Hassan"
    number_id = random.randint(1, 4)
    # print(args, kwargs)
    # data base from app articles 
    Article_obj = Article.objects.get(id= number_id)
    article_list = Article.objects.all()
    # print(article_list)
    context = {
        "object_list":article_list,
        "object":Article_obj,
        "title":Article_obj.title,
        "id" : Article_obj.id,
        "content": Article_obj.content,
    }
    # Template 
    HTML_STRING = render_to_string("home-view.html", context=context )
    # H1_STRING = f"""
    # <h1>Hello {Article_obj.title} (id :{Article_obj.id})!</h1>
    # """

    # P_STRING = f"""
    # <h1>Hello {Article_obj.content}!</h1>
    # """
    # print(1000 * 1000)
    # HTML_STRING = H1_STRING + P_STRING
    
    return HttpResponse(HTML_STRING)