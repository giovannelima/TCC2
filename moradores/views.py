#from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from moradores.models import moradores
from .forms import moradorForm
#from django.utils import timezone

@login_required()
def residents_list(request):
    cliente = moradores.objects.filter(userid=request.user.id)
    return render(request, 'moradores/morador.html', {'cliente': cliente})

@login_required()
def residents_new(request):
    form = moradorForm(request.POST or None)
    if form.is_valid():
        teste = form.save(commit=False)
        teste.userid = request.user.id
        teste.save()
        return redirect('lista_moradores')
    return render(request, 'moradores/morador_form.html', {'form': form})

@login_required()
def residents_update(request, id):
    # cliente = get_object_or_404(moradores, pk=id)
    # print('batata', cliente)
    # form = moradorForm(request.POST or None, instance=cliente)
    # system_messages = messages.get_messages(request)
    # for message in system_messages:
    #     # This iteration is necessary
    #     pass
    # print(form)
    # if form.is_valid():
    #     form.save()
    cliente = get_object_or_404(moradores, pk=id)
    form = moradorForm(request.POST or None, instance=cliente)
    #print(form)
    if form.is_valid():
        form.save()
        return redirect('lista_moradores')
    return render(request, 'moradores/morador_form.html', {'form':form, 'cliente':cliente})

@login_required()
def residents_delete(request, id):
    morador = get_object_or_404(moradores, pk=id)
    #storage = messages.get_messages(request)
   # storage.used = True

    if request.method == 'POST':
        try:
            morador.delete()
            return redirect('lista_moradores')
        except Exception as e:
            messages.error(request, f"Não foi possível excluir o morador {morador}, pois ele faz parte de um contrato!")
           # messages.
            return redirect('lista_moradores')
    # else:
    #   messages.error(request, 'Não é possivel deletar morador, está vinculado a um contrato.!')
    return render(request, 'moradores/morador_delete_confirm.html', {'morador':morador})

@login_required()
def voltarMorador(request):
    return redirect('lista_moradores')

