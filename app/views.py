from django.contrib import messages
from django.shortcuts import render, redirect
from app.forms import UserForm
from app.models import User, History


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['username'] = username
                return redirect('calculator')
        except Exception as e:
            return render(request, 'login.html')
    return render(request, 'login.html')


def calculator(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            expression = request.POST['expression']
            result = None
            try:
                result = eval(expression)
            except SyntaxError:
                result = 'Alphabets not allowed'
            except ZeroDivisionError:
                    result = 'undefined:Division by zero'
            new_history = History.objects.create(expression=expression, result=result)
            print(new_history.result)
            new_history.save()
            context = {'expression': expression, 'result': result}
            return render(request, 'calculator.html', context=context)
        return render(request, 'calculator.html')
    else:
        messages.add_message(request, messages.INFO, 'Login First')
        return render(request, 'login.html')


def register(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Account Created. Please Login')
            return render(request, 'login.html')
    context = {'form': form}
    return render(request, 'register.html', context)


def history(request):
    if request.session.has_key('username'):
        histories = History.objects.all()
        context = {'histories': histories}
        return render(request, 'history.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Login First')
        return render(request, 'login.html')


def profile(request):
    if request.session.has_key('username'):
        username = request.session.get('username')
        user = User.objects.get(username=username)
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']
            user.first_name = first_name
            user.last_name = last_name
            user.password = password
            user.save()
            return redirect('calculator')
        context = {'user': user}
        return render(request, 'profile.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Login First')
        return render(request, 'login.html')


def logout(request):
    try:
        request.session.flush()
        del request.session['username']
    except:
        pass
    messages.add_message(request, messages.INFO, 'Logged out Successfully')
    return render(request, 'login.html')
