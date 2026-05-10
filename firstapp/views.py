from django.shortcuts import render
# import datetime

# def index(request):
#     # context = {
#     #      name : "nitesh",
#     #     age : 20
#     # }
#     date = datetime.datetime.now()
#     msg= "Hello Guest !!!! "
#     h= int(date.strftime("%H"))
#     if h < 12:
#         msg += "Good Morning"
#     elif h < 16:
#         msg += "Good Afternoon"
#     elif h < 20:
#         msg += "Good Evening"
#     else:
#         msg += "Good Night"
#     context = {'insert_date': date, 'insert_msg': msg}
#     return render(request, 'firstapp/html/index.html', context=context)


def index(request):

    nitesh_details = {
        "name"         : "Nitesh Nepali",
        "Profession"   : "Cyber Security Engineer",
    }
    
    res='firstapp/index.html'
    return render(request, res,context=nitesh_details)



# def home(request):
#     res = "<h1>This is home page</h1>"
#     return HttpResponse(res)


def network(request):
    res='firstapp/network.html'
    return render(request, res)


def system(request):
    res='firstapp/system.html'
    return render(request, res)



def cloud(request):
    res='firstapp/cloud.html'
    return render(request, res)


def devops(request):
    res='firstapp/devops.html'
    return render(request, res)



def cybersecurity(request):
    res='firstapp/cybersecurity.html'
    return render(request, res)



    






