from django.urls import path
from . import views


app_name = 'Catalog'
urlpatterns = [
    # path('', views.catalog_page, name='catalog_page'),
    # path('product/<int:category_id>/', views.product_page, name='product_page'),
    # path('upload_category/', views.upload_category, name='upload_category'),
    # path('update_category/<int:category_id>', views.update_category, name='update_category'),
    # path('delete_category/<int:category_id>', views.delete_category, name='delete_category'),
    # path('upload_product/', views.upload_product, name='upload_product'),
    # path('update_product/<int:product_id>', views.update_book, name='update_product'),
    # path('delete_product/<int:product_id>', views.delete_book, name='delete_product'),

    path('', views.homepage, name='homepage'),
    path('Category', views.CategoryListView.as_view(), name='catalog_page'),
    path('upload_category/', views.CategoryUploadView.as_view(), name='upload_category'),
    path('update_category/<int:pk>', views.CategoryUpdateView.as_view(), name='update_category'),
    path('delete_category/<int:pk>', views.CategoryDeleteView.as_view(), name='delete_category'),
    path('book/<int:pk>/', views.CategoryDetailView.as_view(), name='book_page'),         # Category.id
    path('upload_book/', views.BookUploadView.as_view(), name='upload_book'),
    path('update_book/<int:pk>', views.BookUpdateView.as_view(), name='update_book'),
    path('delete_book/<int:pk>', views.BookDeleteView.as_view(), name='delete_book'),
    path('borrowed_book/', views.LoanedBooksByUserView.as_view(), name='borrowed_book'),
]




