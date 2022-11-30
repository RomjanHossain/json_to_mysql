from django.shortcuts import render
import json, os
from jsontomysql.settings import BASE_DIR
from .models import JsonModel

# Create your views here.


def index(request):

    # json_data = open(os.path.join(BASE_DIR, "static", "json/quran_0.json"))
    # json_datas = [
    #     json.load(open(os.path.join(BASE_DIR, "static", f"json/quran_{i}.json")))
    #     for i in range(114)
    #     if i != 1
    # ]
    # for i in json_datas:
    #     for data in range(len(i)):
    #         # JsonModel.objects.create(**i[data])
    #         # data = json.load(json_data)
    #         q0 = JsonModel(
    #             id=i[0]["id"],
    #             verse_number=i[data]["verse_number"],
    #             verse_key=i[data]["verse_key"],
    #             hizb_number=i[data]["hizb_number"],
    #             rub_el_hizb_number=i[data]["rub_el_hizb_number"],
    #             ruku_number=i[data]["ruku_number"],
    #             manzil_number=i[data]["manzil_number"],
    #             sajdah_number=i[data]["sajdah_number"],
    #             text_uthmani=i[data]["text_uthmani"],
    #             chapter_id=i[data]["chapter_id"],
    #             text_imlaei_simple=i[data]["text_imlaei_simple"],
    #             juz_number=i[data]["juz_number"],
    #             translations=i[data]["translations"],
    #         )
    #         print("now doing -> ", q0.chapter_id, q0.verse_number)
    #         q0.save()

    # q0.save()
    return render(
        request,
        "index.html",
        {"json_data": "nothin to see here DUDE!\nMain work running in the background"},
    )
