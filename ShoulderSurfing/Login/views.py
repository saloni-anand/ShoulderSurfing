from django.shortcuts import render, redirect
import random
from .LogicFiles.loginUser import signin
from django.conf import settings
from django.core.mail import send_mail
current = ''
username = ''
phoneNo = ''
otp = 0


def dashboard(request):
    context = {}
    context['username'] = username

    if request.GET.get("logout"):
        return redirect("/login/")

    return render(request, "Login/dashboard.html", context)


def LoginUser(request):
    context = {}
    displayValue = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '#', '*']
    random.shuffle(displayValue)

    choiceList = [0, 1]
    choice = random.choice(choiceList)
    if (choice == 0):
        horver = "horizontal"
    else:
        horver = "vertical"

    subject = 'choice'
    message = f'Hi, thank you. your choice is {horver}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [phoneNo, ]
    send_mail( subject, message, email_from, recipient_list )

    context['displayvaluebuttonone'] = displayValue[0]
    context['displayvaluebuttontwo'] = displayValue[1]
    context['displayvaluebuttonthree'] = displayValue[2]
    context['displayvaluebuttonfour'] = displayValue[3]
    context['displayvaluebuttonfive'] = displayValue[4]
    context['displayvaluebuttonsix'] = displayValue[5]
    context['displayvaluebuttonseven'] = displayValue[6]
    context['displayvaluebuttoneight'] = displayValue[7]
    context['displayvaluebuttonnine'] = displayValue[8]
    context['displayvaluebuttonten'] = displayValue[9]
    context['displayvaluebuttoneleven'] = displayValue[10]
    context['displayvaluebuttontwelve'] = displayValue[11]
    context['displayvaluebuttonthirteen'] = displayValue[12]
    context['displayvaluebuttonfourteen'] = displayValue[13]
    context['displayvaluebuttonfifteen'] = displayValue[14]
    context['displayvaluebuttonsixteen'] = displayValue[15]

    if (choice == 0):
        context['pattern'] = 'Pattern Horizontal'
        context['buttononevalue'] = 'a'
        context['buttontwovalue'] = 'b'
        context['buttonthreevalue'] = 'c'
        context['buttonfourvalue'] = 'd'
        context['buttonfivevalue'] = 'e'
        context['buttonsixvalue'] = 'f'
        context['buttonsevenvalue'] = 'g'
        context['buttoneightvalue'] = 'h'
        context['buttonninevalue'] = 'i'
        context['buttontenvalue'] = 'j'
        context['buttonelevenvalue'] = 'k'
        context['buttontwelvevalue'] = 'l'
        context['buttonthirteenvalue'] = 'm'
        context['buttonfourteenvalue'] = 'n'
        context['buttonfifteenvalue'] = '#'
        context['buttonsixteenvalue'] = '*'

    elif(choice ==1):
        context['pattern'] = 'Pattern Vertical'
        context['buttononevalue'] = 'a'
        context['buttontwovalue'] = 'e'
        context['buttonthreevalue'] = 'i'
        context['buttonfourvalue'] = 'm'
        context['buttonfivevalue'] = 'b'
        context['buttonsixvalue'] = 'f'
        context['buttonsevenvalue'] = 'j'
        context['buttoneightvalue'] = 'n'
        context['buttonninevalue'] = 'c'
        context['buttontenvalue'] = 'g'
        context['buttonelevenvalue'] = 'k'
        context['buttontwelvevalue'] = '#'
        context['buttonthirteenvalue'] = 'd'
        context['buttonfourteenvalue'] = 'h'
        context['buttonfifteenvalue'] = 'l'
        context['buttonsixteenvalue'] = '*'

    logindata = request.POST or None
    if request.POST.get("pass"):
        global current
        current = current + logindata['pass']

    if request.POST.get("save"):
        print(logindata['username'])
        print(logindata['password'])
        global username
        username = logindata['username']
        permission = signin(logindata['username'], logindata['password'])
        if (permission):
            return redirect("/login/dashboard")
        else:
            print("Not valid initials");

    return render(request, "Login/Login.html", context)

def firstLayerAuthentication(request):

    firstLayerData = request.POST or None
    
    if request.POST.get("firstLayerSave"):
        answer = firstLayerData['answer']
        print(otp)
        print(answer)
        if(answer == str(otp)):
            print('yes')
            return redirect('/login/actualLogin')

    return render(request, "Login/firstLayer.html")

def phoneLayer(request):
    global otp 
    otp = random.randint(1111,9999)
    phoneLayerData = request.POST or None
    if request.POST.get("phoneLayerSave"):
        global phoneNo 
        phoneNo = phoneLayerData["phone"]
        subject = 'Project OTP'
        message = f'Hi, thank you. your otp is {otp}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [phoneNo, ]
        send_mail( subject, message, email_from, recipient_list )
        print(phoneNo)
        return redirect('/login/firstLogin')
    return render(request, "Login/phoneLayer.html")