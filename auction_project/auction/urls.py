from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),

    #User Account paths
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path("", views.loginPage, name="home"),
    path('logout/', views.logout_view, name="logout"),

    
    #User API paths
    path('api/users/', views.users_api, name="users"),
    path('api/users/<int:userID>/', views.user_api, name="user"),
    path('api/sessionUser/', views.sessionUser, name="sessionUser"),

    #Item API paths
    path('api/items/', views.items_api, name="items"),
    path('api/items/<int:itemID>/', views.item_api, name="item"),
    path('api/items/<int:itemID>/questions', views.item_questions_api, name="itemquestions"),
    path('api/items/<int:itemID>/bids', views.item_bids_api, name="itembids"),
    path('api/available/', views.available_items, name="available"),
    path('api/available/<str:query>/', views.available_items, name="available"),

    #Bid API paths
    path('api/bids/', views.bids_api, name="bids"),
    path('api/bids/<int:bidID>/', views.bid_api, name="bid"),

    #Question paths
    path('api/questions/', views.questions_api, name="questions"),
    path('api/questions/<int:questionID>/', views.question_api, name="question"),

    #Profile paths
    path('api/profile/<int:userID>/', views.profileImage_api, name="profile"),

    #Send mail test
    path('mail/', views.emailWinners, name="mail"),

]
