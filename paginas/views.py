from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/index.html'

class AdminView(TemplateView):
    template_name = 'paginas/admin.html'
