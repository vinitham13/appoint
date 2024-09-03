
from django.shortcuts import render
from .models import users

# Existing views
# def index(request):
#     return render(request, 'index.html')
#
#
# def about(request):
#     return render(request, 'about.html')
#
#
# def service(request):
#     return render(request, 'service.html')
#
#
# def doctor(request):
#     return render(request, 'doctor.html')
#
#
# def appointment(request):
#     return render(request, 'appointment.html')
#
#
# def feature(request):
#     return render(request, 'feature.html')
#
#
# def team(request):
#     return render(request, 'team.html')
#
# def appo(request):
#     return render(request, 'appoint.html')
#
#
#
# def testimonial(request):
#     return render(request, 'testimonial.html')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def doctor(request):
    return render(request,'doctor.html')
def appointment(request):
    return render(request,'appointment.html')

def feature(request):
    return render(request,'feature.html')
def team(request):
    return render(request,'team.html')
def showcase(request):
    return render(request,'showcase.html')
def testimonial(request):
    return render(request,'testimonial.html')
def contact(request):
    return render(request,'contact.html')
# def index(request):
#     return render(request,'index.html')
# def about(request):
#     return render(request,'about.html')
# def service(request):
#     return render(request,'service.html')
# def doctor(request):
#     return render(request,'doctor.html')
# def appointment(request):
#     return render(request,'appointment.html')
# def feature(request):
#     return render(request,'feature.html')
# def team(request):
#     return render(request,'team.html')
# def showcase(request):
#     return render(request,'showcase.html')
# def testimonial(request):
#     return render(request,'testimonial.html')
# def contact(request):
#     return render(request,'contact.html')
#
# def contact(request):
#     return render(request, 'contact.html')
def appoint(request):
    if request.method == "POST":
        # Extract data from POST request
        fname = request.POST.get('fname', '')
        email = request.POST.get('email', '')
        mobi = request.POST.get('mobi', '')
        doct = request.POST.get('doct', '')
        choosedate = request.POST.get('choosedate', '')
        choosetime = request.POST.get('choosetime', '')
        textar = request.POST.get('textar', '')

        # Prepare data to be inserted
        data = {
            "fname": fname,
            "email": email,
            "mobi": mobi,
            "doct": doct,
            "choosedate": choosedate,
            "choosetime": choosetime,
            "textar": textar
        }

        # Insert data into MongoDB
        users.insert_one(data)

        # Optional: Retrieve all documents to display on `appoint.html`
        all_data = users.find()

        return render(request, 'index.html', {'data': all_data})

    else:
        # Optional: Retrieve all documents if the request is not POST
        all_data = users.find()

        return render(request, 'appoint.html', {'data': all_data})
def update(request):
    if "delete" in request.GET:
        users.delete_one({'mobi':request.GET['mobi']})
        return render(request,'appoint.html')