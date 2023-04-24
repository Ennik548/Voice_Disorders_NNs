from django.shortcuts import render


def user_pa_view(reguest):
    return render(reguest, 'user_pa/user_pa.html')
