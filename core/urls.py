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
#  create an item,
# adding item to week, removing item from week
# add (provide price )and remove expense item from week
# edit a week expense item
# handle the price changes e.g when add new item change the wallet price maybe
# update wallet details

# MUCH LATER
# editting a wallet