"""Extra URLs, added to `df_config.root_urls`."""

from django.urls import include, path
from django.utils.module_loading import autodiscover_modules, import_string
from django.views.generic import RedirectView

admin_site = import_string("django.contrib.admin.site")
autodiscover_modules("admin", register_to=admin_site)

urlpatterns = [
    path("", RedirectView.as_view(url="/v1/"), name="index"),
]
