import tempfile
from xmlrpc.client import Boolean

from django.shortcuts import render
from VoiceDisorders_App.models import CustomUser

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from VoiceDisorders_App.NeuralNetwork.nn import network_inference

# Create your views here.
def index(reguest):
    return render(reguest, 'main_page/index.html')


def sign_in_view(reguest):
    if reguest.method == "POST":
        data = reguest.POST
        allUser = CustomUser.objects.all()
        user = CustomUser(
            email=data.get('userEmail'),
            password=data.get('userPassword')
        )

        if (len(user.email) == 0 or len(user.password) == 0):
            messages.info(reguest, 'Set all fields!')
            return render(reguest, 'sign_in/sign_in.html')

        if (allUser.filter(email=user.email)):
            if (allUser.filter(password=user.password)):
                messages.info(reguest, 'Success!')
                return render(reguest, 'user_pa/user_pa.html')
            else:
                messages.info(reguest, 'Incorrect password!')
                return render(reguest, 'sign_in/sign_in.html')
        else:
            messages.info(reguest, 'User wasn\'t found')
            return render(reguest, 'sign_in/sign_in.html')

    return render(reguest, 'sign_in/sign_in.html')


def reg(reguest):
    if reguest.method == "POST":
        try:
            data = reguest.POST
            user = CustomUser(
                name=data.get('userName'),
                surname=data.get('userSurname'),
                dateOfBithday=data.get('userDateOfBithday'),
                sex=Boolean(data.get('userSex')),
                email=data.get('userEmail'),
                password=data.get('userPassword'),
                role=data.get('userRole')
            )

            if (len(user.dateOfBithday) == 0):
                messages.info(reguest, 'Set all fields!')
                return render(reguest, 'sign_in/reg.html')

            allUser = CustomUser.objects.all()

            if (allUser.get(email=user.email)):
                messages.info(reguest, 'Error!'
                                       'This email has been used!')
                return render(reguest, 'sign_in/reg.html')

        except ValueError:
            messages.info(reguest, 'ValueError!')
            return render(reguest, 'sign_in/reg.html')

        except ObjectDoesNotExist:
            messages.info(reguest, 'Any ObjectDoesNotExist'
                                   'User was created!')
            user.save()
            # return HttpResponse("DONE!")
            return render(reguest, 'sign_in/sign_in.html')
        # except MultipleObjectsReturned:

    else:
        return render(reguest, 'sign_in/reg.html')


def user_pa_view(reguest):
    if reguest.method == "POST":
        wavFile = reguest.FILES['wavFile']
        content = wavFile.read()
        with tempfile.NamedTemporaryFile(delete=False) as wavTemp:
            wavTemp.write(content)
            if network_inference(wavTemp.name):
                # return HttpResponse('BOLEN')
                messages.info(reguest, 'BOLEN')
                return render(reguest, 'user_pa/user_pa.html')
            else:
                # return HttpResponse('NE BOLEN')
                messages.info(reguest, 'NE BOLEN')
                return render(reguest, 'user_pa/user_pa.html')
    return render(reguest, 'user_pa/user_pa.html')


def profile_view(reguest):
    return render(reguest, 'user_pa/profile.html')
