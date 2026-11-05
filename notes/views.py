from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import NoteForm
from .models import Note


def index(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()

    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes, 'form': form})


@require_POST
def delete_note(request, pk):
    get_object_or_404(Note, pk=pk).delete()
    return redirect('index')
