from django.urls import path
from restaurant import views


app_name = "restaurant"

urlpatterns = [
    path("", views.index, name="index"),
    path("dish_types/", views.DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_types/<int:pk>/", views.DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dish_types/ctreate/", views.DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", views.DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", views.DishCreateView.as_view(), name="dish-create"),
    path("cooks/", views.CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", views.CookDetailView.as_view(), name="cook-detail"),
]
