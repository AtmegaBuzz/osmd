from django.contrib import admin
from BookCab.models import (
    Booking,
    CabGroup,
    Source
)

admin.site.register(Booking)
admin.site.register(CabGroup)
admin.site.register(Source)
