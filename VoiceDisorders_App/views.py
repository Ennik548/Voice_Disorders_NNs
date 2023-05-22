from xmlrpc.client import Boolean

from django.shortcuts import render
from VoiceDisorders_App.models import CustomUser

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# Create your views here.
def index(reguest):
    return render(reguest, 'main_page/index.html')

def sign_in_view(reguest):
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

            if(len(user.dateOfBithday) == 0):
                messages.info(reguest, 'Set all fields!')
                return render(reguest, 'sign_in/reg.html')

            allUser = CustomUser.objects.all()

            if(allUser.get(email=user.email)):
                messages.info(reguest, 'Error!'
                                       'This email has been used!')
                return render(reguest, 'sign_in/reg.html')

        except ValueError:
            messages.info(reguest, 'ValueError!')
            return render(reguest, 'sign_in/reg.html')

        except ObjectDoesNotExist:
            messages.info(reguest, 'ObjectDoesNotExist')
            user.save()
            return HttpResponse("DONE!")

        # except MultipleObjectsReturned:
        
    else:
        return render(reguest, 'sign_in/reg.html')

def user_pa_view(reguest):
    return render(reguest, 'user_pa/user_pa.html')

# def handlerDateBaseTest(request):
    # user = CustomUser()
    # user.name = 'George'