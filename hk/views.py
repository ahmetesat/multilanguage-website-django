from django.shortcuts import render, redirect, render_to_response
from django.utils import translation
from django.core.mail import send_mail, EmailMessage, BadHeaderError
import logging
from django.db.models import F
from django.conf import settings

from hk.models import *
from hk.forms import ContactForm
from django.template import RequestContext

from django.template import Template, Context, loader
# Create your views here.

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def error_handler403(request, exception, template_name='403.html'):
    response = render(request, "403.html", {})
    response.status_code = 403
    return response


def error_handler404(request, exception, template_name='404.html'):
    response = render(request, "404.html", {})
    response.status_code = 404
    return response


def error_handler500(request, exception, template_name='404.html'):
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
            author_info = About_Translation.objects.filter(website_language__language=selected_language)
            if not author_info:
                author_info = About_Translation.objects.filter(website_language__language="tr")
            return render(request, "about.html",
                          {"author_info": author_info})
    except:
        pass


def article_page(request):
    try:
        selected_language = translation.get_language()  # Gets the current selected language

        if request.method == 'GET':
            article_info = Article_Translation.objects.filter(website_language__language=selected_language) \
                .annotate(pub_year=F("article__pub_year"),
                          article_language=F("article__article_language__language"),
                          pk=F("article__pk")) \
                .values("pk", "name", "pub_year", "article_language")
            if not article_info:
                article_info = Article_Translation.objects.filter(website_language__language="tr") \
                    .annotate(pub_year=F("article__pub_year"),
                              article_language=F("article__article_language__language")) \
                    .values("article", "name", "pub_year", "article_language")

            return render(request, "articles.html",
                          {"publication_info": article_info})
    except:
        pass


def article_detail(request, pk=None, article_name=None):  # Gets chosen article name and query in database

    try:
        selected_language = translation.get_language()  # Gets the current selected language

        if request.method == 'GET':
            publication_info_detail = Article_Translation.objects. \
                filter(website_language__language=selected_language). \
                filter(article__pk=pk)
            if not publication_info_detail:
                publication_info_detail = Article_Translation.objects.filter(
                    website_language__language="tr").filter(article__pk=pk)

            return render(request, "article_detail.html",
                          {"publication_info_detail": publication_info_detail})
    except:
        pass


def book_page(request):
    try:
        selected_language = translation.get_language()  # Gets the current selected language
        if request.method == 'GET':
            book_info = Book_Translation.objects.filter(website_language__language=selected_language) \
                .annotate(pub_year=F("book__pub_year"),
                          book_language=F("book__book_language__language")) \
                .values("book", "name", "pub_year", "book_language")
            if not book_info:
                book_info = Book_Translation.objects.filter(website_language__language="tr") \
                    .annotate(pub_year=F("book__pub_year"),
                              book_language=F("book__book_language__language")) \
                    .values("book", "name", "pub_year", "book_language")

            return render(request, "books.html",
                          {"publication_info": book_info})
    except:
        pass


def book_detail(request, pk=None, book_name=None):  # Gets chosen article name and query in database

    try:

        selected_language = translation.get_language()  # Gets the current selected language

        if request.method == 'GET':
            publication_info_detail = Book_Translation.objects. \
                filter(website_language__language=selected_language). \
                filter(book__pk=pk)

            if not publication_info_detail:
                publication_info_detail = Book_Translation.objects. \
                    filter(website_language__language="tr").filter(book__pk=pk)

            return render(request, "book_detail.html",
                          {"publication_info_detail": publication_info_detail})

    except:
        pass


def internet_publications(request):
    try:
        if request.method == 'GET':
            publication_info = Internet_Publication.objects.all()

            return render(request, "internet_publications.html",
                          {"publication_info": publication_info})

    except:
        pass


def internet_publication_detail(request, pk=None, internet_pub_artic_name=None):
    if request.method == 'GET':
        publication_info_detail = Internet_Publication.objects.filter(pk=pk)

        return render(request, "internet_publication_detail.html"
                      , {"publication_info_detail": publication_info_detail})


# except:
#     pass


def course_page(request):
    try:
        selected_language = translation.get_language()  # Gets the current selected language
        if request.method == 'GET':
            course_info = Course_Translation.objects.filter(website_language__language=selected_language) \
                .annotate(year=F("course__year")) \
                .values("course", "name", "institution", "year", "course_season")
            if not course_info:
                course_info = Course_Translation.objects.filter(website_language__language="tr") \
                    .annotate(year=F("course__year")) \
                    .values("course", "name", "institution", "year", "course_season")

            return render(request, "courses.html",
                          {"academic_info": course_info})

    except:
        pass


def course_detail(request, pk=None, course_name=None):
    try:
        selected_language = translation.get_language()  # Gets the current selected language
        if request.method == 'GET':

            academic_info_detail = Course_Translation.objects. \
                filter(website_language__language=selected_language). \
                filter(course__pk=pk)

            if not academic_info_detail:
                academic_info_detail = Course_Translation.objects. \
                    filter(website_language__language="tr"). \
                    filter(course__name=pk)

            return render(request,
                          "course_detail.html",
                          {"academic_info_detail": academic_info_detail})
    except:
        pass


def conference_page(request):
    try:
        if request.method == 'GET':
            academic_life = Conference.objects.all()

            return render(request, "conferences.html",
                          {"academic_life": academic_life})

    except:
        pass

def supervised_thesis_page(request):
    if request.method == 'GET':
        academic_life = Supervised_Thesis.objects.all()

        return render(request, "supervised_thesis.html",
                      {"academic_life": academic_life})


# except:
#     pass

def thesis_jury_membership_page(request):
    if request.method == 'GET':
        academic_life = Thesis_Jury_Membership.objects.all()

        return render(request, "thesis_jury_membership.html",
                      {"academic_life": academic_life})


# except:
#     pass


def research_interest_detail(request):
    try:
        selected_language = translation.get_language()  # Gets the current selected language

        if request.method == 'GET':
            research_interest = Research_Interest_Translation.objects.filter(
                website_language__language=selected_language)

            if not research_interest:
                pass

            return render(request, "research_interests.html", {"research_interest": research_interest})

    except:
        pass

def contact(request):
    try:
        return render(request, "contact.html")
    except:
        pass


def contact_send_email(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("form valid")
            full_name = form.cleaned_data['full_name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            subject = "HK Website Contact - %s - %s" % (full_name, from_email)

            try:
                print("33e3e3e")
                email = EmailMessage(subject, message, from_email, ['cphesap@gmail.com'], headers = {'Reply-To': from_email}) #CC ?
                # send() sends the email
                email.send()

                # send_mail(subject, message, from_email, ['cphesap@gmail.com'], headers = {'Reply-To': from_email}) #CC ?
                print(1)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    print(4)
    return redirect('home')
