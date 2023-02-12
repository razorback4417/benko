from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

userMetaMaskAddress = "0x00"
userAccountBalance = 0

#create your views here
def index(request):
    return render(request, 'chessFundy/index.html')

def game(request):
    return render(request, 'chessFundy/game.html')

def discover(request):
    return render(request, 'chessFundy/discover.html')

def connect(request):
    if request.method == "POST":
        global userMetaMaskAddress
        global userAccountBalance
        print("address: " + userMetaMaskAddress)

        if len(request.POST["userMetaMaskAddress"]) > 10:
            print("here inside if statement")
            userMetaMaskAddress = web3.toChecksumAddress(
                request.POST["userMetaMaskAddress"])
            # account balance
            # chain ID
            print("after", userMetaMaskAddress)


    # renders main.html with login information after MetaMask is connected in connectMetaMask.js
    return render(request, "chessFundy/discover.html", {
        "login": userMetaMaskAddress,
    })