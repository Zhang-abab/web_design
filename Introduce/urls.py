from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = 'Introduce'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('editor/', views.editor, name='editor'), #编辑器测试
    path('entity/', views.entity, name='entity'), #实体
    path('mate/', views.mate, name='mate'),#mate标签
    path('semantic/', views.semantic, name='semantic'),#语义化标签
    path('list/', views.list, name='list'),#列表
    path('links/', views.links, name='links'),#超链接
    path('picture/',views.pciture, name='picture'),#图片标签
    path('inline/', views.inline, name='inline'),#内联标签
    path('multi/', views.multi, name='multi'),#媒体    
]