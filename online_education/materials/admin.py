from django.contrib import admin

from .models import Course, Lesson, Subscribe


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "preview", "description")


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview", "link_on_video", "course")


@admin.register(Subscribe)
class UserAdmin(admin.ModelAdmin):
    list_display = ("course", "user")
