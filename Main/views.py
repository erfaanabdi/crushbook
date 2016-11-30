# encoding=utf8
from django.shortcuts import render,redirect
from django import forms
from Main import models
from django.core.mail import send_mail
from uuid import uuid4
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.

class newCrush(forms.Form):
    first=forms.EmailField(required=True)
    second=forms.EmailField(required=True)

def sent(request):
    context={}
    context['message']='Your email needs to be verified. A verification email has been sent to your address.'
    return render(request,'sent.html',context)

def sendtoall():
    #arr=["sahar_gh20002000@yahoo.com","farzaneh.karami91@gmail.com","arash.tashakori@yahoo.com","aidin.francoferra@gmail.com","babak7091@gmail.com","movahhed.sadeghi@hotmail.com","kammirzazad@gmail.com","amirreza.asadi@gmail.com","amir.majlesy@gmail.com","m.baghmirani@gmail.com","hashemianzahra4@gmail.com","sadeghabadi116@yahoo.com","sadeghabadi108@yahoo.com","samane.hamedi22@yahoo.com","princess_ch7@yahoo.com","ivet.soleymani@gmail.com","kian.pari1991@yahoo.com","orodkaveh@yahoo.com","Arya.Aslani@gmail.com","ali_bohlooli@yahoo.com"]
    arr=["erf@gm.com","fff@gm.com"]
    for i in range(len(arr)):
        mytp=(arr[i],)
        send_mail('شیدا','''
سلام

شخصی ایمیل شما را در سایت crush.ir وارد کرده است.

موفق باشید.
            ''','crush.ir.info@gmail.com',mytp)


def verify(request):
    vc=request.GET.get('vc','')
    res=models.pendingcrush.objects.filter(verification=vc)
    context={}
    if len(res)==0:
        context['message']='Invalid Link!'
        return  render(request,'sent.html',context)
    else:
        item=models.crush()
        item.first=res[0].first
        item.second=res[0].second
        reverse=models.crush.objects.filter(Q(first=res[0].second),Q(second=res[0].first))
        if(len(reverse)==0):
            context['message']='A notification email has been sent to your crush. It does not contain your email address and is merely a notification that SOMEONE has entered his/her email address in Crushbook.net'
            mytp=(res[0].second,)
            send_mail('Crushbook.net','Hi ' + res[0].second + ''',

Someone has got a crush on you and has entered your email in Crushbook.net.

All the best,
Crushbook, Inc.

            ''','no-reply@crushbook.net',mytp)
            item.save()
        else:
            context['message']='Congratulations, you have found your match! This means that your crush has already submitted your email address as his/her crush. You guys will receive a notification email shortly'
            mytp=(reverse[0].first,reverse[0].second)
            send_mail('Congratulations', 'Hi ' + reverse[0].first + ' and ' + reverse[0].second + ''',

Congratulations! Crushbook has found that both of you have crush on each other. 
Have a nice time together!

All the best,
Crushbook, Inc.

            ''','no-reply@crushbook.net',mytp)

            reverse[0].delete()

        res[0].delete()
        return render(request,'sent.html',context)

def index(request):
    #sendtoall()
    #print("salam")
    #send_mail('Subject here', 'Hi Erfan This please tell me about your weekend.', 'root@crushbook.net',
    #['web-nnUtrD@mail-tester.com'], fail_silently=False)

    if(request.method=='POST'):
        form=newCrush(request.POST)
        if form.is_valid():
            item=models.pendingcrush()
            item.first=form.cleaned_data['first']
            item.second=form.cleaned_data['second']
            item.verification=uuid4().hex
            item.save()
            mytp=(form.cleaned_data['first'],)
            body='Hi ' + form.cleaned_data['first'] + ''',

Someone recently entered your email address in Crushbook.net. If this was you, please verify your address by clicking the address below. Otherwise discard this message and nothing will happen.

http://crushbook.net/verify/?vc=''' + item.verification + '''

All the best,
Crushbook, Inc.
'''
            send_mail('Crushbook.net',body,'no-reply@crushbook.net',mytp)
            return redirect('/sent')
    else:
        form=newCrush()
    context={}
    context['form']=form
    return render(request,'index.html',context)
