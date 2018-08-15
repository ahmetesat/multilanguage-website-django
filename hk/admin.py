from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import *
# Register your models here.

class AllNavbarSectionsAdmin(admin.ModelAdmin):
    pass
admin.site.register(All_Navbar_Sections, AllNavbarSectionsAdmin)

class AuthorsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Authors,AuthorsAdmin)

class UniversitiesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Universities,AuthorsAdmin)

class ContentLanguageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Content_Language,ContentLanguageAdmin)

class Publication_TypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Publication_Type, Publication_TypeAdmin)

class AboutAdmin(admin.ModelAdmin):
    pass
admin.site.register(About,AboutAdmin)

class AboutTranslationAdmin(admin.ModelAdmin):
    pass
admin.site.register(About_Translation,AboutTranslationAdmin)

class ArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article, ArticleAdmin)

class ArticleTranslationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article_Translation, ArticleTranslationAdmin)

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)

class BookTranslationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book_Translation, BookTranslationAdmin)

class InternetPublicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Internet_Publication, InternetPublicationAdmin)

class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)

class CourseTranslationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course_Translation, CourseTranslationAdmin)

class ConferenceTranslationAdmin(admin.ModelAdmin):
    model = Conference
    list_display = ["name", "date"]
    # ordering = ('-date')
admin.site.register(Conference, ConferenceTranslationAdmin)

class SupervisedThesisTranslationAdmin(admin.ModelAdmin):
    model = Supervised_Thesis
    list_display = ["name", "thesis_owner"]
admin.site.register(Supervised_Thesis, SupervisedThesisTranslationAdmin)

class ThesisJuryMembershipTranslationAdmin(admin.ModelAdmin):
    model = Thesis_Jury_Membership
    list_display = ["name", "date"]
    # ordering = ('-date')
admin.site.register(Thesis_Jury_Membership, SupervisedThesisTranslationAdmin)





