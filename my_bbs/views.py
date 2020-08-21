from django.shortcuts import render, redirect, get_object_or_404
from my_bbs.models import Board, Comment
from my_bbs.forms import BoardForm, CommentForm
######################################################
from .forms import SignupForm, SigninForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.models import User
#######################################################
from django.contrib.auth import login, authenticate, logout
######################################################
from django.contrib.auth.decorators import login_required
#######################################################


def p_list(request):
    board_list = Board.objects.all().order_by('-id')

    return render(request, 'list.html', {'my_bbs': board_list})


def p_create(request):
    if not request.session.get('user'):
        return redirect('/my_bbs/signin')
        # return redirect('/my_bbs/list')
    # POST 방식호출
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            user_id = request.session.get('user')
            board_form.instance.author = user_id
            board_form.save()
            return redirect('my_bbs:list')

    # GET 방식 호출 form방식이 아니면 모두 GET 방식
    else:
        board_form = BoardForm()

    return render(request, 'create.html', {'board_form': board_form})


@login_required
def p_delete(request, board_id):
    board = Board.objects.get(id=board_id)
    board.delete()
    return redirect('my_bbs:list')


@login_required
def p_update(request, board_id):

    board = get_object_or_404(Board, pk=board_id)
    # POST 방식호출
    if request.method == 'POST':
        board_form = BoardForm(request.POST, instance=board)
        if board_form.is_valid():
            board_form.save()
            return redirect('my_bbs:list')

    # GET 방식 호출 form방식이 아니면 모두 GET 방식
    else:
        board_form = BoardForm(instance=board)

    return render(request, 'create.html', {'board_form': board_form})


def c_list(request, board_id):
    board_list = get_object_or_404(Board, pk=board_id)
    context = {'board': board_list}
    return render(request, 'comment.html', context)

@login_required
def c_create(request, board_id):
    # POST 방식호출
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            user_id = request.session.get('user')
            comment_form.instance.board_id_id = board_id
            comment_form.instance.author = user_id
            comment_form.save()
            return redirect('my_bbs:comment', board_id)

    # GET 방식 호출 form방식이 아니면 모두 GET 방식
    else:
        comment_form = CommentForm()

    return render(request, 'c_create.html', {'comment_form': comment_form})


def c_delete(request, ct_id):
    comment = Comment.objects.get(id=ct_id)
    comment.delete()

    return redirect('my_bbs:comment', comment.board_id.pk)


################################################################################################
# 계정 만들기

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'f': SignupForm()})

    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
                new_user.save()

                return HttpResponseRedirect(reverse('my_bbs:list'))
            else:
                return render(request, 'signup.html', {'f': form, 'error': '비밀번호 오류'})
        else:
            return render(request, 'signup.html', {'f': form})

##############################################################################################
# 로그인


def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html', {'f': SigninForm})

    elif request.method == "POST":
        form = SigninForm(request.POST)
        id = request.POST['username']
        pw = request.POST['password']
        u = authenticate(username=id, password=pw)
        if u:
            request.session['user'] = u.username
            login(request, user=u)
            return HttpResponseRedirect(reverse('my_bbs:list'))
        else:
            return render(request, 'signin.html', {'f': form, 'error': '아이디나 비밀번호 오류'})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('my_bbs:list'))

#
