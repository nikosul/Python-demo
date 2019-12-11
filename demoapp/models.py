from django.db import models

# Book object
class Book(models.Model):
  book_name = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

# define string
def __str__(self):
  return self.book_name

# Book details
class Details(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  details_text = models.CharField(max_length=200)

# define string
def __str__(self):
  return self.details_text