from django.contrib import admin
import datetime
from .models import *
# Register your models here.

class AllNavbarSectionsAdmin(admin.ModelAdmin):
    pass
admin.site.register(All_Navbar_Sections, AllNavbarSectionsAdmin)

class AuthorsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Authors,AuthorsAdmin)

class InstitutionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Institution,InstitutionAdmin)

class ContentLanguageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Content_Language,ContentLanguageAdmin)

class AboutAdmin(admin.ModelAdmin):
    pass
admin.site.register(About,AboutAdmin)

class AboutTranslationAdmin(admin.ModelAdmin):
    list_display = ['_name']

    def _name(self,obj):
        return "%s_%s" % (obj.about.name, obj.website_language)

    _name.short_description = 'ABOUT NAME'
admin.site.register(About_Translation,AboutTranslationAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['_name', '_year']
    search_fields = ['_name']
    ordering = ['name_bsc']

    def _name(self,obj):
        return "%s" % (obj.name_bsc)

    def _year(self, obj):
        return obj.pub_year.year

    _name.short_description = 'ARTICLE NAME'
    _year.short_description = 'PUBLICATION YEAR'
admin.site.register(Article, ArticleAdmin)

class ArticleTranslationAdmin(admin.ModelAdmin):
    list_display = ['special_name','_name', '_year']
    search_fields = ['article__name_bsc']
    ordering = ['article__name_bsc', 'website_language']

    def _name(self,obj):
        return "%s" % (obj.name)

    def special_name(self,obj):
        return "%s_%s" % (obj.article.name_bsc, obj.website_language.language)

    def _year(self,obj):
        return obj.article.pub_year.year

    special_name.short_description = 'SPECIAL NAME'
    _name.short_description = 'ARTICLE NAME'
    _year.short_description = 'PUBLICATION YEAR'
admin.site.register(Article_Translation, ArticleTranslationAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['_name', '_year']
    search_fields = ['name_bsc']
    ordering = ['name_bsc']

    def _name(self, obj):
        return "%s" % (obj.name_bsc)

    def _year(self,obj):
        return obj.pub_year.year

    _name.short_description = 'BOOK NAME'
    _year.short_description = 'PUBLICATION YEAR'
admin.site.register(Book, BookAdmin)

class BookTranslationAdmin(admin.ModelAdmin):
    list_display = ['special_name', '_name', '_year']
    search_fields = ['book__name_bsc']
    ordering = ['book__name_bsc', 'website_language']

    def _name(self, obj):
        return "%s" % (obj.name)

    def special_name(self, obj):
        return "%s_%s" % (obj.book.name_bsc, obj.website_language.language)

    def _year(self,obj):
        return obj.book.pub_year.year

    special_name.short_description = 'SPECIAL NAME'
    _name.short_description = 'BOOK NAME'
    _year.short_description = 'PUBLICATION YEAR'
admin.site.register(Book_Translation, BookTranslationAdmin)

class InternetPublicationAdmin(admin.ModelAdmin):
    list_display = ['_name', '_internet_article_date']
    search_fields = ['name']
    ordering = ['name', 'internet_article_date']

    def _name(self, obj):
        return "%s" % (obj.name)

    def _internet_article_date(self, obj):
        return obj.internet_article_date

    _name.short_description = 'ARTICLE NAME'
    _internet_article_date.short_description = 'PUBLICATION YEAR'
admin.site.register(Internet_Publication, InternetPublicationAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['_name', '_year']
    search_fields = ['course__name_bsc']
    ordering = ['name_bsc']

    def _name(self, obj):
        return "%s" % (obj.name_bsc)

    def _year(self,obj):
        return obj.year.year

    _name.short_description = 'COURSE NAME'
    _year.short_description = 'COURSE YEAR'
admin.site.register(Course, CourseAdmin)

class CourseTranslationAdmin(admin.ModelAdmin):
    list_display = ['special_name', '_name','_year']
    search_fields = ['course__name_bsc']
    ordering = ['course__name_bsc', 'website_language']

    def _name(self, obj):
        return "%s" % (obj.name)

    def special_name(self, obj):
        return "%s_%s" % (obj.course.name_bsc, obj.website_language.language)

    def _year(self,obj):
        return obj.course.year.year

    special_name.short_description = 'SPECIAL NAME'
    _name.short_description = 'COURSE NAME'
    _year.short_description = 'COURSE YEAR'
admin.site.register(Course_Translation, CourseTranslationAdmin)

class ConferenceTranslationAdmin(admin.ModelAdmin):
    list_display = ["_name", "date"]
    search_fields = ['name']
    ordering = ['name']

    def _name(self, obj):
        return "%s" % (obj.name)

    _name.short_description = 'CONFERENCE NAME'
admin.site.register(Conference, ConferenceTranslationAdmin)

class SupervisedThesisTranslationAdmin(admin.ModelAdmin):
    list_display = ["_name", "_owner_name", '_year']
    search_fields = ['name']
    ordering = ['name']

    def _name(self, obj):
        return "%s" % (obj.name)

    def _owner_name(self, obj):
        return "%s" % (obj.thesis_owner)

    def _year(self,obj):
        return "%d - %d" % (obj.start_date.year, obj.end_date.year)

    _year.short_description = 'SUPERVISED THESIS YEAR'
    _name.short_description = 'THESIS OWNER NAME'
    _name.short_description = 'THESIS NAME'
admin.site.register(Supervised_Thesis, SupervisedThesisTranslationAdmin)

class ThesisJuryMembershipTranslationAdmin(admin.ModelAdmin):
    list_display = ["_name", "date"]
    ordering = ['name']

    def _name(self, obj):
        return "%s" % (obj.name)

    _name.short_description = 'THESIS NAME'
admin.site.register(Thesis_Jury_Membership, ThesisJuryMembershipTranslationAdmin)

class ResearchInterestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Research_Interest, ResearchInterestAdmin)

class ResearchInterestTranslationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Research_Interest_Translation, ResearchInterestTranslationAdmin)



