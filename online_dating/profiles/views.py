from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from forms import ProfileForm, CommentForm, VoteForm
from django.contrib.auth.decorators import login_required
from profiles.models import Profile,Comment,Vote

def random_profiles(request, n=5):
	all_profiles = Profile.objects.order_by('?')[:n]
	context = {'profiles_list': all_profiles}

	return render(request, 'profiles/profiles.html', context)

def display_objects_with_filter(request, filter):
	profiles_list = Profile.objects.filter(gender=filter).order_by('name')
	return display_objects(request, profiles_list, title=filter)

def most_commented(request):
	profiles_list = sorted(
		Profile.objects.all(),
		key=lambda profile: len(profile.comment_set.all()),
		reverse=True
	)[:5]

	return display_objects(request, profiles_list, title="Most commented")

def most_rated(request):
	profiles_list = sorted(
		Profile.objects.all(),
		key=lambda form: form.average_rate(),
		reverse=True
	)[:5]
	return display_objects(request, profiles_list, title="Most rated")

def display_objects(request, profiles_list, title=""):
	context = {'profiles_list': profiles_list, 'title': title}
	return render(request, 'profiles/profiles.html', context)

@login_required
def detail(request, profile_id):
	profile = get_object_or_404(Profile, pk=profile_id)

	if request.method == 'POST' and request.POST['action'] == "create":
		comment_form = CommentForm(request.POST, )
		if comment_form.is_valid():
			obj = comment_form.save(commit=False)
			obj.user = request.user
			obj.profile = profile
			obj.save()
	else:
		comment_form = CommentForm()

	if request.method == 'POST' and request.POST['action'] == "vote":
		try:
			v = Vote.objects.get(for_whom=profile.owner, from_whom=request.user)
			vote_form = VoteForm(request.POST, instance=v)
		except Vote.DoesNotExist:
			vote_form = VoteForm(request.POST)
		if vote_form.is_valid():
			obj = vote_form.save(commit=False)
			obj.from_whom = request.user
			obj.for_whom = profile
			obj.save()
	else:
		vote_form = VoteForm()

	context = {
		'profile': profile,
		'comment_form': comment_form,
		'vote_form': vote_form,
	}

	return render(request, 'profiles/detail.html', context)

@login_required
def create_profile(request):
	try:
		profile = Profile.objects.get(owner=request.user)
	except Profile.DoesNotExist:
		profile = None

	if request.method == "POST":
		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.owner = request.user
			obj.save()
			return HttpResponseRedirect("/profiles/" + str(obj.pk))
	else:
		form = ProfileForm(instance=profile)

	return render(request, 'profiles/create_profile.html', {'form':form})
