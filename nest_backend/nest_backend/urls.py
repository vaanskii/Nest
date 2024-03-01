from django.contrib import admin
from django.urls import path, include

from account.views import activateEmail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('activateEmail/', activateEmail, name='activate_email')
]
