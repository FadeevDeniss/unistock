from django.shortcuts import render
from django.views.generic.base import View

from apps.core.forms import UserPhoneForm


class HomePageView(View):

    form_class = UserPhoneForm
    template_name = "home.html"

    def get(self, request, *args, **kwargs):

        f = self.form_class()

        return render(
            request,
            self.template_name,
            {'form': f}
        )


