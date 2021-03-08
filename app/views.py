from django.shortcuts import render
from django.http import HttpResponse


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True,
    })


def user_number(request, phone):
    return HttpResponse(f"This number {phone} is valid for Ukraine")


def uuid(request, uuid):
    return HttpResponse("You give me this {}".format(uuid))


def first(request):
    return render(request, "first.html")


def articles(request):
    return render(request, "articles.html")


def archive(request, article_number=""):
    return render(request, "archive.html", {"number": article_number})


def number(request, article_number, slug_text=""):
    return render(request, "number.html", {"number": article_number,
                                           "text": slug_text})


def users(request):
    return HttpResponse("The users page")
