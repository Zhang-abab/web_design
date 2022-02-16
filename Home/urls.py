from django.urls import path

from . import views

urlpatterns = [
<<<<<<< f4fc776c58b415edc252e933b892089ccaaede05:Home/urls.py
    path('', views.index, name='index'),
]
=======
    path('editor/', views.editor, name='editor'), #编辑器测试
    path('index/', views.index, name='index')
]
>>>>>>> Introfuce:Introduce/urls.py
