from django.contrib import admin
from .models import Publisher, Author, Book
from django.contrib.admin.templatetags.admin_list import date_hierarchy

#definition of AuthorAdmin as a ModelAdmin for Author
#specifies admin site related behavior, e.g. which fields should be displayed
#on the Admin interfaces "Change"-site, search bar for fields
class AuthorAdmin(admin.ModelAdmin):
    #tuples of Strings => all relevant fields
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name")
    
    
class BookAdmin(admin.ModelAdmin):
    #tuples of Strings => all relevant fields
    list_display = ("title", "publisher", "publication_date")
    list_filter = ("publication_date",)
    
    #adds a hierarchical date navigation (year -> month -> day)
    #is a String, not a tuple (hierarchy only for a single date)
    date_hierarchy = "publication_date"
    
    #admin-site specific ordering option, here: by publication_date descending
    #is a tuple of Strings (mltpl. fields possible), use '-' to order descending
    ordering = ("-publication_date",)
    
    #defines in which order the fields are displayed in the edit form
    #to exclude fields from being displayed (=> editable) 
    #just let them out of the tuple
    fields = ("title", "authors", "publisher", "publication_date")
    
    #adds an interface with columns "available" and "chosen" authors to select
    #authors in the edit form
    #useful for ManyToMany-Fields with many entries/options
    #DOESN'T WORK WITH ForeignKey-Fields (e.g. "publisher")
    filter_horizontal = ("authors",)
    
    #replaces the default select box with an input field for the publishers DB-id
    #there is a search option next to this field where the publisher can be 
    #selected from the database
    #useful to minimize loading time when the publisher-database gets too big
    raw_id_fields = ("publisher",)
    
        
# Register models (with default admin options)
admin.site.register(Publisher)
#“Register the Author model with the AuthorAdmin options.”
admin.site.register(Author, AuthorAdmin)
#analogous to Author
admin.site.register(Book, BookAdmin)