from django.shortcuts import render, render_to_response,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Datos, Profile, Meeting
from forms import UserForm, ProfileForm, PForm, Prof1Form, Profile1Form, DatosForm, LoginForm
from django.contrib import messages
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from django.views import generic
from django.http import Http404


@transaction.atomic
def signup_user(request):
    print "Signup-----"
    if request.method == 'POST':
        print "100"
        form = SignUpForm(request.POST)
        if form.is_valid():
            print "200"
            user = form.save(commit=False)
#            user.refresh_from_db()  # load the profile instance created by the signal

            print "210"
            user.is_active = False
            user.save()
            print "1"

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            print "2"

            return redirect('account_activation_sent')
        else:
            print "99"
    else:
        print "3"
        form = SignUpForm()
    print "4"
    return render(request, 'registration/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def home(request):
    return render(request, 'mentor/home.html')


def dashboard(request):

    stat = {'participants': 0}

    stat['mentors'] = 0
    stat['interest_in_technology'] = 0
    stat['interest_in_marketing'] = 0
    stat['interest_in_legal'] = 0
    stat['interest_in_leadership'] = 0
    stat['interest_in_business'] = 0
    stat['interest_in_operations'] = 0
    stat['interest_in_investments'] = 0
    stat['interest_in_professional_development'] = 0

    stat['mentees'] = 0
    stat['learn_technology'] = 0
    stat['learn_marketing'] = 0
    stat['learn_legal'] = 0
    stat['learn_leadership'] = 0
    stat['learn_business'] = 0
    stat['learn_operations'] = 0
    stat['learn_investments'] = 0
    stat['learn_professional_development'] = 0

    query_results = Profile.objects.all()
    for i in query_results:
        stat['participants'] += 1
        if i.mentor:
            stat['mentors'] += 1
        if i.interest_in_technology:
            stat['interest_in_technology'] += 1

        if i.interest_in_marketing:
            stat['interest_in_marketing'] += 1
        if i.interest_in_legal:
            stat['interest_in_legal'] += 1
        if i.interest_in_leadership:
            stat['interest_in_leadership'] += 1
        if i.interest_in_business:
            stat['interest_in_business'] += 1
        if i.interest_in_operations:
            stat['interest_in_operations'] += 1
        if i.interest_in_investments:
            stat['interest_in_investments'] += 1
        if i.interest_in_professional_development:
            stat['interest_in_professional_development'] += 1

        if i.mentee:
            stat['mentees'] += 1
        if i.learn_technology:
            stat['learn_technology'] += 1
        if i.learn_marketing:
            stat['learn_marketing'] += 1
        if i.learn_legal:
            stat['learn_legal'] += 1
        if i.learn_leadership:
            stat['learn_leadership'] += 1
        if i.learn_business:
            stat['learn_business'] += 1
        if i.learn_operations:
            stat['learn_operations'] += 1
        if i.learn_investments:
            stat['learn_investments'] += 1
        if i.learn_professional_development:
            stat['learn_professional_development'] += 1

    return render(request, 'dashboard/dashboard.html', {'stat': stat})


@login_required
def meeting(request):
    return render(request, 'meeting/meeting.html')


@login_required
def calendar(request):
    return render(request, 'meeting/calendar.html')


######
######
@login_required
@transaction.atomic
def crispy(request):
    user_form = UserForm(instance=request.user)
    profile_form = Profile1Form(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = Profile1Form(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
    return render(request, 'mentor/crispy.html', {'user_form': user_form,
                                                  'profile_form': profile_form})


def fancy(request):

    if request.method == 'GET':
        print "GET"
        datos = {'phone':'(555)555-5555'}
        datos['facebook'] = 'zavala55'
    if request.method == 'POST':
        valor = request.POST.get('facebook')
        print "Valor: ", valor
        datos = {'phone':'(999)999-9999'}

        print "POST", request.POST
        print request.META
#        print "\n",request.META['QUERY_STRING']
        print "FACEBOOK: ", request.POST.get('facebook')
        datos['facebook']= request.POST.get('facebook')

    return render(request, 'mentor/fancy.html', {'datos':datos})


def login_user(request):
    logout(request)
#    username = password = ''
    if request.POST:
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')

    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'mentor/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
@transaction.atomic
def account_settings(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    print "ACC 1"

    if request.method == 'POST':
        print "ACC 2"
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        print "ACC 3"
        if user_form.is_valid():
            print "user_form"
        print request, profile_form
        print "PROFILE:",  profile_form['facebook'], profile_form['location'], "Value:", profile_form['location'].value()
        print "POST: ", request.POST
        print "ERRORS: ", profile_form.errors
        if profile_form.is_valid():
            print "profile_form"
        if user_form.is_valid() and profile_form.is_valid():
            print "ACC 4"
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
#            return redirect('/')
            return render(request, 'mentor/account_settings.html', {
                'user_form': user_form,
                'profile_form': profile_form})

    return render(request, 'mentor/account_settings.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
@transaction.atomic
def account_1(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    print profile_form.as_p()

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('app_name:url'))
    else:
        messages.error(request, "Error")
    return render(request, 'mentor/account_1.html', {'profile_form': profile_form})


@login_required
@transaction.atomic
def account_2(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        print "POST"
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid():
            print "user_form"

        if profile_form.is_valid():
            print "profile_form"

        if user_form.is_valid() and profile_form.is_valid():
            print "ACC 4"
            user_form.save()
            profile_form.save()
            return render(request, 'mentor/account_2.html', {
                'user_form': user_form,
                'profile_form': profile_form})

    return render(request, 'mentor/account_2.html', {
        'user_form' : user_form,
        'profile_form': profile_form
    })


@login_required
@transaction.atomic
def prof(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        print "POST"
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid():
            print "user_form"

        if profile_form.is_valid():
            print "profile_form"

        if user_form.is_valid() and profile_form.is_valid():
            print "ACC 4"
            user_form.save()
            print 'Antes: ', profile_form
            profile_form.save()
            print 'Despues:',  profile_form

        return render(request, 'mentor/prof.html', {
                'user_form': user_form,
                'profile_form': profile_form})

    return render(request, 'mentor/prof.html', {
        'user_form' : user_form,
        'profile_form': profile_form
    })


@login_required
def datos(request, pk):
    print "Request", request
    print "pk: ", pk

    post = Datos.objects.get(id=6)
    print "Mente:", post.mentee

#    post = get_list_or_404(Datos, id=6)
    print "Post:", post

    form = DatosForm(instance=post)
    print "Form: ", form
    if request.method == 'POST':
        print "POST"

    return render(request, 'mentor/datos.html', {'form':form})


class MeetingListView(generic.ListView):
    model = Meeting

    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Meeting.objects.filter(mentor_name__icontains='daniel')[:5] # Get 5 books containing the title war
    template_name = 'meeting/meeting_listview.html'  # Specify your own template name/location


class MeetingListDetailView(generic.DetailView):
    model = Meeting


def meeting_detail_view( request, pk):
    try:
        book_id=Meeting.objects.get(pk=pk)

    except Meeting.DoesNotExist:
        raise Http404("Meeting does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(request,
                  'meeting/meeting_detailview.html',
                  context={'book':book_id}
                  )


@login_required
def mentors(request):
    mentor = User.objects.filter(profile__mentor=True)
    return render(request, 'meeting/mentors.html', {'mentor': mentor})


@login_required
def mentees(request):
    mentee = {}
    return render(request, 'meeting/mentees.html', {'mentee': mentee})


@login_required
def mentors_statistics(request):
    mentor = {}
    return render(request, 'meeting/mentors_statistics.html', {'mentor': mentor})


@login_required
def mentees_statistics(request):
    mentee = {}
    return render(request, 'meeting/mentees_statistics.html', {'mentee': mentee})


@login_required
def set_as_mentor(request):
    mode = Profile.objects.get(user=request.user.id)
    print "Mentor: ", mode.active_mode
    mode.active_mode = "Mentor"
    mode.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#    return render(request, ".")


@login_required
def set_as_mentee(request):
    mode = Profile.objects.get(user=request.user.id)
    print "Mentee: ", mode.active_mode
    mode.active_mode = "Mentee"
    mode.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#    return render(request, ".")
