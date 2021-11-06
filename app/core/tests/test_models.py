from django.test import TestCase
from django.contrib.auth import get_user_model

# from core import models


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating user with email """
        email = 'test@test.com'
        password = 'Test@1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_emai_nomalized(self):
        """Test news user with normalized email """
        email = 'teas@TEST.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with valid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_creat_new_superuser(self):
        """Test creating new super user"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'tes@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
