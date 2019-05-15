from django.contrib import admin
from django.utils.safestring import mark_safe

from photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ['get_img', 'name', 'license', 'visibility', 'get_owner_name']
    list_filter = ['license', 'visibility', 'owner']
    search_fields = ['name', 'description', 'url', 'owner__first_name', 'owner__last_name']
    readonly_fields = ['get_img', 'get_owner_name']

    def get_owner_name(self, obj):
        return '{0} {1}'.format(obj.owner.first_name, obj.owner.last_name)

    get_owner_name.short_description = 'Owner'
    get_owner_name.admin_order_field = 'owner__first_name'

    def get_img(self, obj):
        return mark_safe('<img src="{0}" height="50">'.format(obj.url))

    get_img.short_description = 'Image'
    get_img.admin_order_field = 'name'
