from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),

    #User API paths
    path('api/users/', views.users_api, name="items"),
    path('api/users/<int:userID>/', views.user_api, name="item"),

    #Item API paths
    path('api/items/', views.items_api, name="items"),
    path('api/items/<int:itemID>/', views.item_api, name="item"),
    path('api/available/', views.available_items, name="available"),
    path('api/available/<str:query>/', views.available_items, name="available"),

    #Bid API paths
    path('api/bids/', views.bids_api, name="bids"),
    path('api/bids/<int:bidID>/', views.bid_api, name="bid"),

    #Question paths
    path('api/questions/', views.questions_api, name="questions"),
    path('api/questions/<int:questionID>/', views.question_api, name="question"),
]
