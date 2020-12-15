from django.shortcuts import render
from django.http import HttpResponse
import random

min_length = 6
max_length = 14
min_password = 1
max_password = 10


def home(request):
    return render(request, 'generator/index.html', {'length_range': range(min_length, max_length + 1),
                                                    'nums_of_password': range(min_password, max_password + 1)})


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('specials'):
        characters.extend(list('!@#$%^&*()_+'))

    length = int(request.GET.get('length', max_length))
    nums_of_password = int(request.GET.get('nums_of_password', max_length))
    if not min_length <= length <= max_length:
        length = 12

    if not min_password <= nums_of_password <= max_password:
        nums_of_password = min_password

    generated_passwords = []
    for _ in range(nums_of_password):
        thepassword = ''
        for x in range(length):
            thepassword += random.choice(characters)
        generated_passwords.append(thepassword)

    return render(request, 'generator/password.html',
                  {'passwords': generated_passwords})


def about(request):
    return render(request, 'generator/about.html')
