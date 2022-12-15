from django.shortcuts import get_object_or_404, redirect, render
from .forms import SignUpForm,LoginForm,MessageForm, UsernameChangeForm, MailadressChangeForm, IconChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
from .models import CustomUser,Message
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
def index(request):
    return render(request, "myapp/index.html")

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =SignUpForm()
    return render(request, "myapp/signup.html", {'form': form})

class Login(LoginView):
    form = LoginForm
    template_name = "myapp/login.html"

@login_required()
def friends(request):
    login_user = request.user
    user_list = CustomUser.objects.all().exclude( Q(username="admin")|Q(id=login_user.id))
    message_list_have = []
    message_list_no_have = []
    for friend in user_list:
        message = Message.objects.filter(Q(name_to = friend, name_from = login_user)|Q(name_to = login_user, name_from = friend)).all().order_by("create_at").last()
        if message:
            message_list_have.append([login_user,friend,message.content,message.create_at])
        else:
            message_list_no_have.append([login_user,friend,"",None])
    message_list_have.sort(key = lambda x:x[3], reverse=True)
    message_list=message_list_have+message_list_no_have
    return render(request, "myapp/friends.html",{'user_list': user_list,'message_list':message_list,'login_user':login_user})
@login_required()
def talk_room(request,username_id):
    friends = get_object_or_404(CustomUser,id=username_id)
    login_user = request.user
    message_list = Message.objects.filter(Q(name_to = friends, name_from = login_user)|Q(name_to = login_user, name_from = friends)).all()
    form = MessageForm()
    if request.method == 'POST':
        new_talk = Message(name_from=login_user, name_to=friends)
        form = MessageForm(request.POST, instance=new_talk)
        if form.is_valid():
            form.save()
            return redirect("talk_room",username_id)
        else:
            form = MessageForm()
    return render(request, "myapp/talk_room.html",{'friends':friends,'message_list':message_list, 'form':form})

@login_required()
def setting(request):
    return render(request, "myapp/setting.html")

@login_required()
def username_change(request):
    form = UsernameChangeForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            user_obj = CustomUser.objects.get(username=request.user.username)
            user_obj.username = username
            user_obj.save()
            return redirect("username_change_done")
    return render(request, "myapp/username_change.html", {'form':form})
@login_required()
def username_change_done(request):
    return render(request, "myapp/username_change_done.html")
@login_required()
def mailadress_change(request):
    form = MailadressChangeForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"]
            user_obj = CustomUser.objects.get(username=request.user.username)
            user_obj.email = email
            user_obj.save()
            
            return redirect("mailadress_change_done")
    
    return render(request, "myapp/mailadress_change.html",{"form":form})

@login_required()
def mailadress_change_done(request):
    return render(request, "myapp/mailadress_change_done.html")

@login_required()
def icon_change(request):
    user = request.user
    form = IconChangeForm(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            image = form.cleaned_data["image"]
            user_obj = CustomUser.objects.get(username=request.user.username)
            user_obj.image = image
            user_obj.save()
            return redirect("icon_change_done")
    return render(request, "myapp/icon_change.html",{"form":form,"user":user})

@login_required()
def icon_change_done(request):
    return render(request, "myapp/icon_change_done.html")

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('password_change_done')
    template_name = 'myapp/password_change.html'
class PasswordChangeDone(LoginRequiredMixin,PasswordChangeDoneView):
    template_name = 'myapp/password_change_done.html'

class Logout(LoginRequiredMixin, LogoutView):
    ""