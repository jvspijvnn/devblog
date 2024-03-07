from django.urls import path, include
from articles import views
from my_blog import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.articles_home, name='home'),
                  path('compte/', include('accounts.urls')),
                  path('details/ <str:slug>', views.details, name='details'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
