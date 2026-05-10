from django.shortcuts import render
# from django.http import HttpResponse
import datetime

def index(request):
    # context = {
    #      name : "nitesh",
    #     age : 20
    # }
    date = datetime.datetime.now()
    msg= "Hello Guest !!!! "
    h= int(date.strftime("%H"))
    if h < 12:
        msg += "Good Morning"
    elif h < 16:
        msg += "Good Afternoon"
    elif h < 20:
        msg += "Good Evening"
    else:
        msg += "Good Night"
    context = {'insert_date': date, 'insert_msg': msg}
    return render(request, 'firstapp/html/index.html', context=context)
    






