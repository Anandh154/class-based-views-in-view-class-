from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.
#fbv for return strig as response
def fbv_str(request):
    return HttpResponse('<h1>this is fbv string response</h1>')
#cbv for return strig as response
class CbvStr(View):
    def get(self,request):
        return HttpResponse('<h1>this is CBV string response</h1>')
class CbvView(View):
    def get(self,request):
        return render(request,'cbv_view.html')   
    
class CbvTemp(TemplateView):
    template_name='cbv_template.html'

class Data_render(View):
    def get(self,request):
        d={'name':'KVR'}
        return render(request,'data_render.html',d)
    
class Cbv_Mf(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'cbv_mf.html',d)
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data inserted is successfully in cbv')
        
def fbv_mf(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=="POST":
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data inserted is successfully in fbv')

    return render(request,'cbv_mf.html',d)


