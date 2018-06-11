from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def error_404(request):
        data = {}
        return render(request,'inventoryManagement/error_404.html', data)
 
def error_500(request):
        data = {}
        return render(request,'inventoryManagement/error_500.html', data)