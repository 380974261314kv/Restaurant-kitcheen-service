from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import DishType, Dish
from restaurant.forms import DishTypeSearchForm, DishSearchForm, CookSearchForm


DISH_URL = reverse("restaurant:dish-list")
DISH_TYPE_URL = reverse("restaurant:dish-type-list")
COOK_URL = reverse("restaurant:cook-list")


class SearchFormsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="test1234"
        )
        self.client.force_login(self.user)

        self.dish_type1 = DishType.objects.create(name="Soups")
        self.dish_type2 = DishType.objects.create(name="Salads")

    def test_dish_type_get_context_data_with_search_form(self):
        url = DISH_TYPE_URL
        data = {"name": "Sa"}

        response = self.client.get(url, data=data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context["search_form"],
            DishTypeSearchForm
        )
        self.assertEqual(response.context["search_form"].initial["name"], "Sa")

    def test_dish_get_context_data_with_search_form(self):
        self.dish1 = Dish.objects.create(
            name="Cezar Salad",
            price=100,
            dish_type=self.dish_type1,
        )
        self.dish2 = Dish.objects.create(
            name="Greek Salad",
            price=150,
            dish_type=self.dish_type2,
        )

        url = DISH_URL
        data = {"name": "salad"}

        response = self.client.get(url, data=data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["search_form"], DishSearchForm)
        self.assertEqual(
            response.context["search_form"].initial["name"],
            "salad"
        )

    def test_cook_get_context_data_with_search_form(self):
        self.cook1 = get_user_model().objects.create_user(
            username="admin101",
            password="admin3476",
        )
        self.cook2 = get_user_model().objects.create_user(
            username="best.cook",
            password="super.cook",
        )

        url = COOK_URL
        data = {"username": "admin"}

        response = self.client.get(url, data=data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["search_form"], CookSearchForm)
        self.assertEqual(
            response.context["search_form"].initial["username"],
            "admin"
        )

    def test_cook_search_form(self):
        form = CookSearchForm(data={"username": "test user"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "test user")

    def test_dish_type_search_form(self):
        form = DishSearchForm(data={"name": "cocktails"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "cocktails")

    def test_dish_search_form(self):
        form = DishSearchForm(data={"name": "test dish"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "test dish")
