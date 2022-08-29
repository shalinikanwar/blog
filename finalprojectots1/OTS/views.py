from django.shortcuts import render

from OTS.models import Question,User

from django.http import HttpResponse,HttpResponseRedirect
import random

def newblog(request):
   try:
    realname=request.session['realname']   
    res=render(request,'OTS/new_blog.html')
    return res
   except KeyError:
     return HttpResponseRedirect("http://localhost:8000/OTS/login/")  


def saveblog(request):

    question=Question()

    question.que=request.POST['question']

    question.optiona=request.POST['optiona']

    question.optionb=request.POST['optionb']

    question.optionc=request.POST['optionc']

    question.optiond=request.POST['optiond']

    question.answer=request.POST['answer']

    question.save()

    return HttpResponseRedirect('http://localhost:8000/OTS/view-blog/')#predefine function save in model class

    #question is name="question" in html file

def viewblog(request):
  try:
    realname=request.session['realname']

    questions=Question.objects.all()

    #table ke record yaha aa jayege all()se

    res=render(request,'OTS/view_blog.html',{'questions':questions})
    return res
  except KeyError:
      return HttpResponseRedirect("http://localhost:8000/OTS/login/")

def editblog(request):
 
    q=request.GET['qno']
    question=Question.objects.get(qno=int(q))#qno is primary key table q is variable name

    res=render(request,'OTS/edit_blog.html',{'question':question})
    return res
  
  

def editsaveblog(request):
 
    question=Question()

    question.qno=request.POST['qno']

    question.que=request.POST['question']

    question.optiona=request.POST['optiona']

    question.optionb=request.POST['optionb']

    question.optionc=request.POST['optionc']

    question.optiond=request.POST['optiond']

    question.answer=request.POST['answer']

    question.save()

    return HttpResponseRedirect('http://localhost:8000/OTS/view-blog/')
 

def deleteblog(request):
    try:
       realname=request.session['realname']
       q=request.GET['qno']
       question=Question.objects.filter(qno=int(q))
       question.delete()

       return HttpResponseRedirect('http://localhost:8000/OTS/view-blog/')

    except KeyError:

        return HttpResponseRedirect("http://localhost:8000/OTS/login/")


     

def signup(request):

    d1={}

    try:
    

      if request.GET['error']==str(1):

        d1['errmsg']='Username already taken'

    except:

        d1['errmsg']=''


    res=render(request,'OTS/signup.html',d1)
    return res

def saveUser(request):

    user=User()

    u=User.objects.filter(username=request.POST['username'])

    if not u:

        user.username=request.POST['username']

        user.password=request.POST['password']

        user.realname=request.POST['realname']

        user.role="LEARNER"

        user.save()

        url="http://localhost:8000/OTS/login/"
    else:

        url="http://localhost:8000/OTS/signup?error=1/"
        
        

    return HttpResponseRedirect(url)


def login(request):
  user=User.objects.filter(username="admin")
  if not user:
      createAdmin()
  res=render(request,'OTS/login.html')
  return res

  

def logout(request) :

        request.session.clear()#sabhi session clear#ek session clear ke liye del.request.session['realname']

        url="http://localhost:8000/OTS/login/"

        return HttpResponseRedirect(url)

def loginValidation(request):
    #u=User.objects.filter(username=request.POST['username'],password=request.POST['password'])
    try: #login successful
        u=User.objects.get(username=request.POST['username'],password=request.POST['password'])
        request.session['username']=u.username
        request.session['realname']=u.realname
        request.session['role']=u.role
        url="http://localhost:8000/OTS/home/"
    except:
        url="http://localhost:8000/OTS/login/"
    return HttpResponseRedirect(url)

def home(request):

    try:
       
       realname=request.session['realname']

    except KeyError:

        return HttpResponseRedirect("http://localhost:8000/OTS/login/")



    #agar ye argument me render me nhi dena chau or html me access bhi karana session variable ko ham jb tk session chalu h use 

    #le sakte hai then home.html me likhna hoga request.session.realname

    #real ye jinja ka nam hai jo html file me kam melege

    #realname jo hamane session start kiya hai vo

    res=render(request,'OTS/home.html',{'realname':realname})
    return res

def startblog(request):
  try:
    realname=request.session['realname']
    no_of_que=6
    questions_pool=list(Question.objects.all())
    
    questions_list=questions_pool[:6]
    res=render(request,'OTS/start_blog.html',{'questions':questions_list})
    return res
  except KeyError:
      return HttpResponseRedirect("http://localhost:8000/OTS/login/")
 
  
def createAdmin():
    user=User()
    user.username="admin"
    user.password="password"
    user.role="ADMIN"
    user.realname="Super User"
    user.save()


