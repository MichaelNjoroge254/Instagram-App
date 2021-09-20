from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from .views import PostListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import ProfileDetailView



urlpatterns = [
    path('',views.index,name = 'index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('explore/', views.explore, name='explore'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('post/(\d+)/delete',views.delete_post,name = 'delete'),
    path('post/new/',views.create_post,name = 'create'),
    # path('post/(\d+)/comment',views.comment,name = 'comment'),
    path('like/(\d+)',views.like_post,name = 'like'),
    path('follow-unfollow/',views.follow_unfollow,name = 'follow-unfollow-view'),
    path('post/(\d+)',views.detail,name = 'detail'),
    path('search/', views.search_results, name='search'),
    path('user/(P<pk>\d+)',views.ProfileDetailView.as_view(template_name='profile_detail.html'), name='profile-detail-view'),

   
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)