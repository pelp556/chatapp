from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup_view, name='signup'),
    path('login', views.Login.as_view(), name='login'),
    path('friends', views.friends, name='friends'),
    path('talk_room/<int:username_id>', views.talk_room, name='talk_room'),
    path('setting', views.setting, name='setting'),
    path('username_change', views.username_change, name='username_change'),
    path('username_change_done', views.username_change_done, name='username_change_done'),
    path('mailadress_change', views.mailadress_change, name='mailadress_change'),
    path('mailadress_change_done', views.mailadress_change_done, name='mailadress_change_done'),
    path('icon_change', views.icon_change, name='icon_change'),
    path('icon_change_done', views.icon_change_done, name='icon_change_done'),
    path('password_change', views.PasswordChange.as_view(), name='password_change'),
    path('password_change_done', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('logout', views.Logout.as_view(), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)