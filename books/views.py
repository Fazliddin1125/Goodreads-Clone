from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import BookReviewForm
from .models import Book, BookAuthor, BookReview
from django.contrib.auth.mixins import LoginRequiredMixin




# class BookListView(ListView):
#     template_name = "books/list.html"
#     queryset = Book.objects.all()
#     context_object_name = "books"
#     paginate_by = 4

class BookListView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q', '')

        if search_query:
            search = books.filter(title__icontains=search_query)
            if search:
                books = search
            else:
                books = Book.objects.all().order_by('id')
                messages.info(request, f"{search_query} not found")

        padinator = Paginator(books, 4)
        page_name = request.GET.get('page', 1)
        page_obj = padinator.get_page(page_name)

        return render(request, 'books/list.html', {'page_obj': page_obj, 'search_query': search_query})

class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        autho = (BookAuthor.objects.filter(book=book))

        review_form = BookReviewForm()

        return render(request, 'books/detail.html', {'book': book, 'author': autho, 'review_form': review_form})

class AddreviewView(LoginRequiredMixin, View):
    def post(self, request, id):

        book = Book.objects.get(id=id)
        autho = (BookAuthor.objects.filter(book=book))
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment']
            )

            return redirect(reverse('detail', kwargs={'id': book.id}))

        return render(request, 'books/detail.html', {'book': book, 'author': autho, 'review_form': review_form})

class EditReview(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review)
        return render(request, 'books/edit_review.html', {'book': book, 'review': review, 'review_form': review_form})
    def post(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review, data=request.POST)

        if review_form.is_valid():
            review_form.save()
            return redirect(reverse('detail', kwargs={'id': book.id}))

class ConfirmDeleteReview(View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        return render(request, 'books/confirmreview.html', {'book': book, 'review': review})

class DeteleReview(View):
    def get(self, request, book_id, review_id ):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)

        review.delete()
        messages.success(request, "You have successfuly deleted this review")
        return redirect(reverse('detail', kwargs={'id': book.id}))

