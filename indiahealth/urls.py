"""indiahealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from signIn import views as v1
from home import views as v2
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',v1.signIn),
    url(r'^postsign/',v1.postsign),
    url(r'^logout/',v1.logout,name="log"),
    url(r'^postsignup/',v1.postsignup,name='postsignup'),
    url(r'^home/',v2.home),
    url(r'^doctordetails/',v2.doctordetails,name='doctordetails'),
    url(r'^post_create/',v2.post_create,name='post_create'),
    url(r'^profile/',v2.profile,name='profile'),
    url(r'^postprofile/',v2.postprofile,name='postprofile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# sudo fuser -k 8000/tcp