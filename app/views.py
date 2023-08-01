from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
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





