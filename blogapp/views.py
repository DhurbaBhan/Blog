import email
from multiprocessing import context
from re import template
from django.shortcuts import render
from blogapp.forms import PostCreateForm,UserRegistrationForm,UserLoginForm
from blogapp.models import BlogPost,BlogAppUser

#package for sending mail
from django.core.mail import send_mail
#settings is imported from settings.py file
from django.conf import settings



# Create your views here.
def register(request):
    template='users/register.html'
    user_form=UserRegistrationForm
    context={'form':user_form}
    
    if request.method=='POST':
        obj=BlogAppUser()
        obj.first_name=request.POST.get('first_name')
        obj.middle_name=request.POST.get('middle_name')
        obj.last_name=request.POST.get('last_name')
        obj.contact=request.POST.get('contact')
        obj.email=request.POST.get('email')
        obj.profile=request.POST.get('profile')
        obj.password=request.POST.get('password')
        obj.verification_code='vr0039'
        obj.save()

        #email sending code
        subject='Email Verification'
        message='Your Verification Code is :'+ str(obj.verification_code)
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[obj.email]


        send_mail(subject,message,email_from,recipient_list)


        context.setdefault('success','Account registered successfully..')
        return render (request,template,context)

    else:
        return render (request,template,context)

def test(request):
    user0=BlogAppUser.objects.get(id=5)
    user1=BlogAppUser.objects.all()
    # user2=BlogAppUser.objects.filter()
    template='test.html'
    context={'user':user0,'user1':user1}
    return render(request,template,context)  


def user_dashboard(request):
    if request.session.has_key('session_email'):
        template='dashboard.html'
        context={'success_msg':'Welcome '}
        return render(request,template,context) 

    else:
        form=UserLoginForm
        context={'form':form,'error_msg':'Access Forbidden'}
        template='users/login.html'
        return render(request,template,context)     


def user_login(request):
    form=UserLoginForm
    if request.method=='POST':
        try:
            users=BlogAppUser.objects.get(email=request.POST.get('email'))
            if request.POST.get('password')==users.password:
                template='dashboard.html'
                # storing session with session key 'session_email'
                request.session['session_email']=users.email
                # checking session key value
                if request.session.has_key('session_email'):
                    # accessing session data
                    
                    context={'success_msg':'Welcome  ' +  request.session['session_email']}
                    return render (request,template,context)

                else:  
                    template='users/login.html'  
                    context={'form':form,'error_msg':'access denied'}
                    return render (request,template,context)

            else:
                context={'form':form ,'error_msg':'Invalid email or password'}
                template='users/login.html'
                return render (request,template,context)
        except:
            context={'form':form ,'error_msg':'Not registered yet.'}
            template='users/login.html'
            return render (request,template,context)

    else:
        context={'form':form}
        template='users/login.html'
        return render (request,template,context)  


def user_logout(request):
    if request.session.has_key('session_email'):
        # destroying the session in order to logout user from the system
        del request.session['session_email']
        template='users/login.html'
        form=UserLoginForm
        context={'form':form, 'error_msg': 'you are logged out of the system.'}
        return render(request,template,context)


def post_create(request):
    template='posts/create.html'
    post_form=PostCreateForm
    context={'form':post_form}
    if request.method=='POST':
        # obj_post=BlogPost()
        # obj_post.post_title=request.POST.get('post_title')
        # obj_post.post_description=request.POST.get('post_description')
        # obj_post.slug=request.POST.get('slug')
        # obj_post.post_status=request.POST.get('post_status')
        # obj_post.save()
        obj_form_data=PostCreateForm(request.POST,request.FILES)
        if obj_form_data.is_valid():
            obj_form_data.save()
            context.setdefault('message','Your post created Successfully')          
            return render (request,template,context)

    else:
        return render (request,template,context)

def post_index(request):
    if request.session.has_key('session_email'):
        template='posts/index.html'
        posts=BlogPost.objects.all()
        context={'posts':posts}
        return render(request,template,context)
    else:
        form=UserLoginForm
        context={'form':form,'error_msg':'Access Forbidden'}
        template='users/login.html'
        return render(request,template,context) 

def post_edit(request,post_id):
    if request.session.has_key('session_email'):
        template='posts/edit.html'
        post=BlogPost.objects.get(id=post_id)
        context={'post':post}
        return render(request,template,context)
    else:
        form=UserLoginForm
        context={'form':form,'error_msg':'Access Forbidden'}
        template='users/login.html'
        return render(request,template,context)

def post_show(request,post_id):
    if request.session.has_key('session_email'):
        template='posts/show.html'
        post=BlogPost.objects.get(id=post_id)
        context={'post':post}
        return render(request,template,context)
    else:
        form=UserLoginForm
        context={'form':form,'error_msg':'Access Forbidden'}
        template='users/login.html'
        return render(request,template,context)    

def post_update(request):
    template='posts/index.html'

    posts=BlogPost.objects.all()
    context={"posts":posts}
    
    if request.method=='POST':
        obj_post=BlogPost.objects.get(id=request.POST.get('post_id'))
        obj_post.post_title=request.POST.get('post_title')
        obj_post.post_description=request.POST.get('post_description')
        obj_post.slug=request.POST.get('slug')
        obj_post.post_status=request.POST.get('post_status')
        obj_post.save()
        
        return render(request,template,context)

    else:
        return render(request,template,context)  

def post_delete(request,post_id):
    if request.session.has_key('session_email'):
        template='posts/index.html'
        post=BlogPost.objects.get(id=post_id)
        post.delete()
        posts=BlogPost.objects.all()
        context={'posts':posts}
        return render(request,template,context)  

    else:
        form=UserLoginForm
        context={'form':form,'error_msg':'Access Forbidden'}
        template='users/login.html'
        return render(request,template,context)       

