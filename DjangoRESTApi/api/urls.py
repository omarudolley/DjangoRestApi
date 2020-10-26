from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns =[
    path('', views.apiOverview, name="api-overview"),
    path('secure/', views.Overclass.as_view(), name="api-overclass"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('token/',jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',jwt_views.TokenRefreshView.as_view(),name='token_refresh'),

    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
