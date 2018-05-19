from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime



# Create your views here.


def index(request):
    context = {
        "time": strftime('%Y-%m-%d %H:%M %p', gmtime())
    }
    return render(request, 'index.html', context)


# def index(request):
#     response = "Hello, I am your first request!"
#     return HttpResponse(response)

#
# def new(request):
#     return render(request, 'new.html')
#
