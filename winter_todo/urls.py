"""winter_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,handler400,handler403,handler404,handler500
from django.contrib import admin
from django.urls import path
from todo import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.todo_list,name="todo_list"),
    path('write/',views.todo_write,name="todo_write"),
    url(r'^(?P<pk>\d+)/edit/$', views.todo_edit, name="todo_edit"),
    url(r'^(?P<pk>\d+)/$', views.todo_detail, name="todo_detail"),
    url(r'^(?P<pk>\d+)/delete/$',views.todo_delete,name="todo_delete"),
    url(r'^(?P<pk>\d+)/check$', views.todo_check,name="todo_check"),
    url(r'^(?P<pk>\d+)/importance$', views.todo_importance,name="todo_importance"),
]

'''
handler400 = 'todo.views.bad_request'
handler403 = 'todo.views.permission_denied'
handler404 = 'todo.views.bad_request'
handler500 = 'todo.views.server_error'
'''
