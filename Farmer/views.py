from django.shortcuts import render


def index(request):
    return render(request, 'Farmer/index.html')


def login(request):
    return render(request, 'Farmer/login.html')


def CreateFarmer(request):
    return render(request, 'Farmer/CreateFarmer.html')


def EditFarmer(request):
    return render(request, 'Farmer/EditFarmer.html')


def DeleteFarmer(request):
    return render(request, 'Farmer/DeleteFarmerForm.html')