from django.contrib import admin
from .models import Book, BookAuthor, BookReview, Author
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    list_display = ('title', 'isbn')


admin.site.register(Book, BookAdmin)
admin.site.register(BookReview)
admin.site.register(BookAuthor)
admin.site.register(Author)