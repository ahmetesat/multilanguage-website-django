from django.contrib.sitemaps import Sitemap
from hk.models import *
from hk.templatetags import custom_tags
# class ArticleSitemap(Sitemap):
#     changefreq = "monthly"
#     priority = 1.0
#     i18n=True
#
#     def items(self):
#         return Article.objects.all()
#
#     def load(self,obj):
#         return obj.name
from hk.views import internet_publications


class ArticleDetailSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0
    i18n = True

    def items(self):
        current_lang_code = translation.get_language()

        return Article_Translation.objects\
            .filter(website_language__language=current_lang_code)

    def load(self, obj):
        return obj.name

class BookDetailSitemap(Sitemap):
    changefreq = "never"
    priority = 1.0
    i18n = True

    def items(self):
        current_lang_code = translation.get_language()
        try:

            return Book_Translation.objects\
                .filter(website_language__language=current_lang_code)
        except:
            pass
    def load(self, obj):
        return obj.name

class InternetPubDetailSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0
    i18n = True

    def items(self):
        try:
            return Internet_Publication.objects.all()
        except:
            pass
    def load(self, obj):
        return obj.name

class CourseDetailSitemap(Sitemap):
    changefreq = "never"
    priority = 1.0
    i18n = True

    def items(self):
        current_lang_code = translation.get_language()
        try:
            return Course_Translation.objects\
                .filter(website_language__language=current_lang_code)
        except:
            pass
    def load(self, obj):
        return obj.name


class StaticSitemapHighImportance(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "monthly"
    priority = 1.0
    i18n = True

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['Articles',
                'Books',
                'Courses',
                'Conferences',
                'Internet_Publications']

    def location(self, item):
        return reverse(item)


class StaticSitemapMiddleImportance(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "monthly"
    priority = 0.5
    i18n = True

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['About',
                'research_interest_detail',
                'Supervised_Thesis',
                'Thesis_Jury_Membership',
                'home']

    def location(self, item):
        return reverse(item)


class StaticSitemapLowImportance(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "never"
    priority = 0.1
    i18n = True

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['Contact']

    def location(self, item):
        return reverse(item)


