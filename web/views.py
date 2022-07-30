from pdb import post_mortem
from django.http import HttpRequest
from django.shortcuts import render,HttpResponse
from .models import Contact
from rest_framework import generics
from .serializers import WebSerializers

# Create your views here.

def index(request):

    if request.method == 'POST':
         phone = request.POST.get('phone')
         email = request.POST.get('email')
         query = request.POST.get('query')
         forum = Contact(email=email ,query = query,phone = phone)
         forum.save()

    return render(request,'Askquery.html')

def forum(request):
    forum = Contact.objects.all()
    return render(request,'forum.html',{'venues': forum})



def show_forum(request,venue_id):
    forum = Contact.objects.get(pk = venue_id)
    return render(request,'show_forum.html',{'venue':forum})


def update_forum(request):
          return render(request)
   

def search_bar(request):
           if request.method == 'POST':
                   search_query = request.POST['searched']
                   venue = Contact.objects.filter(query__contains = search_query)
                   return render(request,'search_bar.html',{'searched':search_query,'venue':venue})
       
class WebGetCreate(generics.ListCreateAPIView):
         queryset = Contact.objects.all()
         serializer_class = WebSerializers

class WebUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = WebSerializers

    
   