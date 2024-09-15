
from django.contrib import admin
from django.urls import path
from food.views import (
    FoodListCreateView,
    VoteCreateListView,
    VoteUpdate,
    FoodRetrieveUpdateDestroyView,
    MyProfileView,
    TimeView,
    BusyListCreateView,
    BusyRetrieveUpdateDestroyView,
    RegisterView,
    UserRatedListCreatedView,
    CustomUserUpdate,
    CommentView,
    LikeOrDislikeView,
    CommentUpdateView,

    )

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [

    path('comments/<int:foodId>/', CommentView.as_view()),
    path('comments/<int:foodId>/<int:pk>/', CommentUpdateView.as_view()),

    path('like_or_dislike/',LikeOrDislikeView.as_view()),

    path('admin/', admin.site.urls),

    path('me/',MyProfileView.as_view()),
    path('user/<str:username>/',CustomUserUpdate.as_view()),
    

    path('ct/',TimeView.as_view()),

    path('busy/',BusyListCreateView.as_view()),
    path('busy/<int:pk>/',BusyRetrieveUpdateDestroyView.as_view()),

    path('food/', FoodListCreateView.as_view()),
    path('food/<int:pk>/', FoodRetrieveUpdateDestroyView.as_view()),

    path('vote/', VoteCreateListView.as_view()),
    path('vote/<int:pk>/', VoteUpdate.as_view()),
    path('rated/', UserRatedListCreatedView.as_view()),



    path('register/', RegisterView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
