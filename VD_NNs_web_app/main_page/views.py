from django.shortcuts import render


def index(reguest):
    return render(reguest, 'main_page/index.html')
