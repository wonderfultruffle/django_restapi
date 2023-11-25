from django.contrib import admin
from .models import Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    
    list_display = ["id", "subscriber", "room", "date_from", "date_to", "created", "updated"]
    
    list_editable = ["room", "date_from", "date_to"]
    
    raw_id_fields = ["subscriber"]
    # raw_id_fields: 관리자 페이지에서 fk 나 m:m 관계인 field의 값을 설정하는 input 위젯을 제공(기본 위젯은 select임)
    #                fk는 pk를 입력해야 하고 m:m field는 comma(,)로 구분되는 list 형식으로 입력해야 함.
    
admin.site.register(Booking, BookingAdmin)