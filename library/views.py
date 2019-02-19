from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import json
import requests

def home(request):
    context={

        'posts':Post.objects.all()    #'posts' is key and we passed posts dictionary created up
    }
    return render(request,'library/home.html',context)  

def about(request):
    return render(request,'library/about.html',{'title':'About'})

def issue_book(request):

    
    if request.method == 'POST':
        title=request.POST["title"]
        author=request.POST["Author"]
        ISBN=request.POST["ISBN"]
        genre=request.POST["Genre"]
        issuedate=Post.objects.create(title=title,author=author,ISBN=ISBN,genre=genre)
        issuedate.save()
        json_data={
                'title':title,
                'author':author    
        }
        received_json_data=json.dumps(json_data)
        print(received_json_data)

        
        '''
        form = IssueBookForm(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data.get('ISBN')
            #messages.success(request,f'BOOK ISSUED with isbn number {isbn}')    
            return redirect('Library-home')
    else:
        form = IssueBookForm()
        '''
    return render(request,'library/issue_book.html')

