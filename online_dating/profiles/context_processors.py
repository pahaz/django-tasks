from profiles.models import Profile


def random_profiles(request, n=5):
	profiles = Profile.objects.order_by('?')[:n]
	return {
		'random_profiles_list': profiles
	}