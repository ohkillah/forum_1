from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from forum.models import (
    Category,
    Topic,
    Message,
)


def create_fake_data():
    if User.objects.filter(username="timurbakibayev").exists():
        print("Data is already there")
        return

    user_admin1 = User.objects.create_user(
        username="admin",
        first_name="Super",
        last_name="Admin",
        is_superuser=True,
        is_staff=True,
        email="admin@gmail.com",
    )
    user_admin1.set_password("admin")
    user_admin1.save()

    user_admin = User.objects.create_user(
        username="timurbakibayev",
        first_name="Timur",
        last_name="Bakibayev",
        is_superuser=True,
        is_staff=True,
        email="timurbakibayev@gmail.com",
    )
    user_admin.set_password("timurtimur")
    user_admin.save()

    user_normal = User.objects.create_user(
        username="user",
        first_name="Bill",
        last_name="Gates",
        is_superuser=False,
        email="billgates@gmail.com",
    )
    user_normal.set_password("useruser")
    user_normal.save()

    category1 = Category.objects.create(name="Django")
    category2 = Category.objects.create(name="Python")
    category3 = Category.objects.create(name="PyGame")

    topic1 = Topic.objects.create(
        category=category1,
        name="How to create a Django project",
        author=user_normal,
    )

    message1 = Message.objects.create(
        topic=topic1,
        author=user_normal,
        text="""
        Go to settings -> project -> django -> create. 
        You should know this from school!
        """,
    )

    message2 = Message.objects.create(
        reply_to=message1,
        topic=topic1,
        author=user_admin,
        text="""
        No!!!!
        
        You should write something like this:
        django-admin startproject project_name
        """,
    )

    topic2 = Topic.objects.create(
        category=category1,
        name="How to create an app inside a Django project",
        author=user_normal,
        text="""What is Lorem Ipsum?
    Lorem Ipsum is simply dummy text of the printing and typesetting
    industry. Lorem Ipsum has been the industry's standard dummy text
    ever since the 1500s, when an unknown printer took a galley of type
    and scrambled it to make a type specimen book. It has survived not only 
    five centuries, but also the leap into electronic typesetting, remaining 
    essentially unchanged. It was popularised in the 1960s with the release 
    of Letraset sheets containing Lorem Ipsum passages, and more recently with 
    desktop publishing software like Aldus PageMaker including versions of 
    Lorem Ipsum
    """
    )

    topic3 = Topic.objects.create(
        category=category2,
        name="How to initialize a variable",
        author=user_normal,
        text="""What is Lorem Ipsum?
    Lorem Ipsum is simply dummy text of the printing and typesetting
    industry. Lorem Ipsum has been the industry's standard dummy text
    ever since the 1500s, when an unknown printer took a galley of type
    and scrambled it to make a type specimen book. It has survived not only 
    five centuries, but also the leap into electronic typesetting, remaining 
    essentially unchanged. It was popularised in the 1960s with the release 
    of Letraset sheets containing Lorem Ipsum passages, and more recently with 
    desktop publishing software like Aldus PageMaker including versions of 
    Lorem Ipsum
    """
    )

    topic4 = Topic.objects.create(
        category=category3,
        name="How write a cool game in PyGame?",
        author=user_normal,
        text="""What is Lorem Ipsum?
    Lorem Ipsum is simply dummy text of the printing and typesetting
    industry. Lorem Ipsum has been the industry's standard dummy text
    ever since the 1500s, when an unknown printer took a galley of type
    and scrambled it to make a type specimen book. It has survived not only 
    five centuries, but also the leap into electronic typesetting, remaining 
    essentially unchanged. It was popularised in the 1960s with the release 
    of Letraset sheets containing Lorem Ipsum passages, and more recently with 
    desktop publishing software like Aldus PageMaker including versions of 
    Lorem Ipsum
    """
    )

    print("Data created.")


class Command(BaseCommand):
    help = 'Creates fake data'

    def handle(self, *args, **options):
        create_fake_data()
        print("Done.")
