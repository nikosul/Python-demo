from django.contrib import admin
from .models import Book, Details

admin.site.site_header = 'Python demoapp'
admin.site.site_title = 'Adminpage'
admin.site.index_title = 'Django db'

# Book details field with Extra 3 inputs
class DetailsInLine(admin.TabularInline):
  model = Details
  extra = 3

# Book object with details and date info
class BookAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields': ['book_name']}),
  ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
  inlines = [DetailsInLine]

# Both classes in adminpage
admin.site.register(Book, BookAdmin)