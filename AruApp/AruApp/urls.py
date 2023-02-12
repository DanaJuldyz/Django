from women.views import *
from django.urls import path,include
from django.conf.urls import handler404
from django.conf.urls import handler403
from django.conf.urls import handler500
from django.conf.urls import handler400


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('women.urls')),

]
handler404 = 'women.views.not_found'
handler403 = 'women.views.Access_is_denied403'
handler500 = 'women.views.server_error'
handler400 = 'women.views.request_processing'

