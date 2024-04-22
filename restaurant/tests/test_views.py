from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from restaurant.models import Dish, DishType, Cook

DISH_URL = reverse("restaurant:dish-list")
DISH_TYPE_URL = reverse("restaurant:dish-type-list")
COOK_URL = reverse("restaurant:cook-list")


class PublishModelTests(TestCase):
    def test_login_required(self):
        response1 = self.client.get(DISH_URL)
        response2 = self.client.get(DISH_TYPE_URL)
        response3 = self.client.get(COOK_URL)
        self.assertNotEqual(response1.status_code, 200)
        self.assertNotEqual(response2.status_code, 200)
        self.assertNotEqual(response3.status_code, 200)


class PrivateModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="cocktails")
        DishType.objects.create(name="salads")
        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "restaurant/dish_type_list.html")

    def test_retrieve_cooks(self):
        Cook.objects.create(username="test admin", years_of_experience=5)
        Cook.objects.create(username="test admin_young", years_of_experience=0)
        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)
        cooks = Cook.objects.all()
        self.assertEqual(list(response.context["cook_list"]), list(cooks))
        self.assertTemplateUsed(response, "restaurant/cook_list.html")

    def test_retrieve_dishes(self):
        dish_type = DishType.objects.create(name="cocktails")
        Dish.objects.create(
            name="verona",
            dish_type=dish_type,
            price=5.00,
            description="test info"
        )
        Dish.objects.create(
            name="milano",
            dish_type=dish_type,
            price=5.00,
            description="test more info"
        )
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(list(response.context["dish_list"]), list(dishes))
        self.assertTemplateUsed(response, "restaurant/dish_list.html")
