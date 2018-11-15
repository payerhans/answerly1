from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect, HttpResponseBadRequest
from django.urls.base import reverse
from django.views.generic import CreateView

from .forms import QuestionForm
from .models import Question

# Create your views here.

class AskQuestionView(LoginRequiredMixin, CreateView):
    form_class = QuestionForm
    login_url = '/admin/login/'
    template_name = 'quanda/ask.html'

    def get_initial(self):
        return {
            'user' : self.request.user.id
        }

    def form_valid(self, form):
        action = self.request.POST.get('action')
        if action == 'SAVE':
            # save and redirect as usaul
            return super().form_valid(form)
        elif action == 'PREVIEW':
            preview = Question(
                question = form.cleaned_data['question'],
                title = form.cleaned_data['title'])
            ctx = self.get_context_data(preview = preview)
            return self.render_to_response(context = ctx)
        return HttpResponseBadRequest()
