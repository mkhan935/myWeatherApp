from django.template.response import TemplateResponse
from station.models import Reading
from  .forms import ZipForm

import worker

def homePage(request):


    getTheZIP=request.GET['zip']
    worker.fetch_data(getTheZIP)
    data = Reading.objects.last()
    return TemplateResponse(request,'index.html',{'data':data})




def getZipCode(request):

    form = ZipForm()
    return TemplateResponse(request,'form.html',{'form':form})