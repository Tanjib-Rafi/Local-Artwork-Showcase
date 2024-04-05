from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ArtistProfileDetail, ArtworkListCreateView, ArtworkRetrieveUpdateDestroyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ArtistProfileDetail.as_view(), name='artist-profile-detail'),
    path('artworks/', ArtworkListCreateView.as_view(), name='artwork-list-create'),
    path('artworks/<int:pk>/', ArtworkRetrieveUpdateDestroyView.as_view(), name='artwork-detail'),
]
