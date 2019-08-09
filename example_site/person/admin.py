from django.contrib import admin
from address.models import AddressField
from address.forms import AutocompleteAddressWidget
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'address',
    )

    formfield_overrides = {
        AddressField: {
            'widget': AutocompleteAddressWidget(
                attrs={
                    'style': 'width: 300px;'
                }
            )
        }
    }
