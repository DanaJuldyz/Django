from women.views import *
from django.urls import path,include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('women.urls')),

]
handler404 = 'women.views.not_found'
