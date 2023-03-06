from django.contrib import admin
from .models import Category, Book, BookInstance, Author
from django.contrib import admin
# Register your models here.


class MyBookInline(admin.TabularInline):
    model = BookInstance
    extra = 0
    # readonly_fields = ('id', )
    can_delete = False


class MyBookInstanceAdmin(admin.ModelAdmin):
    model = BookInstance
    list_display = ["book", "status", "borrower", "due_back"]
    list_filter = ("status", "due_back")


class MyBookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ["title", "author"]
    list_filter = ("title", "category")
    fieldsets = (
        ('Information', {'fields': ("title", "category")}),
        ('Detail', {'fields': ("picture", "author", "summary")}),
    )

    inlines = [MyBookInline]


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book, MyBookAdmin)
admin.site.register(BookInstance, MyBookInstanceAdmin)


# Must have Foreign key
# class MyCategoryAdmin(admin.ModelAdmin):
#     model = Category
#     inlines = [MyProductInline]


