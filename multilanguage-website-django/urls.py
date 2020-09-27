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
    'CourseDetailSitemap': CourseDetailSitemap,
    'InternetPubDetailSitemap':InternetPubDetailSitemap
}
from django.conf.urls import include

urlpatterns = [
    re_path(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files')
]

urlpatterns += i18n_patterns(
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    re_path(r'^sitemap.xml/', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^admin/',
        admin.site.urls),

    re_path(r'^$',
        home_page, name="home"),
    re_path(_(r'^hakkinda/$'),
        about_page, name="About"),

    re_path(_(r'^yayinlar/makaleler/$'),
        article_page, name="Articles"),
    re_path(_(r'^yayinlar/makaleler/detay/(?P<pk>\d+)/(?P<article_name>[\w\s-]+)/$'),
        article_detail,name="Article_Detail"),
    re_path(_(r'^yayinlar/kitaplar/$'),
        book_page, name="Books"),
    re_path(_(r'^yayinlar/kitaplar/detay/(?P<pk>\d+)/(?P<book_name>[\w\s-]+)/$'),
        book_detail, name="Book_Detail"),
    re_path(_(r'^yayinlar/internet-yayinlari/$'),
        internet_publications, name="Internet_Publications"),
    re_path(_(r'^yayinlar/internet-yayinlari/detay/(?P<pk>\d+)/(?P<internet_pub_artic_name>[\w\s-]+)/$'),
        internet_publication_detail, name="Internet_Publication_Detail"),

    re_path(_(r'^akademik/kurslar/$'),
        course_page, name="Courses"),
    re_path(_(r'^akademik/kurslar/detay/(?P<pk>\d+)/(?P<course_name>[\w\s-]+)/$'),
        course_detail, name="Course_Detail"),
    re_path(_(r'^akademik/konferanslar/$'),
        conference_page, name="Conferences"),
    re_path(_(r'^akademik/tez-danismanligi/$'),
        supervised_thesis_page, name="Supervised_Thesis"),
    re_path(_(r'^akademik/tez-juri-uyeligi/$'),
        thesis_jury_membership_page, name="Thesis_Jury_Membership"),

    re_path(_(r'^arastirma-alanlari/$'), research_interest_detail, name="research_interest_detail"),

    re_path(_(r'^iletisim/$'), contact, name="Contact"),
    re_path(_(r'^iletisim-mail-gonder/$'), contact_send_email, name="contact_send_email"),

    re_path(_(r'^sartlar-ve-kasullar/$'), terms_and_conditions, name="terms-and-conditions")

)

if settings.DEBUG:
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
admin.autodiscover()
admin.site.enable_nav_sidebar = False