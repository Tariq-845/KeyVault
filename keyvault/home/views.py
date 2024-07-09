from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# def index(request):
#     return HttpResponse("PLEASE WORK!!!!")

class Home(TemplateView):
    """
    Template view to display the home page
    (index.html)
    """

    template_name = "home/index.html"