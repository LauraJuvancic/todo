from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.forms import model_to_dict
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from datetime import timedelta


# Create your views here.

def first(request):
    context = {}
    context['forml'] = formLogin()
    if request.method == 'POST':
        forml = formLogin(request.POST)
        if forml.is_valid():
            user = authenticate(username=forml.cleaned_data['username'], password=forml.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('Homepage/')


    if request.user.is_authenticated:
        return HttpResponseRedirect('Homepage/')

    return render(request, 'todo/base.html', context)

@login_required(login_url='')
def index(request):
    context = {}

    if request.method == 'POST':
        if 'addhome' in request.POST:
            formh = formHome(request.POST)
            if formh.is_valid():
                t = Tasks(name=formh.cleaned_data['name'], date=formh.cleaned_data['date'],
                          category="Home", completed=False, user=request.user,
                          alarm=formh.cleaned_data['alarm'])
                t.save()

                h = Home(name=formh.cleaned_data['name'], date=formh.cleaned_data['date'],
                         info=formh.cleaned_data['info'], alarm=formh.cleaned_data['alarm'],
                         task=t)
                h.save()

        elif 'addwork' in request.POST:
            formw = formWork(request.POST)
            if formw.is_valid():
                t = Tasks(name=formw.cleaned_data['name'], date=formw.cleaned_data['date'],
                          category="Work", completed=False, user=request.user,
                          alarm=formw.cleaned_data['alarm'])
                t.save()

                w = Work(name=formw.cleaned_data['name'], date=formw.cleaned_data['date'],
                         info=formw.cleaned_data['info'], mails=formw.cleaned_data['mails'],
                         workers=formw.cleaned_data['workers'], alarm=formw.cleaned_data['alarm'],
                         task=t)
                w.save()
        elif 'addpersonal' in request.POST:
            formp = formPersonal(request.POST)
            if formp.is_valid():
                t = Tasks(name=formp.cleaned_data['name'], date=formp.cleaned_data['date'],
                          category="Personal", completed=False, user=request.user,
                          alarm=formp.cleaned_data['alarm'])
                t.save()

                p = Personal(name=formp.cleaned_data['name'], date=formp.cleaned_data['date'],
                         info=formp.cleaned_data['info'], alarm=formp.cleaned_data['alarm'],
                         task=t)
                p.save()

        elif 'addtravel' in request.POST:
            formt = formTravel(request.POST or None)
            if formt.is_valid():
                t = Tasks(name=formt.cleaned_data['name'], date=formt.cleaned_data['departure'],
                          category="Travel", completed=False, user=request.user,
                          alarm=formt.cleaned_data['alarm'])
                t.save()

                tr = Travel(name=formt.cleaned_data['name'], arrival=formt.cleaned_data['arrival'],
                            departure=formt.cleaned_data['departure'], destination=formt.cleaned_data['destination'],
                            pack=formt.cleaned_data['pack'], info=formt.cleaned_data['info'],
                            alarm=formt.cleaned_data['alarm'],
                            task=t)
                tr.save()
            else:
                return HttpResponse("Drek")
        elif 'addshopping' in request.POST:
            forms = formShopping(request.POST)
            if forms.is_valid():
                t = Tasks(name=forms.cleaned_data['name'], date=forms.cleaned_data['date'],
                          category="Shopping", completed=False, user=request.user,
                          alarm=forms.cleaned_data['alarm'])
                t.save()

                s = Shopping(name=forms.cleaned_data['name'], date=forms.cleaned_data['date'],
                         stuff=forms.cleaned_data['stuff'], alarm=forms.cleaned_data['alarm'],
                         task=t)
                s.save()
        elif 'addbirthday' in request.POST:
            formb = formBirthday(request.POST)
            if formb.is_valid():
                t = Tasks(name=formb.cleaned_data['name'], date=formb.cleaned_data['date'],
                          category="Birthday", completed=False, user=request.user,
                          alarm=formb.cleaned_data['alarm'])
                t.save()

                b = Birthday(name=formb.cleaned_data['name'], date=formb.cleaned_data['date'],
                            presents=formb.cleaned_data['presents'], alarm=formb.cleaned_data['alarm'],
                            task=t)
                b.save()
        elif 'addcooking' in request.POST:
            formc = formCooking(request.POST)
            if formc.is_valid():
                t = Tasks(name=formc.cleaned_data['name'], date=formc.cleaned_data['date'],
                          category="Cooking", completed=False, user=request.user,
                          alarm=formc.cleaned_data['alarm'])
                t.save()

                c = Cooking(name=formc.cleaned_data['name'], date=formc.cleaned_data['date'],
                            ingredients=formc.cleaned_data['ingredients'], procedure=formc.cleaned_data['procedure'],
                            alarm=formc.cleaned_data['alarm'],
                            task=t)
                c.save()

    formh = formHome()
    formw = formWork()
    formp = formPersonal()
    formt = formTravel()
    forms = formShopping()
    formb = formBirthday()
    formc = formCooking()

    transaction.commit()
    tasks = Tasks.objects.filter(user=request.user, date=datetime.now().date())
    how_many_days = 30
    min=datetime.today()-timedelta(days=1)
    past = Tasks.objects.filter(user=request.user,
                                date__gte=datetime.today()-timedelta(days=how_many_days),
                                completed=False).exclude(date__gte=datetime.today())

    future = Tasks.objects.filter(user=request.user, date__lte=datetime.today()+timedelta(days=how_many_days), alarm=True,
                                  completed=False)


    context = {'formh': formh, 'formw': formw, 'formp': formp, 'formt': formt, 'forms': forms, 'formb': formb,
             'formc': formc, 'tasks_today': tasks, 'past': past, 'future': future}

    return render(request, 'todo/index.html', context)

@login_required(login_url='')
def home(request):
    context = {}

    transaction.commit()
    context['tasks_progress'] = Tasks.objects.filter(user=request.user, category="Home", completed=False)
    context['tasks_completed'] = Tasks.objects.filter(user=request.user, category="Home", completed=True)

    how_many_days = 30
    context['past'] = Tasks.objects.filter(user=request.user, date__gte=datetime.now() - timedelta(days=how_many_days),
                                           completed=False).exclude(date__gte=datetime.today())
    context['future'] = Tasks.objects.filter(user=request.user, date__lte=datetime.now() + timedelta(days=how_many_days),
                                  alarm=True, completed=False)

    return render(request, 'todo/details.html', context)

@login_required(login_url='')
def work(request):
    context = {}


    context['tasks_progress'] = Tasks.objects.filter(user=request.user, category="Work", completed=False)
    context['tasks_completed'] = Tasks.objects.filter(user=request.user, category="Work", completed=True)

    how_many_days = 30
    context['past'] = Tasks.objects.filter(user=request.user, date__gte=datetime.now() - timedelta(days=how_many_days),
                                           completed=False).exclude(date__gte=datetime.today())
    context['future'] = Tasks.objects.filter(user=request.user,
                                             date__lte=datetime.now() + timedelta(days=how_many_days),
                                             alarm=True, completed=False)
    return render(request, 'todo/details.html', context)

@login_required(login_url='')
def personal(request):
    context = {}


    context['tasks_progress'] = Tasks.objects.filter(user=request.user, category="Personal", completed=False)
    context['tasks_completed'] = Tasks.objects.filter(user=request.user, category="Personal", completed=True)

    how_many_days = 30
    context['past'] = Tasks.objects.filter(user=request.user, date__gte=datetime.now() - timedelta(days=how_many_days),
                                           completed=False).exclude(date__gte=datetime.today())
    context['future'] = Tasks.objects.filter(user=request.user,
                                             date__lte=datetime.now() + timedelta(days=how_many_days),
                                             alarm=True, completed=False)

    return render(request, 'todo/details.html', context)

@login_required(login_url='')
def travel(request):
    context = {}


    context['tasks_progress'] = Tasks.objects.filter(user=request.user, category="Travel", completed=False)
    context['tasks_completed'] = Tasks.objects.filter(user=request.user, category="Travel", completed=True)

    how_many_days = 30
    context['past'] = Tasks.objects.filter(user=request.user, date__gte=datetime.now() - timedelta(days=how_many_days),
                                           completed=False).exclude(date__gte=datetime.today())
    context['future'] = Tasks.objects.filter(user=request.user,
                                             date__lte=datetime.now() + timedelta(days=how_many_days),
                                             alarm=True, completed=False)

    return render(request, 'todo/details.html', context)

@login_required(login_url='')
def shopping(request):
    context = {}


    context['tasks_progress'] = Tasks.objects.filter(user=request.user, category="Shopping", completed=False)
    context['tasks_completed'] = Tasks.objects.filter(user=request.user, category="Shopping", completed=True)

    how_many_days = 30
    context['past'] = Tasks.objects.filter(user=request.user, date__gte=datetime.now() - timedelta(days=how_many_days),
                                           completed=False).exclude(date__gte=datetime.today())
    context['future'] = Tasks.objects.filter(user=request.user,
                                             date__lte=datetime.now() + timedelta(days=how_many_days),
                                             alarm=True, completed=False)

    return render(request, 'todo/details.html', context)

@login_required(login_url='')
def birthday(request):
    context = {}


    context['tasks_progress'] = Tasks.objects.filter(user=request.user, category="Birthday", completed=False)
    context['tasks_completed'] = Tasks.objects.filter(user=request.user, category="Birthday", completed=True)

    how_many_days = 30
    context['past'] = Tasks.objects.filter(user=request.user, date__gte=datetime.now() - timedelta(days=how_many_days),
                                           completed=False).exclude(date__gte=datetime.today())
    context['future'] = Tasks.objects.filter(user=request.user,
                                             date__lte=datetime.now() + timedelta(days=how_many_days),
                                             alarm=True, completed=False)

    return render(request, 'todo/details.html', context)

@login_required(login_url='')
def cooking(request):
    context = {}


    context['tasks_progress'] = Tasks.objects.filter(user=request.user, category="Cooking", completed=False)
    context['tasks_completed'] = Tasks.objects.filter(user=request.user, category="Cooking", completed=True)

    how_many_days = 30
    context['past'] = Tasks.objects.filter(user=request.user, date__gte=datetime.now() - timedelta(days=how_many_days),
                                           completed=False).exclude(date__gte=datetime.today())
    context['future'] = Tasks.objects.filter(user=request.user,
                                             date__lte=datetime.now() + timedelta(days=how_many_days),
                                             alarm=True, completed=False)
    return render(request, 'todo/details.html', context)

@login_required(login_url='')
def days(request):
    context={}

    context['day1'] = Tasks.objects.filter(user=request.user, date=datetime.now()+timedelta(days=1))
    context['day2'] = Tasks.objects.filter(user=request.user, date=datetime.now()+timedelta(days=2))
    context['day3'] = Tasks.objects.filter(user=request.user, date=datetime.now()+timedelta(days=3))
    context['day4'] = Tasks.objects.filter(user=request.user, date=datetime.now()+timedelta(days=4))
    context['day5'] = Tasks.objects.filter(user=request.user, date=datetime.now()+timedelta(days=5))
    context['day6'] = Tasks.objects.filter(user=request.user, date=datetime.now()+timedelta(days=6))
    context['day7'] = Tasks.objects.filter(user=request.user, date=datetime.now()+timedelta(days=7))

    how_many_days = 30
    context['past'] = Tasks.objects.filter(user=request.user, date__gte=datetime.now() - timedelta(days=how_many_days),
                                           completed=False).exclude(date__gte=datetime.today())
    context['future'] = Tasks.objects.filter(user=request.user,
                                             date__lte=datetime.now() + timedelta(days=how_many_days),
                                             alarm=True, completed=False)

    return render(request, 'todo/7days.html', context)

@login_required(login_url='')
def showDetails(request, idt):
    context={}

    t = Tasks.objects.get(id=idt)
    cat = t.category

    context['t'] = t

    if (cat=="Home"):
        form = formHome(data=model_to_dict(Home.objects.get(task=t)))
    elif (cat=="Work"):
        form = formWork(data=model_to_dict(Work.objects.get(task=t)))
    elif(cat=="Personal"):
        form = formPersonal(data=model_to_dict(Personal.objects.get(task=t)))
    elif(cat=="Travel"):
        form = formTravel(data=model_to_dict(Travel.objects.get(task=t)))
    elif(cat=="Shopping"):
        form = formShopping(data=model_to_dict(Shopping.objects.get(task=t)))
    elif(cat=="Birthday"):
        form = formBirthday(data=model_to_dict(Birthday.objects.get(task=t)))
    elif(cat=="Cooking"):
        form = formCooking(data=model_to_dict(Cooking.objects.get(task=t)))
    else:
        form={}
        c={}

    context['form'] = form
    context['options'] = ['Home', 'Work', 'Personal', 'Travel', 'Shopping', 'Birthday', 'Cooking']

    how_many_days = 30
    context['past'] = Tasks.objects.filter(user=request.user, date__gte=datetime.now() - timedelta(days=how_many_days),
                                           completed=False).exclude(date__gte=datetime.today())
    context['future'] = Tasks.objects.filter(user=request.user,
                                             date__lte=datetime.now() + timedelta(days=how_many_days),
                                             alarm=True, completed=False)

    return render(request, 'todo/edit.html', context)

@login_required(login_url='/todo/')
def updateView(request, idt):
    context={}

    if request.method == 'POST':
        category = request.POST['category']

        if(category == "Home"):
            al = request.POST.get('alarm', 0)
            if (al == 0):
                bool = False
            else:
                bool = True

            t = Tasks.objects.get(id=idt)
            t.name = request.POST['name']
            t.date = request.POST['date']
            t.alarm = bool
            t.save()
            Home.objects.filter(task=t).update(name=request.POST['name'], date=request.POST['date'],
                                                 info=request.POST['info'], alarm=bool)


            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        elif (category == "Work"):
            al = request.POST.get('alarm', 0)
            if(al == 0):
                bool = False
            else:
                bool = True

            t = Tasks.objects.get(id=idt)
            t.name = request.POST['name']
            t.date = request.POST['date']
            t.alarm = bool
            t.save()
            Work.objects.filter(task=t).update(name=request.POST['name'], date=request.POST['date'],
                                                 info=request.POST['info'], mails=request.POST['mails'],
                                                 workers=request.POST['workers'], alarm=bool)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        elif (category == "Personal"):
            al = request.POST.get('alarm', 0)
            if (al == 0):
                bool = False
            else:
                bool = True

            t = Tasks.objects.get(id=idt)
            t.name = request.POST['name']
            t.date = request.POST['date']
            t.alarm = bool
            t.save()
            Personal.objects.filter(task=t).update(name=request.POST['name'], date=request.POST['date'],
                                                     info=request.POST['info'], alarm=bool)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        elif (category == "Travel"):
            al = request.POST.get('alarm', 0)
            if (al == 0):
                bool = False
            else:
                bool = True

            t = Tasks.objects.get(id=idt)
            t.name = request.POST['name']
            t.date = request.POST['departure']
            t.alarm = bool
            t.save()

            Travel.objects.filter(task=t).update(name=request.POST['name'], departure=request.POST['departure'],
                                                   arrival=request.POST['arrival'], destination=request.POST['destination'],
                                                   pack=request.POST['pack'], info=request.POST['info'],
                                                   alarm=bool)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        elif (category == "Shopping"):
            al = request.POST.get('alarm', 0)
            if (al == 0):
                bool = False
            else:
                bool = True

            t = Tasks.objects.get(id=idt)
            t.name = request.POST['name']
            t.date = request.POST['date']
            t.alarm = bool
            t.save()

            Shopping.objects.filter(task=t).update(name=request.POST['name'], date=request.POST['date'],
                                                     stuff=request.POST['stuff'], alarm=bool)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        elif (category == "Birthday"):
            al = request.POST.get('alarm', 0)
            if (al == 0):
                bool = False
            else:
                bool = True

            t = Tasks.objects.get(id=idt)
            t.name = request.POST['name']
            t.date = request.POST['date']
            t.alarm = bool
            t.save()

            Birthday.objects.filter(task=t).update(name=request.POST['name'], date=request.POST['date'],
                                                     presents=request.POST['presents'], alarm=bool)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        elif (category == "Cooking"):
            al = request.POST.get('alarm', 0)
            if (al == 0):
                bool = False
            else:
                bool = True

            t = Tasks.objects.get(id=idt)
            t.name = request.POST['name']
            t.date = request.POST['date']
            t.alarm = bool
            t.save()

            Cooking.objects.filter(task=t).update(name=request.POST['name'], date=request.POST['date'],
                                                    ingredients=request.POST['ingredients'],
                                                    procedure=request.POST['procedure'], alarm=bool)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    return render(request, 'todo/edit.html', context)

@login_required(login_url='')
def deleteView(request, idt):
    t = Tasks.objects.get(id=idt)
    cat = t.category

    if (cat=="Home"):
        Home.objects.filter(task=t).delete()
    elif (cat=="Work"):
        Work.objects.filter(task=t).delete()
    elif(cat=="Personal"):
        Personal.objects.filter(task=t).delete()
    elif(cat=="Travel"):
        Travel.objects.filter(task=t).delete()
    elif(cat=="Shopping"):
        Shopping.objects.filter(task=t).delete()
    elif(cat=="Birthday"):
        Birthday.objects.filter(task=t).delete()
    elif(cat=="Cooking"):
        Cooking.objects.filter(task=t).delete()

    t.delete()
    return HttpResponseRedirect(reverse('todo:index'))


@login_required(login_url='')
def completeTask(request, idt):
    t = Tasks.objects.get(id=idt)
    c = request.POST.get('compl', 0)
    if (c == 0):
        bool = False
    else:
        bool = True

    if request.method == 'POST':
        if bool:
            t.completed = True
            t.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            t.completed = False
            t.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('todo:first'))


def signup(request):
    context={}

    if request.method == 'POST':
        form = formSignup(request.POST)
        forml = formLogin(request.POST)
        if request.POST.get("signup"):
            if form.is_valid():
                usr = User.objects.create_user(username=form.cleaned_data['username'], first_name=form.cleaned_data['first_name'],
                                               last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'],
                                               password=form.cleaned_data['password'])

                login(request, usr)
                return HttpResponseRedirect(reverse('todo:index'))
        elif request.POST.get("login"):
            if forml.is_valid():
                user = authenticate(username=forml.cleaned_data['username'], password=forml.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('Homepage/')

    context['form'] = formSignup()
    context['forml'] = formLogin()

    return render(request, 'todo/signup.html', context)

@login_required(login_url='')
def showUser(request, idu):
    context={}
    form = formEditprofile(data=model_to_dict(User.objects.get(id=idu)))
    context['form'] = form

    how_many_days = 30
    context['past'] = Tasks.objects.filter(user=request.user, date__gte=datetime.now() - timedelta(days=how_many_days),
                                           completed=False).exclude(date__gte=datetime.today())
    context['future'] = Tasks.objects.filter(user=request.user,
                                             date__lte=datetime.now() + timedelta(days=how_many_days),
                                             alarm=True, completed=False)
    return render(request, 'todo/editprofile.html', context)

@login_required(login_url='')
def updateUser(request, idu):
    context={}

    if request.method == 'POST':
        usr = User.objects.get(id=idu)
        usr.first_name = request.POST['first_name']
        usr.last_name = request.POST['last_name']
        usr.email = request.POST['email']
        usr.username = request.POST['username']

        if (request.POST['password']!=""):
            usr.set_password(request.POST['password'])

        usr.save()
        login(request, usr)
        return HttpResponseRedirect(reverse('todo:showUser',args=(idu,)))

    return render(request, 'todo/editprofile.html', context)

