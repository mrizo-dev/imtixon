from django.contrib import admin
from django.urls import path
from main.views import (
    hamma_studentlar,
    hamma_rejalar,
    bajarilmagan_rejalar,
    bitiruvchilar,
    katta_talabalar,
    bitiruvchilar_rejalari,
    talaba_rejalari,
    reja_qoshish,
    reja_ochirish
)

urlpatterns = [
    # 1. Admin panel (Buni birinchi yozgan ma'qul)
    path('admin/', admin.site.urls),

    # 2. Bosh sahifa (Saytga kirganda nima chiqishi)
    path('', hamma_studentlar, name='home'),

    # 3. Studentlar bilan bog'liq manzillar
    path('studentlar/', hamma_studentlar, name='hamma_studentlar'),
    path('studentlar/kattalar/', katta_talabalar, name='katta_talabalar'),
    path('bitiruvchilar/', bitiruvchilar, name='bitiruvchilar'),
    path('talaba/<int:talaba_id>/rejalar/', talaba_rejalari, name='talaba_rejalari'),

    # 4. Rejalar bilan bog'liq manzillar
    path('rejalar/', hamma_rejalar, name='hamma_rejalar'),
    path('bajarilmagan-rejalar/', bajarilmagan_rejalar, name='bajarilmagan_rejalar'),
    path('bitiruvchilar/rejalari/', bitiruvchilar_rejalari, name='bitiruvchilar_rejalari'),
    path('reja-qoshish/', reja_qoshish, name='reja_qoshish'),
    path('reja-ochirish/<int:reja_id>/', reja_ochirish, name='reja_ochirish'),
]