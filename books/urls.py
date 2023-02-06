from django.urls import path
from .views import BookListView, BookDetailView, AddreviewView, EditReview, ConfirmDeleteReview, DeteleReview
urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:id>/', BookDetailView.as_view(), name='detail'),
    path('<int:id>/reviews/', AddreviewView.as_view(), name='reviews'),
    path('<int:book_id>/reviews/<int:review_id>/edit/', EditReview.as_view(), name='edit_review'),
    path('<int:book_id>/reviews/<int:review_id>/delete/confirm/', ConfirmDeleteReview.as_view(), name='delete_review_confirm'),
    path('<int:book_id>/reviews/<int:review_id>/delete/', DeteleReview.as_view(), name='delete_review'),




]