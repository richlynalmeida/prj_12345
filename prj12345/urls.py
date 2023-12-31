"""
prj12345 URL Configuration

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

# Uncomment next two lines to enable admin:
from django.urls import path, include
from django.contrib import admin
from patterns import patterns
from validators import url

admin.autodiscover()

urlpatterns = [
    path('', include(('csl.urls', 'home'), namespace="csl")),
    path('', include(('n_knowledgebase.urls', 'n_knowledgebase'), namespace="n_knowledgebase")),
    # path('', include(('s_sandbox.urls', 's_sandbox'), namespace="s_sandbox")),
    # path('nested_admin/', include(('nested_admin.urls', 'home'), namespace="nested_admin")),
    # path('grappelli/', include(('grappelli.urls', 'home'), namespace="grappelli")),
    # path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
]
