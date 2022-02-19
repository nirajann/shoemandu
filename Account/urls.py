from django.urls import path,include
from django.urls import path
from Account import views

urlpatterns = [
   path('signup/' ,views.signupcustomer ,name='signup'),
   path('login/',views.login,name='login') ,
   path('logout/',views.logout_view,name='logout_view') ,

]