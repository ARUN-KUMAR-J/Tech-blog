from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Posts,Category,aboutus
from django.core.paginator import Paginator
from .forms import ContactForm

from django.http import Http404
# Create your views here.
'''
Static data example
posts=[
        {'id':1,'Title':'post 1','content':'content of post1'},
        {'id':2,'Title':'post 2','content':'content of post2'},
        {'id':3,'Title':'post 3','content':'content of post3'},
        {'id':4,'Title':'post 4','content':'content of post4'}
    ]
'''

def index(request):
    blog_title="Latest Posts"

    #getting posts from model
    all_posts = Posts.objects.all()
    #paginate
    paginator=Paginator(all_posts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'index.html',{'blog_title':blog_title,'page_obj':page_obj})
def detail(request,slug):
    
    #getting data from static file
    #post=next((item for item in posts if item['id'] == post_id),None)
    #getting data from database using id 
    try:
        posts =Posts.objects.get(slug=slug)
        related_posts =Posts.objects.filter(category_id=posts.category_id).exclude(pk=posts.id )
    except Posts.DoesNotExist:
        raise Http404("Post Doesn't Exist")
   # logger=logging.getLogger("TESTING")
   # logger.debug(f'post variable is {posts}')
    return render(request,'detail.html',{'posts':posts,'related_posts':related_posts})
def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))
def new_url_view(request):
    return HttpResponse("This is the new url")
def contact_view(request):
    if request.method=='POST':
        form =ContactForm(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        logger=logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f"POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message='Your email has been submitted successfully'
            return render(request,'contact.html',{'form':form,'success_message':success_message})
        else:
            logger.debug('Form validation failed')
        return render(request,'contact.html',{'form':form,'name':name,'email':email,'message':message})
    return render(request,'contact.html')
def about_view(request):
    about_content=aboutus.objects.first().content
    Programming_Languages=aboutus.objects.first().Programming_Languages
    Database_Management=aboutus.objects.first().Database_Management
    problem_solving=aboutus.objects.first().problem_solving
    Web_development=aboutus.objects.first().Web_development
    return render(request,'about.html',{'about_content':about_content,'Programming_Languages':Programming_Languages,'Database_Management':Database_Management,'problem_solving':problem_solving,'Web_development':Web_development})