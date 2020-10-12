from django.urls import path

from users import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create_user'),
    path('email-verification/', views.VerifyEmail.as_view(), name='email_verification'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('update/', views.UserView.as_view(), name='update_user')
]
