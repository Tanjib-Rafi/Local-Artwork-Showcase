from django.urls import path
from .views import ArtistProfileDetail, ArtworkListCreateView, ArtworkRetrieveUpdateDestroyView

urlpatterns = [
    path('profile/<int:pk>/', ArtistProfileDetail.as_view(), name='artist-profile-detail'),
    path('artworks/', ArtworkListCreateView.as_view(), name='artwork-list-create'),
    path('artworks/<int:pk>/', ArtworkRetrieveUpdateDestroyView.as_view(), name='artwork-detail'),
]
