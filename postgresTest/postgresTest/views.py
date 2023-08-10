from django.shortcuts import render
from postgresTest.models import photo
from django.contrib import messages
from django.http import HttpResponse
from postgresTest.forms import photoforms
from django.db import connection


def HomePage(request):
    showall=photo.objects.all()
    return render(request,'HomePage.html',{"data":showall})


def insertphoto(request):
    if request.method=="POST":
        if request.POST.get('photo_id') and request.POST.get('date') and request.POST.get('time') and request.POST.get('location') and request.POST.get('size') and request.POST.get('tag_color') and request.POST.get('user_id'):
            saverecord=photo()
            saverecord.photo_id=request.POST.get('photo_id') 
            saverecord.date=request.POST.get('date')
            saverecord.time=request.POST.get('time')
            saverecord.location=request.POST.get('location')
            saverecord.size=request.POST.get('size')
            saverecord.tag_color=request.POST.get('tag_color')
            saverecord.user_id=request.POST.get('user_id')

            allval=photo.objects.all()
            
            for i in allval:
                if int(i.photo_id)==int(request.POST.get('photo_id')):
                    messages.warning(request,'photo already exists....!');
                    return render(request,'insertphoto.html')

            saverecord.save()
            messages.success(request,'photo is saved succesfully!!')
            return render(request,'insertphoto.html')
    else:
            return render(request,'insertphoto.html')


def showphoto(request):
    showall=photo.objects.all()
    return render(request,'showphoto.html',{"data":showall})

def editphoto(request,id):
    editpic=photo.objects.get(photo_id=id)
    return render(request,'editphoto.html',{"photo":editpic})

def updatephoto(request,id):
    Updatephoto=photo.objects.get(photo_id=id)
    form=photoforms(request.POST,instance=Updatephoto)
    if form.is_valid():
        form.save()
        messages.success(request,'Photo updated successfully')
        return render(request,'editphoto.html',{"photo":Updatephoto})

def deletephoto(request,id):
    delphoto=photo.objects.get(photo_id=id)
    delphoto.delete()
    showdata=photo.objects.all()
    return render(request,'showphoto.html',{"data":showdata})   

def runascphoto(request):
    raw_query = "select * from photo_management.photo order by date ,time"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    return render(request,'sortasc.html',{'data':alldata})

def rundescphoto(request):
    raw_query = "select * from photo_management.photo order by date desc ,time desc "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    return render(request,'sortdesc.html',{'data':alldata})

def sortasc(request):
    raw_query = "select * from photo_management.photo order by date ,time"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    return render(request,'sortasc.html',{'data':alldata})

def sortdesc(request):
    raw_query = "select * from photo_management.photo order by date desc ,time desc "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    return render(request,'sortdesc.html',{'data':alldata})

def runquery(request):
    raw_query = "select * from photo_management.photo where photo.user_id=33574"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    return render(request,'runquery.html',{'data':alldata})

