from django.test import TestCase
from lib_app.models import Book

# Create your tests here.


class TestModel(TestCase):
    def setUp(self):
        self.book = Book.objects.create(name="Hello_buddy", price=450, qty=33, is_published=True)

    def test_name(self):
        self.assertEqual(self.book.name, "Hello_buddy")
        self.assertTrue(self.book.is_published)

    