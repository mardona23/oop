class denmark:
        def capital(self):
            print("Copenhagen is the capital of denmark.")
        def language(self):
            print("danish is the most spoken language in denmark")
        def type(self):
            print("denmark is a developed country")
class sweden:
        def capital(self):
            print("stockholm is the captial of sweden")
        def language(self):
            print("swedish is the most spoken language in sweden")
        def type(self):
            print("sweden is a developed country")
obj_den=denmark()
obj_swe=sweden()
for country in(obj_den,obj_swe):
    country.capital()
    country.language()
    country.type()