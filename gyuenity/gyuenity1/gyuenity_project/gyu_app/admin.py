from django.contrib import admin
from .models import QuizResult, UserProfile, Progress,Contact
# Impor model Anda

# Mendaftarkan model ke admin site
@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz_name', 'score', 'submit_date')  # Kolom yang ditampilkan

admin.site.register(Progress)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','full_name', 'age', 'gender', 'phone')
    search_fields = ['user__username', 'full_name']
    list_filter = ('gender',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)




