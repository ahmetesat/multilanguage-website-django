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
from django.conf.urls import url, static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from hk.views import *
from django.urls import re_path
from django.views.static import serve
from hk.sitemaps import *
from django.contrib.sitemaps.views import sitemap
from django.utils.translation import ugettext_lazy as _

handler403 = 'hk.views.error_handler403'
handler404 = 'hk.views.error_handler404'
handler500 = 'hk.views.error_handler500'

sitemaps = {
    # "Article": ArticleSitemap,
    'StaticSitemapHighImportance': StaticSitemapHighImportance,
    'StaticSitemapMiddleImportance': StaticSitemapMiddleImportance,
    'StaticSitemapLowImportance': StaticSitemapLowImportance,
    'ArticleDetail': ArticleDetailSitemap,
    'BookDetailSitemap': BookDetailSitemap,
    'CourseDetailSitemap': CourseDetailSitemap
}
from django.conf.urls import include

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files')
]

urlpatterns += i18n_patterns(
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^sitemap.xml/', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^admin/',
        admin.site.urls),

    url(r'^$',
        home_page, name="home"),
    url(_(r'^hakkinda/$'),
        about_page, name="About"),

    url(_(r'^yayinlar/makaleler/$'),
        article_page, name="Articles"),
    url(_(r'^yayinlar/makaleler/detay/(?P<pk>\d+)/(?P<article_name>[\w\s]+)/$'),
        article_detail,name="Article_Detail"),
    url(_(r'^yayinlar/kitaplar/$'),
        book_page, name="Books"),
    url(_(r'^yayinlar/kitaplar/detay/(?P<pk>\d+)/(?P<book_name>[\w\s]+)/$'),
        book_detail, name="Book_Detail"),
    url(_(r'^yayinlar/internet-yayinlari/$'),
        internet_publications, name="internet_publications"),
    url(_(r'^yayinlar/internet-yayinlari/detay/(?P<pk>\d+)/(?P<internet_pub_artic_name>[\w\s]+)/$'),
        internet_publication_detail, name="internet_publication_detail"),

    url(_(r'^akademik/kurslar/$'),
        course_page, name="Courses"),
    url(_(r'^akademik/kurslar/detay/(?P<pk>\d+)/(?P<course_name>[\w\s]+)/$'),
        course_detail, name="Course_Detail"),
    url(_(r'^akademik/konferanslar/$'),
        conference_page, name="Conferences"),
    url(_(r'^akademik/tez-danismanligi/$'),
        supervised_thesis_page, name="Supervised_Thesis"),
    url(_(r'^akademik/tez-juri-uyeligi/$'),
        thesis_jury_membership_page, name="Thesis_Jury_Membership"),

    url(_(r'^arastirma-alanlari/$'), research_interest_detail, name="research_interest_detail"),

    url(_(r'^iletisim/$'), contact, name="Contact"),
    url(_(r'^iletisim-mail-gonder/$'), contact_send_email, name="contact_send_email"),

    url(_(r'^sartlar-ve-kasullar/$'), terms_and_conditions, name="terms-and-conditions")

)

if settings.DEBUG:
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
