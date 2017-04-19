from .models import Datos, Profile, Meeting


result = Profile.objects.filter(mentor = True) | Profile.objects.filter(mentee = True)


