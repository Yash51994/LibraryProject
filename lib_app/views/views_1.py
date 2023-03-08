from django.shortcuts import render, redirect
from lib_app.models import Book
from ..forms import BookForm, Bform
from django.http import HttpResponse

def form_view(request):
    if request.method=='POST':
        form = Bform(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': Bform()}
    return render(request, 'form.html', context)

def update_view(request, pk):
    book = Book.objects.get(id=pk)
    if request.method=='POST':
        book.name = request.POST.get('name')
        book.price = request.POST.get('price')
        book.qty = request.POST.get('qty')
        book.is_published = request.POST.get('is_published')
        book.save()
    form = Bform(instance=book)
    context = {'form': form}
    return render(request, 'form.html', context)


from django.views import View

class Home(View):
    def get(self, request):
        return HttpResponse("get method")

# -------------------------------------------------------------

# print(dir(generic))

# 'CreateView', 'DateDetailView', 'DayArchiveView', 'DeleteView', 'DetailView', 'FormView', 'GenericViewError', 'ListView',
# 'MonthArchiveView', 'RedirectView', 'TemplateView', 'TodayArchiveView', 'UpdateView'


from django.views.generic import TemplateView, RedirectView

class about_us(TemplateView):
    template_name = 'temp.html'


class  TestRedirect(RedirectView):
    url = "https://www.facebook.com/"
    


