from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # The include() function allows referencing other URLconfs
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
