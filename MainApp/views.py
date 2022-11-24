from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet, Comment
from MainApp.forms import SnippetForm, UserRegistrationForm, CommentForm
from django.contrib import auth
from django.db.models import Q


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form,
        }
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == "POST":
        # print("form data:", list(request.POST.items()))
        # snippet = Snippet(
        #     name=request.POST["name"],
        #     lang=request.POST["lang"],
        #     code=request.POST["code"]
        # )
        # snippet.save()
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
        return redirect("snippets-list")


def snippet_delete(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    snippet.delete()
    return redirect("snippets-list")


def snippet_edit(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    comment_form = CommentForm()
    comments = snippet.comments.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippet': snippet,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'pages/show_snippet.html', context)


def snippets_page(request):
    filter = request.GET.get('filter')
    if filter:
        pagename = 'Мои сниппеты'
        if request.user.is_authenticated:
            snippets = Snippet.objects.filter(user=request.user)
        else:
            return redirect("snippets-list")
    else:
        pagename = 'Просмотр сниппетов'
        if request.user.is_authenticated:
            snippets = Snippet.objects.filter(Q(public=True) | Q(user=request.user))
        else:
            snippets = Snippet.objects.exclude(public=False)
    context = {
        'pagename': pagename,
        'snippets': snippets
    }
    return render(request, 'pages/view_snippets.html', context)


def show_snippet_page(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    comment_form = CommentForm()
    comments = snippet.comments.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippet': snippet,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'pages/show_snippet.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # print("SUCCESS")
        else:
            # Return error message
            pass
        return redirect(request.META.get('HTTP_REFERER', '/'))

    else:
        raise Http404


def logout_page(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def registration(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        context = {
            'form': form
        }
        return render(request, 'pages/registration.html', context)
    elif request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form
            }
            return render(request, 'pages/registration.html', context)


def comment_add(request):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        snippet_id = request.POST["snippet_id"]
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            print("COMMENT USER", request.user)
            comment.snippet = Snippet.objects.get(id=snippet_id)
            comment.save()
            return redirect("snippet-show", snippet_id)
    raise Http404
