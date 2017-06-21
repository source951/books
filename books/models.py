from django.db import models

GENRES = (
    (1, "Romans"),
    (2, "Obyczajowa"),
    (3, "Sci-fi i fantasy"),
    (4, "Literatura faktu"),
    (5, "Popularnonaukowa"),
    (6, "Poradnik"),
    (7, "Kryminał, sensacja")
)


# Create your models here.

class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=17)
    publisher = models.CharField(max_length=200)
    genre = models.IntegerField(choices=GENRES)

    def __str__(self):
        return '{} "{}"'.format(self.author, self.title)


def fake_book(locale="en_US"):
    fake = Factory.create(locale)
    t1 = ["Tajemnica", "Śmierć", "Kod", "Zabójstwo", "Śledztwo", "Proces",
         "Gra", "Bogactwo", "Teoria", "Miłość", "Dane", "Szyfry", "Zagadka",
         "Manipulacja", "Szansa", "Żal", "Broń", "Zdrowie", "Herezja", 
         "Porwanie", "Poszukiwania", "Zabawa", "Programy", "Pieniądze",
         "Komunikat", "Leczenie", "Psychoterapia", "Rozrywka", "Ból",
         "Dziewczyny", "Chłopaki", "Druhny", "Rodzice", "Dzieci", "Dziadkowie",
         "Narzeczone", "Żony"]
    t2 = ["Afrodyty", "Da Vinci", "szaleńca", "Newtona", "Einsteina", "rycerza",
          "wojownika", "lęku", "sportowców", "komputerów", "nauki",
          "czarownic", "kierowców", "żołnierzy", "przyrody", "profesjonalistów",
          "naukowców", "zwierząt", "w Kosmosie", "na bogato", "w Polsce", 
          "we współczesnym świecie", "w górach", "nad morzem", "na rynku", 
          "w polityce", "Polaków", "Europy", "na wojnie", "dla każdego", 
          "w weekend", "istnienia", "lekarzy", "królów", "prezydentów",
          "zapomnianych", "Złego", "bogów"]

    isbn = fake.ean13()
    author = "{} {}".format(fake.first_name(), fake.last_name())
    publisher = fake.company()
    genre = choice(GENRES)[0]
    b = Book()
    b.title = "{} {}".format(choice(t1), choice(t2))
    b.author = author
    b.isbn = "{}-{}-{}-{}-{}".format(isbn[0:3], isbn[3], 
        isbn[4:8], isbn[8:12], isbn[12])
    b.publisher = publisher
    b.genre = genre
    b.save()
