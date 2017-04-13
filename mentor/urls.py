from django.conf.urls import url
from .views import home, login_user, logout_user, update_profile, account_settings, account_1, account_2
from .views import prof, fancy, crispy, datos, dashboard, meeting, calendar,\
     account_activation_sent, activate, signup_user, \
     MeetingListView, MeetingListDetailView, meeting_detail_view, mentors, mentees


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^home/$', home, name='home'),
    url(r'^meeting/$', meeting, name='meeting'),
    url(r'^list_meeting/$', MeetingListView.as_view(), name='list_meeting'),
    url(r'^list_meeting_detail/(?P<pk>\d+)$', meeting_detail_view, name='list_meeting_detail'),

    url(r'^mentors/$', mentors, name='mentors'),
    url(r'^mentees/$', mentees, name='mentees'),


    url(r'^calendar/$', calendar, name='calendar'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^login/$', login_user, name='login_user'),
    url(r'^logout/$', logout_user, name='logout_user'),
    url(r'^update_profile/$', update_profile, name='update_profile'),
    url(r'^account_settings/$', account_settings, name='account_settings'),
    url(r'^account_1/$', account_1, name='account_1'),
    url(r'^account_2/$', account_2, name='account_2'),
    url(r'^prof/$', prof, name='prof'),
    url(r'^fancy/$', fancy, name='fancy'),
    url(r'^crispy/$', crispy, name='crispy'),
    url(r'^datos/(?P<pk>\d+)$', datos, name='datos'),
    url(r'^signup/$', signup_user, name='signup_user'),

    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]
