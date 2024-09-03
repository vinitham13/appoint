from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="home"),
    path('appoint/', views.appoint, name='appoint'),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("doctor/", views.doctor, name="doctor"),
    path("update/",views.update,name="update"),
    path("doctor/update",views.update,name="update"),
    path("doctor/appoint", views.appoint, name="doctor_appoint"),
    # path("doctor/index",views.add,name="index"),
    path("appointment/", views.appointment, name="appointment"),
    path("appointment/", views.index, name="appointment"),
    path("feature/", views.feature, name="feature"),
    path("team/", views.team, name="team"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("contact/", views.contact, name="contact"),
]
# from django.urls import path
# from . import views
#
#
# urlpatterns = [
#     path("",views.index,name="index"),
#     path("index",views.index,name="home"),
#     path("about",views.about,name="about"),
#     path("service",views.service,name="service"),
#     path("doctor",views.doctor,name="doctor"),
#     path("appointment",views.appointment,name="appointment"),
#     path("feature",views.feature,name="feature"),
#     path("team",views.team,name="team"),
#     path("appoint",views.appoint,name="appoint"),
#     path("testimonial",views.testimonial,name="testimonial"),
#     path("contact",views.contact,name="contact"),
# ]