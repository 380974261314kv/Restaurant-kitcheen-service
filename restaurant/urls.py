from django.urls import path
from restaurant import views


app_name = "restaurant"

urlpatterns = [
    path("", views.index, name="index"),
    path("dish_types/", views.DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_types/<int:pk>/", views.DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dish_types/create/", views.DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish_types/update/<int:pk>/", views.DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish_types/delete/<int:pk>/", views.DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", views.DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", views.DishCreateView.as_view(), name="dish-create"),
    path("dishes/update/<int:pk>/", views.DishUpdateView.as_view(), name="dish-update"),
    path("dishes/delete/<int:pk>/", views.DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", views.CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", views.CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", views.CookCreateView.as_view(), name="cook-create"),
]
