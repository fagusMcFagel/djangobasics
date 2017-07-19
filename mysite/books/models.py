from django.db import models

#defines the data structure for Publisher which will be created 
#analogously as a table in the database
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    
    #method which returns the "human readable presentation" of a Publisher object
    def __str__(self):
        return self.name
    
    #class in Publisher which is used to specify model-specific options
    #e.g. by which value query results should be ordered
    class Meta:
        ordering = ["name"]

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    
    #"blank=True" specifies the field as optional; default:blank=False 
    #no update needed
    #verbose_name: specify the label shown on the admin site
    email = models.EmailField(blank=True, verbose_name="E-Mail")
    
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    
    #analogous to blank: "null=True"; used for e.g. DateField, IntegerField,...
    #update necessary (makemigrations -> migrate)
    publication_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title