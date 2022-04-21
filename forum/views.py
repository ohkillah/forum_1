import json
from unicodedata import category

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from forum.models import Category, Topic, Message


#@login_required(login_url="/login/")
def index(request: HttpRequest) -> HttpResponse:
    category_id = request.GET.get("category", "")
    topics = Topic.objects.filter(blocked=False)
    categories = Category.objects.all()
    if category_id != "":
        try:
            category = Category.objects.get(id=int(category_id))
            topics = topics.filter(category=category)
        except:
            pass
    return render(request, "topics.html", context={
        'topics':  topics,
        'categories': categories,
    })


def main_view(request: HttpRequest) -> HttpResponse:
    # Get the list of all categories
    # render file "categories.html" with all categories
    categories = Category.objects.all()
    return render(request, "categories.html", context={
        "categories": categories})


def category_view(request: HttpRequest, category_id: int) -> HttpResponse:
    # Get the category with id category_id
    # Get the list of topics with category=category
    # render file "topics.html" with category and topics
    category = Category.objects.get(id=category_id)
    topics = Topic.objects.filter(category=category).all()
    return render(request, "topics.html", context={
        'category': category,
        'topics':  topics,
    })


def topic_view(request: HttpRequest, topic_id: int) -> HttpResponse:
    # Get the topic with topic_id
    # Get the corresponding category
    # Get the list of messages with topic=topic
    # render file "messages.html" with category, topic, messages
    topic = Topic.objects.get(id=topic_id)
    category = Category.objects.get(topic=topic)
    messages = Message.objects.filter(topic=topic).all()
    return render(request, "messages.html", context={
        'topic': topic,
        'messages':  messages,
        'category': category,
    })


def topic_updownvote(request: HttpRequest, topic_id: int) -> HttpResponse:
    if request.user.is_anonymous:
        return HttpResponse("Please login first", status=404)
    if request.method == "POST":
        body = json.loads(request.body.decode("utf8"))
        action = body["action"]
        try:
            topic = Topic.objects.get(pk=topic_id)
            if topic.upvoted_users.filter(id=request.user.id):
                topic.upvoted_users.remove(request.user)
            elif topic.downvoted_users.filter(id=request.user.id):
                topic.downvoted_users.remove(request.user)
            elif action == "up":
                topic.upvoted_users.add(request.user)
            elif action == "down":
                topic.downvoted_users.add(request.user)
            else:
                return HttpResponse(f"action not implemented: {action}", status=400)
        except ObjectDoesNotExist:
            return HttpResponse("Topic not found", status=404)
        return HttpResponse(str(topic.get_votes()), status=200)

    return HttpResponse("please post, not get", status=400)
