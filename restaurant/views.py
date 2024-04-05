from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import generic

from restaurant.models import Dish, DishType, Cook


@login_required
def index(request: HttpRequest) -> HttpResponse:

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits,
    }

    return render(request, "restaurant/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "restaurant/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "restaurant/dish_type_detail.html"
    context_object_name = "dish_type"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 5


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
