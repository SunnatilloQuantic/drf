from django.contrib import admin

from .models import Account,Contact, ContactSource, ContactStatus

admin.site.register(Account)
admin.site.register(Contact)
admin.site.register(ContactSource)
admin.site.register(ContactStatus)
