from django.shortcuts import render
from django.views.generic import TemplateView
from googlelogin.settings import YOUR_GOOGLE_CLIENT_ID


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['YOUR_GOOGLE_CLIENT_ID'] = YOUR_GOOGLE_CLIENT_ID
        return context
