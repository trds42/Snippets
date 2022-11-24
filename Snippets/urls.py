from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('snippets/add', views.add_snippet_page, name='snippets-add'),
    path('snippets/list', views.snippets_page, name='snippets-list'),
    path('snippets/<int:snippet_id>', views.show_snippet_page, name='snippet-show'),
    path('comment/add', views.comment_add, name='comment_add'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('registration', views.registration, name='registration'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
