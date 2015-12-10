"""manaflare_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from rest_framework import routers
from manaflare.apps.manaflare_api.v1 import views as v1_views

router = routers.DefaultRouter()
router.register(r'cards', v1_views.CardViewSet)
router.register(r'supertypes', v1_views.SuperTypeViewSet)
router.register(r'types', v1_views.TypeViewSet)
router.register(r'subtypes', v1_views.SubTypeViewSet)
router.register(r'sets', v1_views.SetViewSet)
router.register(r'printings', v1_views.PrintingViewSet)


urlpatterns = [
    url(r'^/', include(router.urls))
]

