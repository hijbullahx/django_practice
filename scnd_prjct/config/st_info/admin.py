from django.contrib import admin

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("st_id", "st_name", "dept", "dob", "gender", "address")
    search_fields = ("st_id", "st_name")
    list_filter = ("dept", "gender")
    