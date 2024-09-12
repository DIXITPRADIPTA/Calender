from django.urls import path
from . import views  
from .views import HomePageView
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static

urlpatterns = [
     path('home/', views.HomePageView, name='home'),

     path('horoscope/', views.horoscope_page, name='horoscope_page'),

]  # Your home view defined earlier
    # Add more paths here as needed
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
