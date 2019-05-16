from django.shortcuts import render
from django.http import JsonResponse


def home_view(request, *args, **kwargs):
    return render(request, "home.html", locals())

def get_calories(request):
    submit = request.POST.get('submit_form', None)
    print(f'submit: {submit}')

    data = request.POST

    submit_form = data.get('submit_form');
    print(f'submit_form: {submit_form}');

    # Get data from user.
    username  = data.get('username')
    gender = data.get('gender')
    male_gender = data.get('male_gender')
    activity = data.get('activity')
    weight = data.get('weight')
    age = data.get('age')
    height = data.get('height')

    print(f'username: {username}')
    print(f'weight: {weight}')
    print(f'male_gender: {male_gender}')

    dictionary = {
        'is_taken': 'some_text',
        'gender': gender,
        'username': username,
        'male_gender': male_gender,
        'activity': activity,
        'weight': weight,
        'age': age,
        'height': height
    }


    basal_metabolism = 0.0
    daily_calorie_requirement = 0.0
    
    if gender == 'male':
        basal_metabolism = 66 + (13.7 * float(weight)) + (5 * float(height)) - (6.8 * float(age))
        
    if gender == 'female':
        basal_metabolism = 655 + (9.6 * float(weight)) + (1.8 * float(height)) - (4.7 * float(age))

    if activity == 'no':
        daily_calorie_requirement = basal_metabolism * 1.2

    if activity == 'low':
        daily_calorie_requirement = basal_metabolism * 1.375

    if activity == 'middle':
        daily_calorie_requirement = basal_metabolism * 1.55

    if activity == 'high':
        daily_calorie_requirement = basal_metabolism * 1.725

    if activity == 'super':
        daily_calorie_requirement = basal_metabolism * 1.9
    
    daily_calorie_requirement = int(daily_calorie_requirement)

    data = {
        'daily_calorie_requirement': daily_calorie_requirement
    }
    
    return JsonResponse(data)
            
def calories_view(request, *args, **kwargs):

    data = request.POST

    # Get data from user.
    username  = data.get('username')
    gender = data.get('gender')
    activity = data.get('activity')
    weight = data.get('weight')
    age = data.get('age')
    height = data.get('height')

    print(f'Пол: {gender}')
    print(f'Активность: {activity}')
    print(f'Пользователь: {username}')
    print(f'Вес: {weight}')
    print(f'Рост: {height}')
    print(f'Возраст: {age}')

    # Print types.
    print(f'Пол (тип): {type(gender)}')
    print(f'Активность (тип): {type(activity)}')
    print(f'Пользователь (тип): {type(username)}')
    print(f'Вес (тип): {type(weight)}')
    print(f'Рост (тип): {type(height)}')
    print(f'Возраст (тип): {type(age)}')


    basal_metabolism = 0.0
    daily_calorie_requirement = 0.0
    
    if gender == 'male':
        basal_metabolism = 66 + (13.7 * float(weight)) + (5 * float(height)) - (6.8 * float(age))
        
    if gender == 'female':
        basal_metabolism = 655 + (9.6 * float(weight)) + (1.8 * float(height)) - (4.7 * float(age))

    if activity == 'no':
        daily_calorie_requirement = basal_metabolism * 1.2

    if activity == 'low':
        daily_calorie_requirement = basal_metabolism * 1.375

    if activity == 'middle':
        daily_calorie_requirement = basal_metabolism * 1.55

    if activity == 'high':
        daily_calorie_requirement = basal_metabolism * 1.725

    if activity == 'super':
        daily_calorie_requirement = basal_metabolism * 1.9
    
    daily_calorie_requirement = int(daily_calorie_requirement)

    print(f'Величина основного обмена: {basal_metabolism}')
    print(f'Суточная потребность в калориях: {daily_calorie_requirement}')

    return render(request, "calories.html", locals())
