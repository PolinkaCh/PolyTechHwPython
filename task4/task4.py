class Translators:
    def __init__(self, first_name,  last_name, email, phone):
      self.first_name = first_name
      self.last_name = last_name
      self.email = email
      self.phone = phone

    def __str__(self):
      return self.last_name + " " + self.first_name
      
translator = Translators("Лена", "Богатырёва", "Bog@mail.ru", 897658975) 
print (translator.__str__())

class Post:
    def __init__(self,language,  translation_type,  movie_type, title, episode, duration,  rate,  deadline):
      self.language = language
      self.translation_type = translation_type
      self.movie_type = movie_type
      self.title = title
      self.episode = episode
      self.duration = duration
      self.rate = rate
      self.deadline = deadline
      
    def __str__(self):
        return self.title

    def info(self):
        print("Новый заказ")
        print("Язык: " + self.language)
        print("Вид перевода: " + self.translation_type)
        print("Тип: " + self.movie_type)
        print("Название: " + self.title)
        print("Серия: " + str(self.episode))
        print("Длительность: " + str(self.duration))
        print("Ставка: " + str(self.rate))
        print("Срок сдачи: " + str(self.deadline))

        
        
class Order(Post):
    def __init__(self, receipt_date, translator, language,  translation_type,  movie_type, title, episode, duration,  rate,  deadline):
      super().__init__(language,  translation_type,  movie_type, title, episode, duration,  rate,  deadline)
      self.receipt_date = receipt_date
      self.translator = translator
    
    def info(self):
        print("Взятый заказ")
        print("Язык: " + self.language)
        print("Вид перевода: " + self.translation_type)
        print("Тип: " + self.movie_type)
        print("Название: " + self.title)
        print("Серия: " + str(self.episode))
        print("Длительность: " + str(self.duration))
        print("Ставка: " + str(self.rate))
        print("Срок сдачи: " + str(self.deadline))
        print("Дата получения: " + str(self.receipt_date))
        print("Переводчик: " + self.translator)
     

newPost = Post("en","dubbing","serial", "7 months", 2, 46, 50, 27.11)
newOrder = Order (13.11, "Chebisheva","en","dubbing","serial", "7 months", 2, 46, 50, 27.11)
#newOrder.info()