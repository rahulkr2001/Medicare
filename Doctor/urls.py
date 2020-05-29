from . import views
from django.urls import path
s='hello'
urlpatterns=[
    path('',views.Home,name='home'),
    path('doctor/',views.DoctorDetail,name='doctor'),
    path('patient/',views.PatientDetail,name='patient'),
    path('doctor/<int:id>',views.DoctorPatientsData,name="doctorPatients"),
    path('addDoctor/',views.AddDoctor,name='addDoctor'),
    path('addPatient/',views.AddPatient,name='addPatient'),
]
