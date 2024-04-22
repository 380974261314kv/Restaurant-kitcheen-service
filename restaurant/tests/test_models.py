from django.test import TestCase
from django.contrib.auth import get_user_model

from restaurant.models import Dish, DishType, Cook


class ModelTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Test Dish Type")
        self.dish = Dish.objects.create(
            name="Test Dish",
            dish_type=self.dish_type,
            description="Test Dish Description",
            price=100,
        )
        self.cook = Cook.objects.create(
            username="Test Cook",
            first_name="Test Cook First",
            last_name="Test",
            years_of_experience=1,
        )
        self.dish.cooks.add(self.cook)

    def test_dish_str(self):
        self.assertEquals(
            str(self.dish), self.dish.name
        )

    def test_dish_type_str(self):
        self.assertEquals(
            str(self.dish_type), self.dish_type.name
        )

    def test_cook_str(self):
        self.assertEquals(
            str(self.cook),
            f"{self.cook.username} "
            f"({self.cook.first_name} {self.cook.last_name})"
        )

    def test_create_cook_with_years_of_experience(self):
        username = "test user"
        password = "test_password"
        years_of_experience = 1
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )
        self.assertEquals(cook.username, username)
        self.assertEquals(
            cook.years_of_experience,
            years_of_experience
        )
        self.assertTrue(cook.check_password(password))
