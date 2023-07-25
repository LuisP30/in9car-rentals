from django.contrib import admin

from .models import Veiculo


class VeiculoAdmin(admin.ModelAdmin):
    ...


admin.site.register(Veiculo, VeiculoAdmin)
