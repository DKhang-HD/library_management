from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy, reverse
from .models import Category, Book, BookInstance, Author
from .forms import CategoryCreate, BookCreate, BookInstanceCreate, AuthorCreate
from django.core.paginator import Paginator
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# error_class=ErrorListMsg


def homepage(request):
    """View function for home page of site."""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'Catalog/index.html', context=context)


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    # Redirect to setting.LOGIN_URL in default
    # redirect_field_name = reverse_lazy('Catalog:catalog_page')
    permission_required = 'Catalog.view_category'
    model = Category
    paginate_by = 2
    context_object_name = 'list_category'
    template_name = 'Catalog/list_category.html'


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    permission_required = ('Catalog.view_category', 'Catalog.view_product')
    model = Category
    paginate_by = 1
    context_object_name = 'detail_category'
    template_name = 'Catalog/detail_category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        category = self.object
        book_list = category.book_set.all()
        p = Paginator(book_list, self.paginate_by)
        page = self.request.GET.get('page')
        book_per_page = p.get_page(page)
        context['book_per_page'] = book_per_page
        return context


class CategoryUploadView(generic.CreateView):
    model = Category
    form_class = CategoryCreate
    template_name = 'Catalog/upload_category.html'
    success_url = reverse_lazy('Catalog:homepage')


class CategoryUpdateView(generic.UpdateView):
    model = Category
    form_class = CategoryCreate
    template_name = 'Catalog/update_category.html'
    success_url = reverse_lazy('Catalog:catalog_page')


class CategoryDeleteView(generic.DeleteView):
    model = Category
    template_name = 'Catalog/category_confirm_delete.html'
    success_url = reverse_lazy('Catalog:catalog_page')


class BookUploadView(CategoryUploadView):
    model = Book
    form_class = BookCreate

    # def get_success_url(self):
    #     # category = get_object_or_404(Category, pk=self.request.POST['pk'])
    #
    #     return reverse('Catalog:product_page', kwargs={'pk': self.request.POST['pk']})


class BookUpdateView(CategoryUpdateView):
    model = Book
    form_class = BookCreate


class BookDeleteView(CategoryDeleteView):
    model = Book


class LoanedBooksByUserView(LoginRequiredMixin, generic.ListView):

    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 2

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )

# @login_required(redirect_field_name=None)
# @permission_required('Catalog.view_category')
# def catalog_page(request):
#     category_list = Category.objects.all()
#     p = Paginator(category_list, 2)
#     page = request.GET.get('page')
#     category_per_page = p.get_page(page)
#     return render(request, 'Catalog/library.html',
#                   {'category_list': category_list, 'category_per_page': category_per_page})
#
#
# def upload_category(request):
#     if request.method == 'POST':
#         upload_form = CategoryCreate(request.POST, request.FILES)
#         if upload_form.is_valid():
#             upload_form.save()
#             return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
#         else:
#             return HttpResponse("""your form is wrong, reload on <a href = "{% url 'Catalog:catalog_page' %}">reload</a>""") # fix
#     else:
#         upload_form = CategoryCreate()
#         return render(request, 'Catalog/upload_form.html', {'upload_form': upload_form})
#
#
# def update_category(request, category_id):
#     category_id = int(category_id)
#     try:
#         book = Category.objects.get(pk=category_id)
#     except Category.DoesNotExist:
#         return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
#     category_form = CategoryCreate(request.POST, request.FILES, instance=book)
#     if category_form.is_valid():
#         category_form.save()
#         return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
#     return render(request, 'Catalog/upload_form.html', {'upload_form': category_form})
#
#
# def delete_category(request, category_id):
#     category_id = int(category_id)
#     try:
#         category = Category.objects.get(id=category_id)
#     except Category.DoesNotExist:
#         return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
#     category.delete()
#     return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
#
#
# def product_page(request, category_id):
#     category = get_object_or_404(Category, pk=int(category_id))
#     product_list = category.product_set.all()
#     p = Paginator(product_list, 2)
#     page = request.GET.get('page')
#     product_per_page = p.get_page(page)
#     return render(request, 'Catalog/shelf.html',
#                   {'category': category, 'product_per_page': product_per_page})
#
#
# def upload_product(request):
#     if request.method == 'POST':
#         upload_form = ProductCreate(request.POST, request.FILES)
#         if upload_form.is_valid():
#             upload_form.save()
#             return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
#         else:
#             return HttpResponse("""your form is wrong, reload on <a href = "{% url 'Catalog:catalog_page' %}">reload</a>""") # fix
#     else:
#         upload_form = ProductCreate()
#         return render(request, 'Catalog/upload_form.html', {'upload_form': upload_form})
#
#
# def update_book(request, product_id):
#     product_id = int(product_id)
#     try:
#         book = Product.objects.get(pk=product_id)
#     except Product.DoesNotExist:
#         return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
#     product_form = ProductCreate(request.POST or None, instance=book)
#     if product_form.is_valid():
#         product_form.save()
#         return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
#     return render(request, 'Catalog/upload_form.html', {'upload_form': product_form})
#
#
# def delete_book(request, product_id):
#     product_id = int(product_id)
#     try:
#         book = Product.objects.get(id=product_id)
#     except Product.DoesNotExist:
#         return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
#     book.delete()
#     return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))


