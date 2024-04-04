from django.urls import path
from restaurant import views


app_name = "restaurant"

urlpatterns = [
    path("", views.index, name="index"),
    path("dish_types/", views.DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes/", views.DishListView.as_view(), name="dish-list"),
]
