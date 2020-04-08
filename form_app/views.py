from django.shortcuts import render, redirect
def index(request):
    return render(request, 'index.html')

def show(request):
    return render(request, 'show.html')

def users(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form
    }
    return redirect(request,"/show", context)

