from django.db import models
from django.contrib.auth.models import User
'''
Версия 1.0:

    1. Приложение должно принимать от пользователя данные:

       - Пол
       - Вес
       - Рост
       - Возраст
       - Уровень активности

    2. Производится расчёт по формулам: 

       - Мужчины: ВОО = 66 + (13.7 х вес в кг) + (5 х рост в см) - (6.8 х возраст в годах)
       - Женщины: ВОО = 655 + (9.6 х вес в кг) + (1.8 х рост в см) - (4.7 х возраст в годах)

       Коэффициенты активности: 
            - Сидячий образ жизни = ВОО х 1.2 (мало или совсем не делаете упражнения, сидячая работа)
            - Небольшая активность = ВОО х 1.375 (небольшая физическая нагрузка/ занятия спортом 1-3 раза в неделю)
            - Умеренная активность = ВОО х 1.55 (достаточно большая физическая нагрузка / занятия спортом 3-5 раз в неделю)
            - Высокая активность = ВОО х 1.725 (большая физическая нагрузка/ занятия спортом 6-7 раз в неделю)
            - Очень высокая активность = ВОО х 1.9 (очень большая ежедневная физическая нагрузка/ занятия спортом и физическая работа или тренировки 2 раза в день, например, марафон, соревнования)

        СПК = ВОО х коэффициент активности

        СПК - суточная потребность в калориях 
        ВОО - величина основного обмена

    3. Приложение должно выводить (через AJAX):

       - Суточную потребность в калориях.


    Sedentary lifestyle = HEI x 1.2 (do little or no exercise, sit-down work)
    Slight activity = HEI x 1.375 (slight exercise / sports 1-3 times a week)
    Moderate activity = HEI x 1.55 (quite large exercise / sports 3-5 times a week)
    High activity = HEI x 1.725 (large physical activity / sports 6-7 times a week)
    Very high activity = HEI x 1.9 (very large daily exercise / sports and physical work or training 2 times a day, for example, a marathon, competitions)

'''

# A user of our website.
class User(User):

    name = models.TextField(max_length=500, blank=True, null=True, default=None)
    gender = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=500, decimal_places=0)
    age = models.DecimalField(max_digits=150, decimal_places=0)
    
    def get_basal_metabolism(self):
        pass


    

