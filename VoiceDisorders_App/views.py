from django.shortcuts import render

# Create your views here.
def index(reguest):
    return render(reguest, 'main_page/index.html')

def sign_in_view(reguest):
    return render(reguest, 'sign_in/sign_in.html')

def reg(reguest):
    return render(reguest, 'sign_in/reg.html')

def user_pa_view(reguest):
    return render(reguest, 'user_pa/user_pa.html')
