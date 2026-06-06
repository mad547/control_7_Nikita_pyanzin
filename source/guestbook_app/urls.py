from django.urls import path
from guestbook_app.views import entry_list, entry_add, entry_edit, entry_delete


urlpatterns = [
    path('', entry_list, name='entry_list'),
    path('add/', entry_add, name='entry_add'),
    path('<int:entry_id>/edit/', entry_edit, name='entry_edit'),
    path('<int:entry_id>/delete/', entry_delete, name='entry_delete'),
]