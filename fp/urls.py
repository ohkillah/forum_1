from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import forum.views as main_views
from forum.auth_views import (
    forgot_password_success_view,
    login_view,
    register_view,
    forgot_password_view,
    forgot_password_success_view,
    logout_view,
)
from fp import settings

urlpatterns = [
    path('', main_views.index),
    path('category/<int:category_id>', main_views.category_view),
    path('topic/<int:topic_id>/', main_views.topic_view),
    path('topic/<int:topic_id>/updownvote/', main_views.topic_updownvote),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('forgot_password/', forgot_password_view),
    path('forgot_password_success/', forgot_password_success_view),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
