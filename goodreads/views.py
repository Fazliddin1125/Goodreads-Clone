from django.shortcuts import render
from django.views import View
from books.models import BookReview
from django.core.paginator import Paginator

def landing_page(requset):
    return render(requset, 'landing_page.html')

# def home_page(request):
#     return render(request, 'home.html')

class HomePageView(View):
    def get(self, request):
        reviews = BookReview.objects.all().order_by('-create_at')
        page_size = request.GET.get('page_size', 10)
        padinator = Paginator(reviews, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = padinator.get_page(page_num)
        return render(request, 'home.html', {'page_obj': page_obj})

