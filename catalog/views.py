from django.shortcuts import render
from .models import Cliente, CotizaInstance
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .forms import RenewCotizaAhora

def index(request):
    
    """
    Función vista para la página inicio del sitio.
    """
    num_instances=CotizaInstance.objects.all().count()
    num_instances_available=CotizaInstance.objects.filter(status__exact='d').count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_instances':num_instances,'num_instances_available':num_instances_available},
    )


@permission_required('catalog.can_mark_returned')
def cotiza_ahora(request, pk):
    
    cotiza_inst=get_object_or_404(CotizaInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewCotizaAhora(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            cotiza_inst.due_back = form.cleaned_data['renewal_date']
            cotiza_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewCotizaAhora(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/cotiza_ahora.html', {'form': form, 'cotizainst':cotiza_inst})



class CotizaInstanceCreate(CreateView):
    model = CotizaInstance
    fields = '__all__'
    initial={'due_back':'24/06/2022',}

class CotizaInstanceUpdate(UpdateView):
    model = CotizaInstance
    fields = ['id','nombre','due_back']

class CotizaInstanceDelete(DeleteView):
    model = CotizaInstance
    success_url = reverse_lazy('cotizas')