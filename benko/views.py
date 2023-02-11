from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "benko/index.html")

def play(request):
    return render(request, "benko/play.html", {
        "image": True,
    })

def discover(request):
    return render(request, "benko/discover.html", {
        "image": False,
    })

def game(request):
    return render(request, "benko/game.html", {
        "image": False,
    })