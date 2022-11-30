from django.shortcuts import render
import json, os
from jsontomysql.settings import BASE_DIR
from .models import JsonModel

# Create your views here.
# mysql -u username -p -h localhost DATA-BASE-NAME < data.sql


def index(request):

    # json_data = open(os.path.join(BASE_DIR, "static", "json/quran_0.json"))
    # json_datas = [
    #     json.load(open(os.path.join(BASE_DIR, "static", f"json/quran_{i}.json")))
    #     for i in range(114)
    #     if i != 1
    # ]
    for i in range(114):
        if i != 1:
            json_data = open(os.path.join(BASE_DIR, "static", f"json/quran_{i}.json"))
            data = json.load(json_data)
            for j in data:
                # for data in range(len(i)):
                #     # JsonModel.objects.create(**i[data])
                #     # data = json.load(json_data)
                q0 = JsonModel(
                    id=j["id"],
                    verse_number=j["verse_number"],
                    verse_key=j["verse_key"],
                    hizb_number=j["hizb_number"],
                    rub_el_hizb_number=j["rub_el_hizb_number"],
                    ruku_number=j["ruku_number"],
                    manzil_number=j["manzil_number"],
                    sajdah_number=j["sajdah_number"],
                    text_uthmani=j["text_uthmani"],
                    chapter_id=j["chapter_id"],
                    text_imlaei_simple=j["text_imlaei_simple"],
                    juz_number=j["juz_number"],
                    translations=j["translations"],
                )
                print("now doing -> ", q0.chapter_id, q0.verse_number)
                q0.save()

    # q0.save()
    return render(
        request,
        "index.html",
        {"json_data": "nothin to see here DUDE!\nMain work running in the background"},
    )
