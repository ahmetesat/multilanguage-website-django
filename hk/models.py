from django.db import models
from django.utils import translation
from django.urls import reverse
from django.core.validators import FileExtensionValidator
import datetime

from ckeditor.fields import RichTextField
from hk.templatetags import custom_tags

selected_language = translation.get_language()


class All_Navbar_Sections(models.Model):  # Keeps the main navbar sections names
    name = models.CharField(max_length=25, unique=True, verbose_name="All Navbar Sections Name")

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "All Navbar"
        verbose_name_plural = "All Navbars"


class Authors(models.Model):
    name = models.CharField(max_length=25, default='Hacı Kara', unique=True, verbose_name="Author Name")

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Institution(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            default="Istanbul Medeniyet University",
                            verbose_name="Instituon Name")

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"


class Content_Language(models.Model):  # Exp. tr, en ..
    language = models.CharField(max_length=10, default="tr", unique=True, verbose_name="Content Language")

    def __str__(self):
        return "%s" % (self.language)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Content Language"
        verbose_name_plural = "Content Languages"


class About(models.Model):
    name = models.CharField(max_length=10, default='Hacı Kara', unique=True)
    section = models.ForeignKey(All_Navbar_Sections,
                                verbose_name="Navbar Section*",
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/%Y/%m/%d', blank=True, help_text="Not Obligatory", )

    def get_absolute_url(self):
        return reverse('About')

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"


class About_Translation(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    website_language = models.ForeignKey(Content_Language,
                                         help_text="Language shown in the website",
                                         verbose_name="Website Language*",
                                         default=0,  # Default is tr
                                         on_delete=models.CASCADE)
    about_description = RichTextField(blank=True, null=True,
                                      help_text="About Description (Not Obligatory)",
                                      verbose_name="About Description")
    pdf = models.FileField(upload_to='pdf/%Y/%m/%d',
                           help_text="CV PDF (Not Obligatory)",
                           verbose_name="PDF",
                           blank=True,
                           validators=[FileExtensionValidator(["pdf"])],
                           max_length=250)

    def __str__(self):
        return "%s" % (self.about.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "About Detail"
        verbose_name_plural = "About Detail"


class Article(models.Model):
    name_bsc = models.CharField(max_length=255, unique=True, verbose_name="Article Name*")  # Name of the article
    author_names = models.ManyToManyField(Authors,
                                          help_text="Choose An Author",
                                          verbose_name="Author Names*")  # Author manes
    article_language = models.ForeignKey(Content_Language,
                                         help_text="Article Language",
                                         verbose_name="Content Language*",
                                         default=0,  # Default is tr
                                         on_delete=models.CASCADE)  # Article language
    pub_year = models.DateField(default=datetime.date.today,
                                help_text="Ex: June 2018",
                                verbose_name="Published Year*")  # Publish Year)  # Conference Date
    pp = models.CharField(max_length=15,
                          blank=True,
                          help_text="Page Start and Page End: Ex:10-20 (Not Obligatory)",
                          verbose_name="PP.")
    volume = models.IntegerField(blank=True,
                                 null=True,
                                 help_text="Cilt no - Ex: 7 (Not Obligatory)",
                                 verbose_name="Volume")
    issue = models.IntegerField(blank=True,
                                null=True,
                                help_text="Sayı - Ex: 52 (Not Obligatory)",
                                verbose_name="Issue")
    page_count = models.IntegerField(verbose_name="Page Count",
                                     blank=True,
                                     null=True,
                                     help_text="Total Page Number (Not Obligatory)")  # How many page is there
    journal_title = models.CharField(max_length=255,
                                     help_text="Journal Title*",
                                     verbose_name="Journal Title")  # Publisher of the article

    publisher = models.CharField(max_length=255,
                                 blank=True,
                                 help_text="Publisher Name (Not Obligatory)",
                                 verbose_name="Publisher", )  # Publisher of the article

    pdf = models.FileField(upload_to='pdf/%Y/%m/%d',
                           help_text="Article PDF (Not Obligatory)",
                           verbose_name="PDF",
                           blank=True,
                           validators=[FileExtensionValidator(["pdf"])],
                           max_length=250)

    section = models.ForeignKey(All_Navbar_Sections,
                                verbose_name="Navbar Section*",
                                on_delete=models.CASCADE)

    # tags =

    def __str__(self):
        return "%s" % (self.name_bsc)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Article_Translation(models.Model):
    Article_Type = (
        ('Dergi Makalesi', 'Dergi Makalesi'),
        ('Journal Article', 'Journal Article'),
        ('Kitap Bölümü', 'Kitap Bölümü'),
        ('Book Chapter', 'Book Chapter')
    )
    name = models.CharField(max_length=255,
                            verbose_name="Article Name*")  # Name of the article

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    publication_type = models.CharField(max_length=17,
                                        help_text="EX: Journal Article",
                                        verbose_name="Publication Type*",
                                        choices=Article_Type,
                                        )

    website_language = models.ForeignKey(Content_Language,
                                         help_text="Language shown in the website",
                                         verbose_name="Website Language*",
                                         default=0,  # Default is tr
                                         on_delete=models.CASCADE)  # website language

    article_abstract = RichTextField(blank=True, null=True)

    def __str__(self):
        return "%s_%s" % (
            self.article.name_bsc, self.website_language.language)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Article Detail"
        verbose_name_plural = "Articles Details"

    def get_absolute_url(self):
        return reverse('Article_Detail',
                       kwargs={'pk': self.article.pk, 'article_name': custom_tags.slugify2(self.name)})


class Book(models.Model):
    name_bsc = models.CharField(max_length=255, unique=True, verbose_name="Name*")  # Name of the book

    author_names = models.ManyToManyField(Authors,
                                          help_text="Choose An Author*",
                                          verbose_name="Author Names*")  # Author manes
    book_language = models.ForeignKey(Content_Language,
                                      help_text="Article Language*",
                                      verbose_name="Content Language",
                                      default=0,  # Default is tr
                                      on_delete=models.CASCADE)  # Book language

    pub_year = models.DateField(default=datetime.date.today,
                                help_text="Ex: June 2018*",
                                verbose_name="Published Year")  # Publish Year

    isbn = models.CharField(max_length=20,
                            blank=True,
                            help_text="ISBN number EX: 978-975-17-3133-3 (Not Obligatory)",
                            verbose_name="ISBN number")

    page_count = models.IntegerField(verbose_name="Page Count*",
                                     help_text="Total Page Number")  # How many page is there

    publisher = models.CharField(max_length=255,
                                 blank=True,
                                 help_text="Publisher Name (Not Obligatory)",
                                 verbose_name="Publisher")  # Publisher of the book

    section = models.ForeignKey(All_Navbar_Sections,
                                verbose_name="Navbar Section*",
                                on_delete=models.CASCADE)

    pdf = models.FileField(upload_to='pdf/%Y/%m/%d',
                           help_text="Book PDF (Not Obligatory)",
                           verbose_name="PDF",
                           validators=[FileExtensionValidator(["pdf"])],
                           blank=True)

    # tags =

    def __str__(self):
        return "%s" % (self.name_bsc)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Book_Translation(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="Name*")  # Name of the book

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    website_language = models.ForeignKey(Content_Language,
                                         help_text="Language shown in the website",
                                         verbose_name="Website Language*",
                                         default=0,  # Default is tr
                                         on_delete=models.CASCADE)  # website language

    book_abstract = RichTextField(blank=True, null=True)

    def __str__(self):
        return "%s_%s" % (self.name, self.website_language.language)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Book Detail"
        verbose_name_plural = "Books Details"

    def get_absolute_url(self):
        return reverse('Book_Detail', kwargs={'pk': self.book.pk, 'book_name': custom_tags.slugify2(self.name)})


class Course(models.Model):
    name_bsc = models.CharField(max_length=255, unique=True,
                                verbose_name="Name*")  # Name of the course

    course_code = models.CharField(max_length=10,
                                   blank=True,
                                   help_text="Ex: Huk 101 (Not Obligatory)",
                                   verbose_name="Course Code")  # Course code

    year = models.DateField(default=datetime.date.today,
                            help_text="Ex: 2018(Only year will be visible)",
                            verbose_name="Course Year*")  # Publish Year)  # Conference Date

    course_language = models.ForeignKey(Content_Language,
                                        help_text="Course Language",
                                        verbose_name="Course Language*",
                                        default=0,  # Default is tr
                                        on_delete=models.CASCADE)  # Course language

    section = models.ForeignKey(All_Navbar_Sections,
                                verbose_name="Navbar Section*",
                                on_delete=models.CASCADE)

    pdf = models.FileField(upload_to='pdf/%Y/%m/%d',
                           help_text="(Not Obligatory)",
                           verbose_name="Course PDF",
                           blank=True,
                           validators=[FileExtensionValidator(["pdf"])],
                           max_length=250)

    def __str__(self):
        return "%s" % (self.name_bsc)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Course_Translation(models.Model):
    Season_Choice = (
        ('Sonbahar', 'Sonbahar'),
        ('Autumn', 'Autumn'),
        ('Kış', 'Kış'),
        ('Winter', 'Winter'),
        ('İlkbahar', 'İlkbahar'),
        ('Spring', 'Spring'),
        ('Yaz', 'Yaz'),
        ('Summer', 'Summer'),
    )
    name = models.CharField(max_length=255,
                            verbose_name="Name*")  # Name of the course
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    course_season = models.CharField(max_length=12,
                                     help_text="EX: Sonbahar",
                                     verbose_name="Course Season*",
                                     choices=Season_Choice,
                                     default='Sonbahar')  # Course language

    institution = models.ForeignKey(Institution,
                                    verbose_name="Institution*",
                                    help_text="EX: Medeniyet University",
                                    default=0,
                                    on_delete=models.CASCADE)

    department = models.CharField(max_length=255,
                                  verbose_name="Course department",
                                  blank=True,
                                  help_text="EX: Department of Law,"
                                            "Course For Lawyers (Not Obligatory)")  # Course department or for who

    website_language = models.ForeignKey(Content_Language,
                                         help_text="Language shown in the website",
                                         verbose_name="Website Language*",
                                         default=0,  # Default is tr
                                         on_delete=models.CASCADE)  # website language

    course_abstract = RichTextField(blank=True, null=True)

    def __str__(self):
        return "%s_%s" % (self.name, self.website_language.language)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Course Details"
        verbose_name_plural = "Courses Details"

    def get_absolute_url(self):
        return reverse('Course_Detail', kwargs={'pk': self.course.pk, 'course_name': custom_tags.slugify2(self.name)})


class Conference(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Conferance Name")  # Name of the conference

    participants = models.ManyToManyField(Authors,
                                          help_text="Choose An Participant",
                                          verbose_name="Participant Names*")  # Author manes

    institution = models.ForeignKey(Institution,
                                    verbose_name="Institution*",
                                    help_text="EX: Medeniyet University",
                                    default=0,
                                    on_delete=models.CASCADE)

    conference_link = models.URLField(
        blank=True,
        help_text="Conference Link (Not Obligatory)",
        verbose_name="Conference Link")
    date = models.DateField(default=datetime.date.today)  # Conference Date
    conference_abstract = RichTextField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Conference"
        verbose_name_plural = "Conferences"


class Internet_Publication(models.Model):
    name = models.CharField(max_length=255,
                            help_text="Article Title",
                            verbose_name="Article Title*")  # Name of the Internet_Publications
    author_names = models.ManyToManyField(Authors,
                                          help_text="Choose An Author",
                                          verbose_name="Author Names*")  # Author names

    internet_article_date = models.DateField(default=datetime.date.today)

    website_name = models.CharField(max_length=255,
                                    blank=True,
                                    help_text="Website Name",
                                    verbose_name="Website Name")
    website_link = models.URLField(
        max_length=128,
        blank=True,
        help_text="Website Link",
        verbose_name="Website Link"
    )
    article_content = RichTextField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Internet Publication"
        verbose_name_plural = "Internet Publications"

    def get_absolute_url(self):
        # NOT: Internet_Publication_Detail should be same in url. This is important for sitemap
        return reverse('Internet_Publication_Detail',
                       kwargs={'pk': self.pk, 'internet_pub_artic_name': custom_tags.slugify2(self.name)})


class Supervised_Thesis(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Thesis Name*")  # Name of the thesis

    thesis_owner = models.CharField(
        max_length=40,
        verbose_name="Thesis Owner Name*")  # Name of the thesis
    start_date = models.DateField(default=datetime.date.today, verbose_name="Start Date*")
    end_date = models.DateField(default=datetime.date.today, verbose_name="End Date*")

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Supervised Thesis"
        verbose_name_plural = "Supervised Thesis"


class Thesis_Jury_Membership(models.Model):
    DEGREE_CHOICES = (
        ('MA', 'MA'),
        ('Phd.', 'Phd.'),
        ('Assoc. Prof.', 'Assoc. Prof.'),
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Thesis Name*")  # Name of the thesis

    thesis_owner = models.CharField(
        max_length=40,
        verbose_name="Thesis Owner Name*")  # Name of the thesis

    date = models.DateField(default=datetime.date.today, verbose_name="Date*")

    thesis_degree = models.CharField(max_length=12, choices=DEGREE_CHOICES, default='MA',
                                     verbose_name="Thesis Degree*")

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Thesis Jury Membership"
        verbose_name_plural = "Thesis Jury Membership"


class Research_Interest(models.Model):
    name_base = models.CharField(max_length=255, unique=True,
                                 help_text="Base interest",
                                 verbose_name="Name*",
                                 default="Base")  # Name of the interest

    def __str__(self):
        return "%s" % (self.name_base)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Research Interest"
        verbose_name_plural = "Research Interest"


class Research_Interest_Translation(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            help_text="Base interest",
                            verbose_name="Name*",
                            default="Research_Interest_tr")  # Name of the interest

    research_interest = models.ForeignKey(Research_Interest,
                                          verbose_name="Research Interest*",
                                          help_text="EX: Write All Research Interests",
                                          on_delete=models.CASCADE)

    website_language = models.ForeignKey(Content_Language,
                                         help_text="Language shown in the website",
                                         verbose_name="Website Language*",
                                         default=0,  # Default is tr
                                         on_delete=models.CASCADE)  # website language

    research_interest_content = RichTextField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Research Interest Detail"
        verbose_name_plural = "Research Interests Details"
