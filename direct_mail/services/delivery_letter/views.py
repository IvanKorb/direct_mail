

# Create your views here.
from django.views.generic import TemplateView, FormView

from .models import DeliveryType
from .forms import LetterForm



class TypeListView(TemplateView):
    template_name = "delivery_letter/type_list.html"

    def get_context_data(self, **kwargs):
        kwargs['delivery_type_list'] = DeliveryType.objects.all()
        return super().get_context_data(**kwargs)

class LetterFormView(FormView):
    template_name = 'delivery_letter/delivery.html'
    form_class = LetterForm


