from django.shortcuts import render


# Create your views here.
def index(reguest):
    return render(reguest, 'sign_in/sign_in.html')


def reg(reguest):
    return render(reguest, 'sign_in/reg.html')
