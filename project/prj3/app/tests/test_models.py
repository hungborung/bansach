from django.test import TestCase
from app.models import *
from datetime import datetime
import unittest
class TestModels(TestCase):
    def test_event_model(self):
        category = Category.objects.create(
            code = "8",
            name = "name",
            slug = "name",
            cat_parent = "",

        )