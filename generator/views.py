from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(req):
    return render(req,'generator/home.html')

def about_me(req):
    return render(req,'generator/about_me.html')
    
def password(req):

    option=['lower']
    pass_length=int(req.GET.get('length'))
    upper=req.GET.get('upper')
    number=req.GET.get('number')
    special=req.GET.get('special')
    
    if upper=='on':
        option.append('upper')
    if number=='on':
        option.append('number')
    if special=='on':
        option.append('special')

    lower=list('abcdefghijklmnopqrstuvwxyz')
    upper=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special=list('@!#$%&')
    number=list('1234567890')

    
    password=''
    random.seed()
    while pass_length>0:
        
        choice=random.choice(option)
        
        if choice=='lower':
            lower_character=random.choice(lower)
            password+=lower_character
        elif choice=='upper':
            upper_character=random.choice(upper)
            password+=upper_character
        elif choice=='special':
            special_character=random.choice(special)
            password+=special_character
        else:
            numeric_character=random.choice(number)
            password+=numeric_character

        pass_length-=1

    


    return render(req,'generator/password.html',{'password':password})
