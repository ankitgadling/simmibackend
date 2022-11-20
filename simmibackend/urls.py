"""simmibackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from carrers.views import GetJobs
from contact.views import contact
from .views import home
from .router import router
from example.views import V
from django.conf import settings
from django.conf.urls.static import static
#from userprofile import urls

urlpatterns = [
    path('', home),
    path('api/account/', include("account.urls")),
    path('api/simmi-admin/', admin.site.urls),
    path('contact/', include("contact.urls")),
    path('api/donation/', include(router.urls)),
    path('api/carrers/', include("carrers.urls")),
    path('blogs/', include('blog.urls')),
    path('api/gallery/', include("gallery.urls")),
    path('latestnews/', include('latestnews.urls')),
    path('api/events/', include('events.urls')),
    path('api/certification/', include('certifications.urls')),
    path('api/transactions/', include('user_transactions.urls')),
    path('api/about/', include('about.urls')),
    path('api/admin_transactions/', include('admin_transactions.urls')),
    path('api/admin_about/', include('admin_about.urls')),
    path('api/admin_details/', include('admin_details.urls')),
    path('api/admin_logs/', include('admin_logs.urls')),
    path('api/', include('speaker.urls')),
    path('transactions/', include('Razorpay.urls')),
    path('api/inst_aliance/', include('institutional_aliance.urls')),
    path('api/', include('get_involved.urls')),
    path('api/tender',include('tender.urls')),
    path('api/admin_tender/',include('admin_tender.urls')),
    path('a',V.as_view()),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
