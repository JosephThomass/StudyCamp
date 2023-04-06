from django.shortcuts import render


rooms=[
    {'id':1,'name':'Python'},
    {'id':2,'name':'Html'},
    {'id':3,'name':'Css'},
    {'id':4,'name':'JavaScript'}    
    ]

def home(request):
    context={'rooms':rooms}
    return render(request, 'home.html',context)

def rooms(request):
    return render(request, 'rooms.html')