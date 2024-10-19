from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("a_shared.urls")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# LATER 
# deposit in wallet - done
# expense items of a user - done,
#  create an item - done,
# adding item to week - done
# removing item from week - done
# edit a week expense item - done
# editting a wallet - done
# handle the price changes e.g when add new item change the wallet price maybe

# MUCH LATER