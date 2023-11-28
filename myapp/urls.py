from django.urls import path
from .views import set_cookie, set_session, show_message, sign_data

urlpatterns = [
    path('set_cookie/', set_cookie, name='set_cookie'),
    path('set_session/', set_session, name='set_session'),
    path('show_message/', show_message, name='show_message'),
    path('sign_data/', sign_data, name='sign_data'),
]
