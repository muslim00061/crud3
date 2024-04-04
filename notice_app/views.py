from django.shortcuts import render,redirect, get_object_or_404
from .models import Category,Board
from .forms import AddBoardForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm


def home_page(requeset):
    categories = Category.objects.all()
    boards = Board.objects.all().order_by('posted_date')[:8]

    context = {
        'categories': categories,
        'boards': boards
    }

    return render(requeset, "./home_page.html", context)
#create
def add_board_page(request):
    if request.method == "POST":
        form = AddBoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = AddBoardForm

        context = {
            'form': form
        }

        return render(request, "./add_board_page.html", context)
#view
def board_detail_page(request,pk):
    board = get_object_or_404(Board, pk=pk)
    context = {
        'board': board
    }

    return render(request, "board_detail_page.html", context)
#delete
def delete_board_page(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        board.delete()
        return redirect("home_page")
    else:
        context = {'board': board}
        return render(request, "delete_board_page.html", context)
#update
def edit_board_page(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == "POST":
        form = AddBoardForm(request.POST or None, request.FILES or None, instance=board)
        if form.is_valid():
            form.save()
            return redirect("board_detail_page", pk=board.pk)
    else:
        # Если это GET-запрос, просто создайте форму с существующими данными доски
        form = AddBoardForm(instance=board)

    context = {
        'board': board,
        'form': form
    }

    return render(request, "./edit_board_page.html", context)

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")

    else:
        form = NewUserForm()

    context = {
        'form': form
    }

    return render(request,"./sign_up.html", context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("home_page")
    else:
        form=AuthenticationForm

    context = {
        'form': form
    }
    return render(request, "./login.html", context)

def logout_request(request):
    logout(request)
    return redirect("home_page")

