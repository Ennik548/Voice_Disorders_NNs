import logging
import tempfile
from xmlrpc.client import Boolean
from django.utils import timezone
from django.shortcuts import render
from VoiceDisorders_App.models import CustomUser

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from VoiceDisorders_App.NeuralNetwork.nn import network_inference

from django.contrib import sessions
# Create your views here.
def index(reguest):
    return render(reguest, 'main_page/index.html')


def sign_in_view(reguest):
    if reguest.method == "POST":
        data = reguest.POST
        allUser = CustomUser.objects.all()
        temp_user = CustomUser(
            email=data.get('userEmail'),
            password=data.get('userPassword')
        )

        if (len(temp_user.email) == 0 or len(temp_user.password) == 0):
            messages.info(reguest, 'Set all fields!')
            return render(reguest, 'sign_in/sign_in.html')

        if (allUser.filter(email=temp_user.email)):
            if (allUser.filter(password=temp_user.password)):
                sign_user = CustomUser.objects.get(email=temp_user.email)
                reguest.session['id'] = sign_user.id
                if (sign_user.is_active == False):
                    sign_user.is_active = True
                    sign_user.save()
                    return render(reguest, 'user_pa/user_pa.html',
                                  {'lastDate': 'Данных нет', 'lastResult': ''})
                elif(sign_user.last_result == True):
                    return render(reguest, 'user_pa/user_pa.html',
                                  {'lastDate': sign_user.last_result_date, 'lastResult': 'БОЛЕН'})
                else:
                    return render(reguest, 'user_pa/user_pa.html',
                                  {'lastDate': sign_user.last_result_date, 'lastResult': 'ЗДОРОВ'})
            else:
                messages.info(reguest, 'Incorrect password!')
                return render(reguest, 'sign_in/sign_in.html')
        else:
            messages.info(reguest, 'User wasn\'t found')
            return render(reguest, 'sign_in/sign_in.html')

    else:
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
            return render(reguest, 'sign_in/sign_in.html')
        # except MultipleObjectsReturned:

    else:
        return render(reguest, 'sign_in/reg.html')

def user_pa_view(reguest):
    user_id = reguest.session['id']
    sign_user = CustomUser.objects.get(id=user_id)

    if reguest.method == "POST":
        if reguest.FILES.get('wavFile') == None:
            messages.info(reguest, 'Загрузите данные!!!')
            return render(reguest, 'user_pa/user_pa.html', )

        wavFile = reguest.FILES['wavFile']
        content = wavFile.read()

        with tempfile.NamedTemporaryFile(delete=False) as wavTemp:
            wavTemp.write(content)
            if network_inference(wavTemp.name):
                sign_user.last_result = True
                sign_user.last_result_date = timezone.now()
                sign_user.save()
                # messages.info(reguest, 'Человек болен!')
                return render(reguest, 'user_pa/user_pa.html', {'lastDate': sign_user.last_result_date, 'lastResult': 'БОЛЕН'})
            else:
                sign_user.last_result = False
                sign_user.last_result_date = timezone.now()
                sign_user.save()
                # messages.info(reguest, 'Человек здоров!')
                return render(reguest, 'user_pa/user_pa.html', {'lastDate': sign_user.last_result_date, 'lastResult': 'ЗДОРОВ'})
    else:
        if(sign_user.last_result == True):
            return render(reguest, 'user_pa/user_pa.html', {'lastDate': sign_user.last_result_date, 'lastResult': 'БОЛЕН'})
        else:
            return render(reguest, 'user_pa/user_pa.html', {'lastDate': sign_user.last_result_date, 'lastResult': 'ЗДОРОВ'})

def profile_view(reguest):
    return render(reguest, 'user_pa/profile.html')
