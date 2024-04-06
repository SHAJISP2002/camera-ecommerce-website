from django.contrib import admin
from .models import Catagory
from .models import Product
from .models import Cart
from .models import Order



admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)


