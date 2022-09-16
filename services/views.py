from django.shortcuts import render, HttpResponse
import random

honor = {'vodo': 'Водолеи очень веселые',
         'leo': 'Львы тупые'}


def index(request):
    a = random.randrange(5)
    return render(request, 'index.html', {'b': a})


def page(request, page_num):
    honor_dict = {'vodo': 'Водолеи очень веселые',
             'leo': 'Львы тупые'}
    honor = list(honor_dict)
    honor_b = {
        'honors': honor_dict
    }
    h={
        'h':honor
    }
    a = random.randrange(5)
    return render(request, 'page.html', {'page_num':page_num,
                                    'honor_b':honor_dict,
                                    'h':h})
