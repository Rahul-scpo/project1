from django.urls import path
from . import views
urlpatterns=[path("path1",views.signup,name="signup"),
             path("",views.login,name="login"),
             path("path2",views.personal,name='personal'),
             path("path3",views.personaldata,name='personaldata')]