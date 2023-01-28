from django.urls import include, path
from django.utils.module_loading import autodiscover_modules, import_string
from django.views.generic import RedirectView

admin_site = import_string('django.contrib.admin.site')
autodiscover_modules("admin", register_to=admin_site)

urlpatterns = [
    path("v1/", include(admin_site.urls[:2])),
    path("", RedirectView.as_view(url="/v1/"), name="index"),
]
