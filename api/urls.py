from django.urls import path
from .views import ProductsListView, ProductsCreateView, ProductsDestroyView, ProductsUpdateView



urlpatterns = [
    path('get-list', ProductsListView.as_view(), name="list_view"),
    path('post-list', ProductsCreateView.as_view(), name="post_view"),
    path('delete-list/<pk>', ProductsDestroyView.as_view(), name="delete_view"),
    path('update-list', ProductsUpdateView.as_view(), name="update_view"),
]