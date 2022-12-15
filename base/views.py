from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Match"
        return context

