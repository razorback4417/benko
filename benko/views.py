from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "benko/index.html")

def play(request):
    return render(request, "benko/play.html")