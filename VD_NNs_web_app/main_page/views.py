from django.shortcuts import render


# Create your views here.
def index(reguest):
    return render(reguest, 'main_page/index.html')


def about(reguest):
    return render(reguest, 'main_page/about.html')
