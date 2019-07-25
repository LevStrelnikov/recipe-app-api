from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@test.com', password='testpass'):
    """Create sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_user_with_email_successful(self):
        """Test creating new user with email successful"""
        email = "test@londonappdev.com"
        password = "TestPass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email for new user is normalized"""

        email = "test@LONDONAPPDEV.COM"
        password = "TestPass123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        email_name, domain_part = email.strip().rsplit('@', 1)
        normalized_email = email_name + '@' + domain_part.lower()
        self.assertEqual(user.email, normalized_email)

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password="Test123"
            )

    def test_create_new_super_user(self):
        """Test creating super user"""
        user = get_user_model().objects.create_superuser(
            "test@londonappdev.com",
            "test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(user=sample_user(), name='Vegan')

        self.assertEqual(str(tag), tag.name)
