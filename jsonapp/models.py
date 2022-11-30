from django.db import models

# set this according to your json data
class JsonModel(models.Model):
    id = models.IntegerField(primary_key=True)
    verse_number = models.IntegerField()
    verse_key = models.CharField(max_length=10)
    hizb_number = models.IntegerField()
    rub_el_hizb_number = models.IntegerField()
    ruku_number = models.IntegerField()
    manzil_number = models.IntegerField()
    # sajdah_number can be null
    sajdah_number = models.IntegerField(
        null=True,
    )
    text_uthmani = models.CharField(max_length=2000)
    chapter_id = models.IntegerField()
    text_imlaei_simple = models.CharField(max_length=2000)
    juz_number = models.IntegerField()
    translations = models.JSONField()

    def __str__(self):
        return self.chapter_id + " " + self.verse_number


# <class 'int'> id
# <class 'int'> verse_number
# <class 'str'> verse_key
# <class 'int'> hizb_number
# <class 'int'> rub_el_hizb_number
# <class 'int'> ruku_number
# <class 'int'> manzil_number
# <class 'NoneType'> sajdah_number
# <class 'str'> text_uthmani
# <class 'int'> chapter_id
# <class 'str'> text_imlaei_simple
# <class 'int'> page_number
# <class 'int'> juz_number
# <class 'list'> words
# <class 'dict'> timestamps
# <class 'list'> translations
