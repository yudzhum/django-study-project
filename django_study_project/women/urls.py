from django.urls import path, re_path
from django_study_project.women import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.WomenIndex.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
