from django.contrib import admin

from .models import Account,Contact, ContactSource, ContactStatus,Event

admin.site.register(Account)
admin.site.register(Contact)
admin.site.register(ContactSource)
admin.site.register(ContactStatus)
admin.site.register(Event)