from django.shortcuts import render
from django.template import Context
from msys.forms import EnterFormcc1
from msys.forms import EnterFormcc2
from msys.forms import EnterFormacl
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import ListView
from msys.models import DataEntrycc1
from msys.models import DataEntrycc2
from msys.models import DataEntryacl
from django.template.loader import get_template



class Page1(TemplateView):
    template_name = 'page1.html'

class Select(TemplateView):
    template_name = 'select.html'

class Logincc1(TemplateView):
    template_name = 'logincc1.html'

class Logincc2(TemplateView):
    template_name = 'logincc2.html'

class Loginacl(TemplateView):
    template_name = 'loginacl.html'

class Choosecc1(TemplateView):
    template_name = 'choosecc1.html'

class Choosecc2(TemplateView):
    template_name = 'choosecc2.html' 

class Chooseacl(TemplateView):
    template_name = 'chooseacl.html'

class Login(TemplateView):
    template_name = 'login.html'
# class Enter(TemplateView):
    
#     model = DataEntry
#     template_name = 'enter.html'

#     def post(self, request, *args, **kwargs):
#         print(request.POST)
#         form = EnterForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return render(request,'success.html') 

class Entercc1(CreateView):
    
    model = DataEntrycc1
    form_class = EnterFormcc1
    template_name = 'entercc1.html'


class Entercc2(CreateView):
    
    model = DataEntrycc2
    form_class = EnterFormcc2
    template_name = 'entercc2.html'



class Enteracl(CreateView):
    
    model = DataEntryacl
    form_class = EnterFormacl
    template_name = 'enteracl.html'

    # template_name_suffix = '_update_form'

    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #     form = EnterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return render(request,'success.html') 
        


class Successcc1(TemplateView):
    template_name = 'successcc1.html'


class Successcc2(TemplateView):
    template_name = 'successcc2.html'


class Successacl(TemplateView):
    template_name = 'successacl.html'


def index(request):
    return render(request, 'msys/page1.html')

# def enter(request):
#     if request.POST:
#         form = EnterForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return render(request,'msys/success.html') 
#     return render(request,'enter.html')
    #return render(request, 'msys/success.html')         
'''
        create = request.session.get('sysno')
        
          if create :
            Enter.objects.filter(System_no=create).update(Instrument=request.session.get("instrument"))
            Enter.objects.filter(System_no=create).update(Date=request.session.get("date"))
            Enter.objects.filter(System_no=create).update(Time=request.session.get("time"))
        
            return HttpResponseRedirect('success.html')
    return render(request, 'msys/enter.html') 
'''
'''
def enter(request):
    if request.method == 'POST':
        post=DataEntry()
        post.System_No=request.POST.get('System_No')
        post.Date=request.POST.get('Date')
        post.Make=request.POST.get('Make')
        post.Model_No=request.POST.get('Model_No')
        post.Quantity=request.POST.get('Quantity')
        post.Particulars=request.POST.get('Partiulars')
        post.Remarks=request.POST.get('Remarks')
        post.save()

        return render(request, 'msys/enter.html')
    else:
        return render(request, 'msys/enter.html')
            
'''