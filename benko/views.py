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

def connect(request):
    if request.method == "POST":
        #print("Here in POST connect()")
        global userMetaMaskAddress
        global userAccountBalance
        global chainID
        print("address: " + userMetaMaskAddress)

        if len(request.POST["userMetaMaskAddress"]) > 10:
            print("here inside if statement")
            userMetaMaskAddress = web3.toChecksumAddress(
                request.POST["userMetaMaskAddress"])
            # account balance
            # chain ID
            print("after", userMetaMaskAddress)

        organizations = Organization.objects.filter(
            active='Y').order_by('organizationName')

    # renders html with login information after MetaMask is connected with js
    return render(request, "benko/index.html", {
        "login": userMetaMaskAddress,
    })