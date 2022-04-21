from django.test import TestCase
from forum.models import Message, Category, Topic
from django.contrib.auth.models import User


class CategoryTestCase(TestCase):
    def  test_model_str(self):
        test1 = Category.objects.create(name="Tech", blocked=False)
        test2 = Category.objects.create(name="Design", blocked=True)
        self.assertEqual(str(test1), "Tech")
        self.assertEqual(str(test2), "Design")


class TopicTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="ddd",
        )

    def test_fields_author_name(self):
        category = Category(name="Tech", blocked=False )
        category.save()
        topic = Topic(
            author=self.user,
            name="How to create a Django project",
            category=category,
            blocked=False,
        )
        topic.save()
        record = Topic.objects.get(id=1)
        self.assertEqual(record.category.name, "Tech")

