
from django.urls import path
from bali.views import(
    CheckListsAPIView,
    CheckListAPIView,
    CheckListItemCreateAPIview,
    CheckListItemAPIview,
    )

urlpatterns = [
    path('api/CheckLists/', CheckListsAPIView.as_view()),
    path('api/CheckLists/<int:pk>/', CheckListAPIView.as_view()),
    path('api/CheckListItem/create/', CheckListItemCreateAPIview.as_view()),
    path('api/CheckListItem/<int:pk>/', CheckListItemAPIview.as_view()),
]
