
from django.views.generic import TemplateView
# Create your views here.

class LandingView(TemplateView): 
	template_name = 'base/index.html'