from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response as render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from checklist.models import Store, Template, Item


# Create your views here.
def fg_login(request,template_name="Login.html"):
    context = {}
    context.update(csrf(request))
    next = None


    try:
        next = request.GET['next']

    except:
        next = ""



    auth_frm = AuthenticationForm(data=request.POST or None)
    context['form'] = auth_frm

    if auth_frm.is_valid():
        try:
            user = authenticate(username=auth_frm.cleaned_data['username'], password=auth_frm.cleaned_data['password'])
            login(request, user)
        except Exception, e:
            pass

        return redirect('manager_home')

    return render(template_name, context, context_instance=RequestContext(request))

@login_required(login_url='Login/')
def manager_home(request,template_name="ManagerHome.html"):
    context ={}
    context['Templates']= Template.objects.all()
    context['Stores']= Store.objects.all()

    return render(template_name,context, context_instance=RequestContext(request))

def report(request,template_name="ReportMain.html"):
    context= {}
    context['Templates']= Template.objects.all()
    context['Stores']= Store.objects.all()

    return render(template_name, context, context_instance=RequestContext(request))

def admin_home(request,template_name="AdminHome.html"):
    context={}
    return render(template_name, context, context_instance=RequestContext(request))

def new_location(request,template_name="new_location.html"):
    context={}

    try:
        StoreID = request.GET["storeidvalue"]
    except Exception ,e:
        return HttpResponse(e)

    try:
        MyStoreID = Store()
        MyStoreID.storeid = StoreID
        MyStoreID.save()
    except Exception ,e:
         return HttpResponse("Location Not Saved")

    return render(template_name,context, context_instance=RequestContext(request))

def CreateTemplate(request,template_name="CreateTemplate.html"):
    context={}
    return render(template_name,context, context_instance=RequestContext(request))

def Users(request,template_name="Users.html"):
    context={}
    return render(template_name,context, context_instance=RequestContext(request))

def email_settings(request,template_name="AutoEmailSetting.html"):
    context={}
    return render(template_name,context, context_instance=RequestContext(request))

def fill_checklist(request,template_name="Fill_Checklist.html"):
    context={}
    context['Templates']= Template.objects.all()
    context['Items']= Item.objects.all()
    return render(template_name,context, context_instance=RequestContext(request))


