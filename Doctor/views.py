from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Doctor,Patient
from .forms import DoctorForm,PatientForm
def Home(request):
    return render(request,'DoctorPatient/Home.html')

def DoctorDetail(request):
    dd=Doctor.objects.all()
    return render(request,'DoctorPatient/Doctor.html',{'DD':dd})

def PatientDetail(request):
    pd=Patient.objects.all()
    return render(request,'DoctorPatient/Patient.html',{'PD':pd})

def AddDoctor(request):
    form=DoctorForm()
    if request.method=='POST':
        form=DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            Doctor.objects.create(name=form.cleaned_data['name'],
            specialization=form.cleaned_data['specialization'],
            location=form.cleaned_data['location'],
            phone=form.cleaned_data['phone'],
            mail=form.cleaned_data['mail'])
        return redirect('doctor')
    return render(request,"DoctorPatient/AddDoctor.html",{'form':form})

def AddPatient(request):
    form=PatientForm()
    if request.method=='POST':
        form=PatientForm(request.POST,request.FILES)
        if form.is_valid():
            Patient.objects.create(name=form.cleaned_data['name'],
            doctor=form.cleaned_data['doctor'],
            gander=form.cleaned_data['gander'],
            age=form.cleaned_data['age'],
            phone=form.cleaned_data['phone'],
            mail=form.cleaned_data['mail'])
        return redirect('patient')
    return render(request,"DoctorPatient/AddPatient.html",{'form':form})

def DoctorPatientsData(request,id):
    doctorList=Doctor.objects.get(id=id)
    patientList=Patient.objects.filter(doctor=doctorList)
    return render(request,'DoctorPatient/DoctorPatientsList.html',{'DrList':doctorList,'PList':patientList})
