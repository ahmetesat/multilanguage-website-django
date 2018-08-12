from django.shortcuts import render, render_to_response
from django.utils import translation
import logging

from hk.models import *

from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

from django.http import HttpResponse

logger = logging.getLogger(__name__)

def _handler403(request, exception, template_name='403.html'):
    response = render(request, "403.html", {})
    response.status_code = 403
    return response

def _handler404(request, exception, template_name='404.html'):
    response = render(request, "404.html", {})
    response.status_code = 404
    return response


def _handler500(request, exception, template_name='500.html'):
    response = render(request, "500.html", {})
    response.status_code = 500
    return response


def home_files(request, filename):  # robots.txt and humans.txt required for searc engines
    return render(request, filename, {}, content_type="text/plain")


def home_page(request):
    return render(request, "home.html")


def about_page(request):
    try:
        selected_language = translation.get_language()  # Gets the current selected language
        if request.method == 'GET':
            #author_info = About_Translation.objects.get(name="Hacı Kara")

            # a = Content_Language.objects.filter(language="tr")
            # author_info = About_Translation.objects.filter(language__in=a)

            author_info = About_Translation.objects.filter(language__language=selected_language)
            if not author_info:
                author_info = About_Translation.objects.filter(language__language="tr")
            return render(request, "about.html", {"author_info": author_info})
    except:
        pass

def article_page(request):
    try:
        selected_language = translation.get_language()  # Gets the current selected language

        if request.method == 'GET':
            #article_info = Article_Translation.objects.filter(website_language__language=selected_language).values("name","pub_year","article__article_language__language","article__name")#.filter(article__article=get_article)#Article.objects.filter(article_translation__website_language__language=selected_language)#.filter(website_language__language=selected_language)#.filter(article__name=article_name)#Article.objects.filter(article_translation__website_language__language=selected_language)#filter(article_translation__website_language=selected_language)#.filter(article_translation__website_language=selected_language)#.values("name", "pub_year","article_language")
            #aa = Article_Translation.objects.annotate(Article("id"))
            #article_info = Article_Translation.objects.filter(article__article=aa)
            ##article_info = Article_Translation.objects.filter(website_language__language=selected_language)#select_related()
            """article_info= Article_Translation.objects.filter(article__article=None)#filter(website_language__language=selected_language)
            print (article_info.query)"""
            article_info = Article_Translation.objects.filter(website_language__language=selected_language)#.values("name","pub_year","article__article_language__language","article__name")
            if not article_info:
            #     language = "en" #if selected_language == "tr" else "tr"
                article_info = Article_Translation.objects.filter(website_language__language="tr").values("name","pub_year","article__article_language__language","article__name_bsc")

            return render(request, "articles.html",
                          {"base_publications": "base_publications.html",
                           "publication_info": article_info})
    except:
        pass

def article_detail(request,pk=None,article_name=None):                 #Gets chosen article name and query in database

    try:
        selected_language = translation.get_language()  # Gets the current selected language

        if request.method == 'GET':
            publication_info_detail = Article_Translation.objects.\
                filter(website_language__language=selected_language).\
                filter(article__pk=pk)
            if not publication_info_detail:
                publication_info_detail = Article_Translation.objects.filter(
                    website_language__language="tr").filter(article__name=pk)

            return render(request, "article_detail.html", {"publication_info_detail": publication_info_detail})
    except:
        pass



def book_page(request):
    try:
        selected_language = translation.get_language()  # Gets the current selected language
        if request.method == 'GET':

            book_info = Book_Translation.objects.filter(website_language__language=selected_language)
            if not book_info:
                book_info = Book_Translation.objects.filter(
                    website_language__language="tr")
            return render(request, "books.html",
                          {"base_publications": "base_publications.html",
                           "publication_info": book_info})
    except:
        pass

def book_detail(request,pk=None,book_name=None):                 #Gets chosen article name and query in database

    try:

        selected_language = translation.get_language()  # Gets the current selected language

        if request.method == 'GET':
            publication_info_detail = Book_Translation.objects.\
                                      filter(website_language__language=selected_language).\
                                      filter(book__pk=pk)

            if not publication_info_detail:
                publication_info_detail = Book_Translation.objects.\
                    filter(website_language__language="tr").filter(book__pk=pk)

            return render(request, "book_detail.html", {"publication_info_detail": publication_info_detail})

    except:
        pass

def course_page(request):
    # try:
        selected_language = translation.get_language()  # Gets the current selected language
        if request.method == 'GET':
            course_info = Course_Translation.objects.all()
            # course_info = Course_Translation.objects.\
            #     filter(website_language__language=selected_language)
            #
            #
            # if not course_info:
            #     course_info = Course_Translation.objects.\
            #         filter(website_language__language="tr")


            return render(request, "courses.html",{"base_academic_life": "base_academic_life.html","academic_info": course_info})
    # except:
    #     pass


def course_detail(request, pk=None,course_name=None):
    try:
        selected_language = translation.get_language()  # Gets the current selected language
        if request.method == 'GET':

            academic_info_detail = Course_Translation.objects.\
                                   filter(website_language__language=selected_language).\
                                    filter(course__pk=pk)

            if not academic_info_detail:
                academic_info_detail = Course_Translation.objects.\
                                       filter(website_language__language="tr").\
                                        filter(course__name=pk)
                                       # filter(course__name=course_name)

            return render(request,
                          "course_detail.html",
                          {"academic_info_detail": academic_info_detail})
    except:
        pass

def conference_page(request):

        if request.method == 'GET':
            academic_life = Conference.objects.all()

            return render(request, "conferences.html",
                          {"base_academic_life": "base_academic_life.html",
                           "academic_life": academic_life})
    # except:
    #     pass

def supervised_thesis_page(request):

        if request.method == 'GET':
            academic_life = Supervised_Thesis.objects.all()

            return render(request, "supervised_thesis.html",
                          {"base_academic_life": "base_academic_life.html",
                           "academic_life": academic_life})
    # except:
    #     pass

def thesis_jury_membership_page(request):

        if request.method == 'GET':
            academic_life = Thesis_Jury_Membership.objects.all()

            return render(request, "thesis_jury_membership.html",
                          {"base_academic_life": "base_academic_life.html",
                           "academic_life": academic_life})
    # except:
    #     pass