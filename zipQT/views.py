from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

from .validators import validate_file_extension
import uuid
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

fs = FileSystemStorage()

def home(request):
    return render(request, 'zipQT/home.html')

def help(request):
    return render(request, 'zipQT/help.html')


def convert(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        #fs = FileSystemStorage(validators = [validate_file_extension(uploaded_file)])
        name = str(uuid.uuid4())
        fs.save(name+".txt", uploaded_file)
        os.system('text2qti ' + os.path.join(MEDIA_ROOT, name+".txt"))
      
        with open(os.path.join(MEDIA_ROOT, name+".zip"), 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/zip")
            response['Content-Disposition'] = 'inline; filename=' + uploaded_file.name + ".zip"
            return response
        raise Http404

    else:
        redirect('zipQT-home')

    return render(request, 'zipQT/convert.html')








    