from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

import sys
sys.path.insert(0, 'tourists/resources')
from data import records



# context = records[0].update()

# print(context)
# # print(type(records[0]))
records[0]
print(records[0])
context = {}
for i,j in records[0].items():
    context[(i+'_num')] = j
    if 'area' in i:
        if j >= 80 :
            context[i] = '혼잡'
        elif 30<= j < 80:
            context[i] = '보통'
        else:
            context[i] = '여유'
    else:
        context[i]=j
print(context)

# Create your views here.
def index(request):
    today = datetime.now().strftime(" %Y 년 %m 월 %d 일 %I:%M:%S%p")
    context['today']= today
    print(context)
    return render(request, 'index.html', context=context) 

def button(request):
    context  = { }
    return render(request, 'buttons.html', context)

def cards(request):
    context  = { }
    return render(request, 'cards.html', context) 
