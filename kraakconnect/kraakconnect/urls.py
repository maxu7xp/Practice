
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auths/', include('auths.urls')),
    path('chats/', include('chats.urls'))
    
]
