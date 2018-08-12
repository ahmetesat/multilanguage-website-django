"""multilanguage-website-django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from hk.views import *
from django.urls import re_path
from django.views.static import serve

# handler403 = '_handler403'
# handler404 = '_handler404'
# handler500 = '_handler500'

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
]

urlpatterns += i18n_patterns(

    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name="home"),
    url(r'^About/$', about_page, name="About"),
    url(r'^Publications/Articles$', article_page, name="Articles"),
    # url(r'^Publications/Articles/Detail/(?P<article_name>[\w\s]+)/$', article_detail, name="Article_Detail"),
    url(r'^Publications/Articles/Detail/(?P<pk>\d+)/(?P<article_name>[\w\s]+)/$', article_detail, name="Article_Detail"),
    url(r'^Publications/Books$', book_page, name="Books"),
    # url(r'^Publications/Books/Detail/(?P<book_name>[\w\s]+)/$', book_detail, name="Book_Detail"),
    url(r'^Publications/Books/Detail/(?P<pk>\d+)/(?P<book_name>[\w\s]+)/$', book_detail, name="Book_Detail"),
    url(r'^Academic/Courses$', course_page, name="Courses"),
    url(r'^Academic/Course/Detail/(?P<pk>\d+)/(?P<course_name>[\w\s]+)/$', course_detail, name="Course_Detail"),
    url(r'^Academic/Conferences$', conference_page, name="Conferences"),
    url(r'^Academic/Supervised_Thesis$', supervised_thesis_page, name="Supervised_Thesis"),
    url(r'^Academic/Thesis_Jury_Membership$', thesis_jury_membership_page, name="Thesis_Jury_Membership")

)

if settings.DEBUG:
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
