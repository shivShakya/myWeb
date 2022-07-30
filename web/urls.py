from django.contrib import admin
from django.urls import path
from web import views
from .views import WebGetCreate,WebUpdateDelete
urlpatterns = [
    #main page
    path("",views.index,name = "web"),
    # forum page
    path("forum",views.forum,name = "forum"),  
    # go to specific question page
   path('show_forum/<venue_id>',views.show_forum,name = "show_forum"),
   #go to admin page
   path('admin/web/contact/<venue_id>',views.update_forum,name= 'update_forum'),
   #search specific question
   path('search-bar',views.search_bar,name= 'search_bar'),
   path('rest', WebGetCreate.as_view(), name = 'rest'),
   path('rest/<int:pk>',WebUpdateDelete.as_view(), name = 'rest_id')

]

