from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone




def home(request):
    date = timezone.now()

    msg = "Hello Guest !! "
    h = int(date.strftime("%H"))

    if h < 12:
        msg+= "Good Morning"

    elif h<16:
        msg+= "Good Afternoon"

    elif h < 20:
        msg+= "Good Evening"
    
    else: 
        msg = "Hello Guest, Good Night."

    context = {
        'insert_date':date,
        'insert_msg':msg,
    }
    
    return  render(request,"core/html/index.html",context=context)




