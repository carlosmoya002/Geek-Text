from django.contrib import admin

from .models import Wishlists
from .models import Books
from .models import Genres
from .models import Bookratings
from .models import Purchasedbooks

admin.site.register(Wishlists)
admin.site.register(Books)
admin.site.register(Genres)
admin.site.register(Bookratings)
admin.site.register(Purchasedbooks)
