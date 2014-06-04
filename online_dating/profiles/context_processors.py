from profiles.models import Profile


def random_profiles(request):
	return {
		'random_profiles_list': Profile.random_profiles.all()
	}