from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Registration


class RegistrationAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        opts = obj._meta
        pk_value = obj._get_pk_val()
        obj_url = reverse(
            'admin:%s_%s_change' % (opts.app_label, opts.model_name),
            args=(pk_value,),
            current_app=self.admin_site.name,
        )
        preserved_filters = self.get_preserved_filters(request)
        if preserved_filters:
            obj_url += '?' + urlencode(preserved_filters)
        msg_dict = {
            'name': opts.verbose_name,
            'obj': obj,
        }
        self.message_user(request, 'The %(name)s "%(obj)s" was added successfully.' %
                          msg_dict, level=messages.SUCCESS)
        return HttpResponseRedirect(reverse('home'))

admin.site.register(Registration, RegistrationAdmin)

