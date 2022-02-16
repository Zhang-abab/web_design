from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = 'Introduce'

urlpatterns = [
    path('editor/', views.editor, name='editor'), #编辑器测试
]