from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from Book.models import Book, Comments, Pay
from Book.forms import CommentForm
# from django.contrib import auth
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def books(request):
    return render(request, 'books.html', {'books': Book.objects.all(), 'username': request.user.username})


# Тож вроде норм
def only_one_book(request, book_id):
    context = {}
    context['book'] = get_object_or_404(Book, id=book_id)
    context['comments'] = Comments.objects.filter(comments_books_id=book_id)
    context['form'] = CommentForm
    context['username'] = request.user.username
    return render(request, 'book.html', context)

# Вродь норм
def add_like(request, book_id):
    if book_id in request.COOKIES:
        return redirect('/')
    else:
        book = get_object_or_404(Book, id=book_id)
        book.likes += 1
        book.save()
        response = redirect('/')
        response.set_cookie(book_id, "like")
        return response

# Систему регистрации, лайк, посты были, трай убрать, база - сеты.

# Вроде щас тоже ништяк, если аноним пытается добавить коммент - редиректим на страицу логина
@login_required
def add_comment(request, book_id):
    if request.GET and ('pause' not in request.session):
        form = CommentForm(request.GET)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_books = Book.objects.get(id=book_id)
            form.save()
            request.session.set_expiry(10)
            request.session['pause'] = True
    return redirect('/books/get/%s/' % book_id)


# Ну щас вроде норм)
def my_books(request):
    args = {}
    mass = request.user.book_set.all()      # Я люблю эту функцию <3
    sum = 0
    for x in mass:      # Знаю, что здесь хрень, но Матан не ждет  =)
        sum += x.price
    args['books'] = mass
    args['username'] = request.user.username
    args['Pays'] = Pay.objects.all()
    args['sum'] = sum
    return render(request, 'user_books.html', args)

# Не работает логика с токеном
@login_required
def add_in_list(request, book_id):
    context = {}
    context['username'] = request.user.username
    a = Book.objects.get(id=book_id)
    context['book'] = a
    context['form'] = CommentForm()
    context['comments'] = Comments.objects.filter(comments_books_id=book_id)
    if request.method == "POST":
        mass = request.user.book_set.all()
        if a in mass:
            error = True
            context['error'] = error
            return render(request, 'book.html', context)
        else:
            a.owns_names.add(request.user)
            a.save()
            return redirect('/books/get/%s/buy/thx/' %book_id)
    return render(request, 'book.html', context)

def thx(request, book_id):
     return render(request, 'thx_for_buy.html', {'username': request.user.username,})

@login_required
def choice(request):
    context = {}
    context['username'] = request.user.username
    return render(request, 'money.html', context)

@login_required
def accepted(request):
    context = {}
    context['username'] = request.user.username
    if request.method == "POST":
        return render(request, 'accepted.html', context)
    else:
        return redirect('/my_books/choice/')