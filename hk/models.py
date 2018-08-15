from django.db import models
from ckeditor.fields import RichTextField
import datetime


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


class Universities(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name="University Name")

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"


class Content_Language(models.Model):  # Exp. tr, en ..
    language = models.CharField(max_length=10, unique=True, verbose_name="Content Language")

    def __str__(self):
        return "%s" % (self.language)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Content Language"
        verbose_name_plural = "Content Languages"


class Publication_Type(models.Model):
    publication_type = models.CharField(max_length=30, blank=True,
                                        help_text="Ex: Book Chapter, Conferance Paper, ",
                                        verbose_name="Publication Type")  # Publication Type

    def __str__(self):
        return "%s" % (self.publication_type)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Publication Type"
        verbose_name_plural = "Publication Type"


class About(models.Model):
    name = models.CharField(max_length=10, default='Hacı Kara', unique=True)
    section = models.ForeignKey(All_Navbar_Sections, verbose_name="Navbar Section", on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"


class About_Translation(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    language = models.ForeignKey(Content_Language, on_delete=models.CASCADE)
    about_description = RichTextField()

    def __str__(self):
        return "%s" % (self.about.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "About Detail"
        verbose_name_plural = "About Detail"


class Article(models.Model):
    name_bsc = models.CharField(max_length=255, unique=True, verbose_name="Name")  # Name of the article
    author_names = models.ManyToManyField(Authors,
                                          help_text="Choose An Author",
                                          verbose_name="Author Names")  # Author manes
    article_language = models.ForeignKey(Content_Language,
                                         help_text="Article Language",
                                         verbose_name="Content Language",
                                         on_delete=models.CASCADE)  # Article language
    pp = models.CharField(max_length=15,
                          blank=True,
                          help_text="Page Start and Page End(Not Obligatory): Ex:10-20",
                          verbose_name="PP.(Not Obligatory)")

    page_count = models.IntegerField(verbose_name="Page Count",
                                     help_text="Total Page Number")  # How many page is there

    publisher = models.CharField(max_length=255,
                                 help_text="Publisher Name")  # Publisher of the article

    pdf = models.FileField(upload_to='pdf/',
                           help_text="Not Obligatory",
                           verbose_name="PDF(Not Obligatory)",
                           blank=True,
                           max_length=250)

    section = models.ForeignKey(All_Navbar_Sections,
                                verbose_name="Navbar Section",
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
                            verbose_name="Name")  # Name of the course

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    pub_year = models.CharField(max_length=30, blank=True,
                                help_text="Ex:20.05.2018, Spring 2018, 2018 ...",
                                verbose_name="Published Year(Not Obligatory)")  # Publish Year

    publication_type = models.CharField(max_length=17,
                                        help_text="EX: Journal Article",
                                        verbose_name="Publication Type",
                                        choices=Article_Type,
                                        )  # Course language

    website_language = models.ForeignKey(Content_Language,
                                         help_text="Language shown in the website",
                                         verbose_name="Website Language",
                                         on_delete=models.CASCADE)  # website language

    article_abstract = RichTextField()

    def __str__(self):
        return "%s_%s" % (self.name, self.website_language.language)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Article Detail"
        verbose_name_plural = "Articles Details"


class Book(models.Model):
    name_bsc = models.CharField(max_length=255, unique=True, verbose_name="Name")  # Name of the book

    author_names = models.ManyToManyField(Authors,
                                          help_text="Choose An Author",
                                          verbose_name="Author Names")  # Author manes
    book_language = models.ForeignKey(Content_Language,
                                      help_text="Article Language",
                                      verbose_name="Content Language",
                                      on_delete=models.CASCADE)  # Book language
    pp = models.CharField(max_length=15,
                          blank=True,
                          help_text="Page Start and Page End(Not Obligatory): Ex:10-20",
                          verbose_name="PP.(Not Obligatory)")

    page_count = models.IntegerField(verbose_name="Page Count",
                                     help_text="Total Page Number")  # How many page is there

    publisher = models.CharField(max_length=255,
                                 help_text="Publisher Name")  # Publisher of the book

    section = models.ForeignKey(All_Navbar_Sections,
                                verbose_name="Navbar Section",
                                on_delete=models.CASCADE)

    pdf = models.FileField(upload_to='pdf/',
                           help_text="Not Obligatory",
                           verbose_name="PDF(Not Obligatory)",
                           blank=True,
                           max_length=250)

    # tags =

    def __str__(self):
        return "%s" % (self.name_bsc)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Book_Translation(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="Name")  # Name of the course

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    pub_year = models.CharField(max_length=30, blank=True,
                                help_text="Ex:20.05.2018, Spring 2018, 2018 ...",
                                verbose_name="Published Year(Not Obligatory)")  # Publish Year

    website_language = models.ForeignKey(Content_Language,
                                         help_text="Language shown in the website",
                                         verbose_name="Website Language",
                                         on_delete=models.CASCADE)  # website language

    book_abstract = RichTextField()

    def __str__(self):
        return "%s_%s" % (self.name, self.website_language.language)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Book Detail"
        verbose_name_plural = "Books Details"


class Course(models.Model):
    name_bsc = models.CharField(max_length=255, unique=True,
                                verbose_name="Name")  # Name of the course

    course_code = models.CharField(max_length=10,
                                   blank=True,
                                   verbose_name="Course Code")  # Course code

    course_language = models.ForeignKey(Content_Language,
                                        help_text="Course Language",
                                        verbose_name="Course Language",
                                        on_delete=models.CASCADE)  # Course language

    section = models.ForeignKey(All_Navbar_Sections,
                                verbose_name="Navbar Section",
                                on_delete=models.CASCADE)

    # pdf = models.FileField(upload_to='pdf/',
    #                        help_text="Not Obligatory",
    #                        verbose_name="PDF(Not Obligatory)",
    #                        blank=True,
    #                        max_length=250)

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
                            verbose_name="Name")  # Name of the course
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    university = models.ForeignKey(Universities,
                                   verbose_name="University",
                                   on_delete=models.CASCADE)  # University name that is given course

    department = models.CharField(max_length=255,
                                  verbose_name="Course department",
                                  blank=True,
                                  help_text="EX: Department of Law,"
                                            "Course For Lawyers")  # Course department or for who

    course_season = models.CharField(max_length=12,
                                     help_text="EX: Autumn, Winter ...",
                                     verbose_name="Course Season",
                                     choices=Season_Choice,
                                     default='Autumn')  # Course language

    year = models.IntegerField(verbose_name="Course year",
                               help_text="EX: 2018")  # Course department or for who

    website_language = models.ForeignKey(Content_Language,
                                         help_text="Language shown in the website",
                                         verbose_name="Website Language",
                                         related_name="Website_Language_Content_Language",
                                         on_delete=models.CASCADE)  # website language

    course_abstract = RichTextField()

    def __str__(self):
        return "%s_%s" % (self.name, self.website_language.language)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Course Details"
        verbose_name_plural = "Courses Details"


class Conference(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Name")  # Name of the conference

    location = models.CharField(
        max_length=255,
        verbose_name="Conference Location")  # Conference Location

    conference_link = models.URLField(
        max_length=128,
        db_index=True,
        unique=True,
        blank=True
    )  # Conference Link
    date = models.DateField(default=datetime.date.today)  # Conference Date

    poster = models.ImageField(upload_to='img/', blank=True)  # Conference Poster

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Conference"
        verbose_name_plural = "Conferences"


class Internet_Publication(models.Model):
    name = models.CharField(max_length=255,
                            help_text="Article Title",
                            verbose_name="Article Title")  # Name of the Internet_Publications
    author_names = models.ManyToManyField(Authors,
                                          help_text="Choose An Author",
                                          verbose_name="Author Names")  # Author names

    internet_article_date = models.DateField()

    website_name = models.CharField(max_length=255,
                                    blank=True,
                                    help_text="Website Name",
                                    verbose_name="Website Name")
    website_link = models.URLField(
        max_length=128,
        db_index=True,
        unique=True,
        blank=True,
        help_text="Website Link",
        verbose_name="Website Link"
    )
    article_content = RichTextField()

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object


class Supervised_Thesis(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Thesis Name")  # Name of the thesis

    thesis_owner = models.CharField(
        max_length=40,
        verbose_name="Thesis Owner Name")  # Name of the thesis

    year = models.CharField(
        max_length=20,
        help_text="EX: 2018, 2015 - 2018",
        verbose_name="Thesis Year/'s")  # Year of the thesis

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
        verbose_name="Thesis Name")  # Name of the thesis

    thesis_owner = models.CharField(
        max_length=40,
        verbose_name="Thesis Owner Name")  # Name of the thesis

    date = models.DateField(default=datetime.date.today)

    thesis_degree = models.CharField(max_length=12, choices=DEGREE_CHOICES, default='MA')

    def __str__(self):
        return "%s" % (self.name)  # In Admin Page see the name itself not as object

    class Meta:
        verbose_name = "Thesis Jury Membership"
        verbose_name_plural = "Thesis Jury Membership"
