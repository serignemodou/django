from django.shortcuts import render
from django.http import FileResponse
from django.http import HttpResponse

from blog.models import Cours

def index(request):
    """with open("C:/Users/user/Desktop/python/doc/probabilte.pdf", "rb") as pdf:
        response= HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition']= 'inline; filename=some_file.pdf'
        return response
    pdf.close() """

    return render(request, 'blog/index.html', {'cours':Cours.objects.all()})

def show(request):
    
    return render(request, 'blog/show.html' )


