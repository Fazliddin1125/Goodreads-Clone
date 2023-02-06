from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from books.models import BookReview, Book


# Create your views here.

class ReviewAPIView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        book_review = BookReview.objects.get(book=book)

        # return JsonResponse(json_response)
        return render(request, 'api/review.html', {'reviews': book_review})
