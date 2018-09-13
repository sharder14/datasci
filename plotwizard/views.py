from django.shortcuts import render
from django.http import HttpResponse
from .models import DataLine,Dataset
from django.views import generic
# Create your views here.

def index(request):

    data= DataLine.objects.all()
    data.dataset="Test Data"
    context = {"data":data}
    return render(request, "plotwizard/plot.html", context=context)



class DataLineListView(generic.ListView):
    model = DataLine
