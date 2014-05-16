from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from mainapp.models import Document, UserProfile
from mainapp.forms import DocumentForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'mainapp/index.html', {})


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    purchased_documents = user_profile.purchased_documents.all()
    return render(request, 'mainapp/profile.html', {'user_profile': user_profile, 'purchased_documents': purchased_documents})

@login_required
def get_credits(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.credits += 100
    user_profile.save()
    return HttpResponseRedirect(reverse('mainapp.views.index'))


@login_required
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'], uploaded_by=request.user, price=request.POST['price'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('mainapp.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    user_profile = UserProfile.objects.get(user=request.user)
    credits_amount = user_profile.credits
    purchased_documents = user_profile.purchased_documents.all()

    return render_to_response(
        'mainapp/list.html',
        {'documents': documents, 'form': form, 'credits_amount': credits_amount, 'purchased_documents': purchased_documents},
        context_instance=RequestContext(request)
    )

@login_required
def download(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    user_profile = UserProfile.objects.get(user=request.user)
    if document not in user_profile.purchased_documents.all():
        user_profile.purchased_documents.add(document)
        user_profile.credits -= document.price
        user_profile.save()
    return redirect(document.docfile.url)


def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response(
        'mainapp/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context
    )


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Your account is disabled')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse('Invalid login and/or password')
    else:
        return render_to_response('mainapp/login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')