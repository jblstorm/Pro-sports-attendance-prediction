from django.shortcuts import render, redirect
from django.http import HttpResponse,StreamingHttpResponse
from django.conf import settings

import os
# Create your views here.

def create(request):
    return HttpResponse('Create!')

def read(request, id):
    return HttpResponse('Read!'+id)

def post(request):
    if request.method == 'POST':
        list_item = request.POST.getlist('checkbox')
        reset = request.POST.getlist('reset')
        print(list_item)
        print(reset)
        if len(reset) == 1:
            return render(request, 'post_list.html', {'GRAPH':0,'CHECK':'off'})
        elif len(list_item) == 1:
            if list_item[0] == '3':
                return render(request, 'post_list.html', {'GRAPH':3,'CHECK_3':'on'})
            elif list_item[0] == '2':
                return render(request, 'post_list.html', {'GRAPH':2,'CHECK_2':'on'})
            else :
                return render(request, 'post_list.html', {'GRAPH':1,'CHECK_1':'on'})
        else :
            return render(request, 'post_list.html', {'GRAPH':0,'CHECK':'off'})
    else :
        return render(request, 'post_list.html', {'GRAPH':0,'CHECK':'off'})


def download(request):
    filename = request.GET.get('file')
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    fp = open(filepath, 'rb')
    response = StreamingHttpResponse(fp)
    # response = FileResponse(fp)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % filename
    return response
    fp.close()