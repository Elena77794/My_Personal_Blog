"""
URL configuration for Blog_Post project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

<<<<<<< HEAD
from posts.views import PostAPIList, PostAPIUpdate, PostApiDestroy
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'post', PostViewSet)
# path('api/v1/', include(router.urls))
=======
from posts.views import PostViewSet
from rest_framework import routers
>>>>>>> 0601ef10fea95110d0d4ce56ba2872af43c28785

router = routers.SimpleRouter()
router.register(r'post', PostViewSet)
print(router.urls)
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('posts.urls')),
<<<<<<< HEAD
    path('api/v1/post/', PostAPIList.as_view()),
    path('api/v1/post/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/v1/delete/<int:pk>/',  PostApiDestroy.as_view()),
=======
    path('api/v1/', include(router.urls))
    # path('api/v1/postlist',  PostViewSet.as_view({'get': 'list'})),
    # path('api/v1/postlist/<int:pk>/', PostViewSet.as_view({'put': 'update'})),
    # path('api/v1/postdetail/<int:pk>/',  PostApiDetailView.as_view()),
>>>>>>> 0601ef10fea95110d0d4ce56ba2872af43c28785
]
