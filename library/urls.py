from django.conf.urls import include, url
from . import views

urlpatterns = [
     url('about/',views.about, name = 'Library-about'),
     url('issuebook/',views.issue_book,name='Issue-book'),
    url(r'', views.home, name = 'library-home'),
    
]