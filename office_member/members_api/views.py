from django.http import HttpResponse
from django.template import loader
from .models import Member_api

def members_api(request):
  mymembers = Member_api.objects.all().values()
  template = loader.get_template('all_members_api.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


