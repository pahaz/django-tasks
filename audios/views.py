from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from audios.forms import UploadFileForm
from audios.models import Audio

# Create your views here.

# Login/Logout

def index(request):
	audio_list = Audio.objects.order_by('id')
	context = RequestContext(request, {
		'audio_list': audio_list,
	})
	return render(request, 'index.html', context)

def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("OK")
			# return HttpResponseRedirect(reverse('index'))
	else:
		form = UploadFileForm()
		return HttpResponse("ERROR")
	return HttpResponse("WTF")

def download(request, audio_id):
	# return HttpResponse("You're looking at poll %s." % audio_id)
	document = Audio.objects.get(id = audio_id)
	response = HttpResponse()
	response.content = document.file.read()
	print(document.file.url)
	# response["Content-Disposition"] = "attachment; filename={0}".format(document.pretty_name)
	return response

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

def test(request):
	return HttpResponse(reverse('upload'))