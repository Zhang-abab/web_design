from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = 'Introduce'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('editor/', views.editor, name='editor'), #编辑器测试
    path('editor/<str:content>',views.editor_content),
    path('entity/', views.entity, name='entity'), #实体
    path('entity/<str:content>',views.entity_content),
    path('mate/', views.mate, name='mate'),#mate标签
    path('mate/<str:content>',views.mate_content),
    path('semantic/', views.semantic, name='semantic'),#语义化标签
    path('semantic/<str:content>',views.semantic_content),
    path('list/', views.list, name='list'),#列表
    path('list/<str:content>',views.list_content),
    # path('links/', views.links, name='links'),#超链接
    # path('links/<str:content>',views.links_content),
    # path('picture/',views.pciture, name='picture'),#图片标签
    # path('picture/<str:content>',views.picture_content),
    # path('inline/', views.inline, name='inline'),#内联标签
    # path('inline/<str:content>',views.inline_content),
    # path('multi/', views.multi, name='multi'),#媒体  
    # path('multi/<str:content>',views.multi_content),  
]