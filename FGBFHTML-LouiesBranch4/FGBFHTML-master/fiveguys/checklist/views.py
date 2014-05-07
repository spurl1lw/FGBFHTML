from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response as render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from checklist.models import Store, Template, Item, Managers


# Create your views here.
def fg_login(request,template_name="Login.html"):
    context = {}
    context.update(csrf(request))
    next = None
    try:
        next = request.GET['next']

    except:
        next = None

    auth_frm = AuthenticationForm(data=request.POST or None)
    context['form'] = auth_frm

    if auth_frm.is_valid():
        try:

            user = authenticate(username=auth_frm.cleaned_data['username'], password=auth_frm.cleaned_data['password'])
            login(request, user)

        except Exception, e:
            return render(template_name, context, context_instance=RequestContext(request))

        m = Managers.objects.get(user=user)
        if m.is_admin:
            return redirect('admin_home')
        elif m.is_account_manger:
            return redirect('account_manager_home')
        else:
            return redirect('manager_home')


    return render(template_name, context, context_instance=RequestContext(request))


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
        StoreID = request.GET.get("storeidvalue")

    except Exception ,e:
        print e
        return HttpResponse(e)
    if StoreID:
        try:
            MyStoreID = Store()
            MyStoreID.storeid = StoreID
            MyStoreID.save()
            return HttpResponse("Location Saved")
        except Exception ,e:

            return HttpResponse("Location Not Saved")
    else:
        return render(template_name,context, context_instance=RequestContext(request))

def CreateTemplate(request,template_name="CreateTemplate.html"):
    context={}
    return render(template_name,context, context_instance=RequestContext(request))

def Users(request,template_name="Users.html"):
    context={}
    context.update(csrf(request))

    #if request.method == 'POST':
     #   form = MyRegistrationForm(request.POST)


      #  form.save()

       # return HttpResponseRedirect('/Users/')




    context['form'] = MyRegistrationForm()


    return render(template_name,context, context_instance=RequestContext(request))

def email_settings(request,template_name="AutoEmailSetting.html"):
    context={}
    return render(template_name,context, context_instance=RequestContext(request))

def reportchecklist(request,template_name="reportchecklist.html"):
    context={}
    context['Templates']= Template.objects.all()
    context['Items']= Item.objects.all()
    return render(template_name,context, context_instance=RequestContext(request))


def summaryreport(request,template_name="SummaryReport.html"):
    context={}
    return render(template_name,context, context_instance=RequestContext(request))



def fill_checklist(request,template_name="Fill_Checklist.html"):
    context={}
    #context['Templates']= Template.objects.all()
    #context['Items']= Item.objects.all()
    return render(template_name,context, context_instance=RequestContext(request))

def fg_logout(request):
    logout(request)
    return HttpResponseRedirect('/Login/')

def mainchecklist(request,template_name="mainchecklist.html"):

    context={}

    print request.POST

    if request.GET:
        print request.GET
        try:
            templateName = request.GET['TemplateValue']
            context['StoreName'] = request.GET['LocationValue']
            context['Items'] = Item.objects.filter(templateid__pk = templateName)
        except Exception, e:
            return HttpResponse(e)
            #return HttpResponseRedirect('/Build_Checklist/')

    return render(template_name,context, context_instance=RequestContext(request))

def Users2(request,template_name="Users2.html"):
    context={}
    try:
     Username = request.GET.get("UserID")
     password = request.GET.get("Password")
     lname = request.GET.get("Lname")
     emailAddress = request.GET.get("EmailAddress")
     fname = request.GET.get("Fname")
     isadmin = request.GET.get("isAdmin")
     ismanager= request.GET.get("isManager")
     isaccountmanager= request.GET.get("isAccountManager")
     print (Username)
    except Exception,e:
        return HttpResponse(e)

    if Username:
        User.objects.create_user(Username, email=emailAddress,password=password)

    else:
        return render(template_name,context, context_instance=RequestContext(request))



def account_manager_home(request,template_name="AccountManagerHome.html"):
    context ={}
    context['Templates']= Template.objects.all()
    context['Stores']= Store.objects.all()

    return render(template_name,context, context_instance=RequestContext(request))

def accountmainchecklist(request,template_name="accountmainchecklist.html"):

    context={}

    print request.POST

    if request.GET:
        print request.GET
        try:
            templateName = request.GET['TemplateValue']
            context['StoreName'] = request.GET['LocationValue']
            context['Items'] = Item.objects.filter(templateid__pk = templateName)
        except Exception, e:
            return HttpResponse(e)
            #return HttpResponseRedirect('/Build_Checklist/')

    return render(template_name,context, context_instance=RequestContext(request))

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    account_type = forms.ChoiceField(choices=((0,'Manager'),(1,'Admin'),(-1,'Account Manager'),))

    class Meta:

        model = User
        fields = ('username','first_name','last_name','password1','password2','email','account_type')










