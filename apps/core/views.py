import json

from django.http import JsonResponse, HttpResponse
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

    def post(self, request):
        data = json.load(request)
        f = self.form_class(data)
        if f.is_valid():
            return JsonResponse(
                {"phone": 'Номер не найден. Проверьте правильность введенного номера и отправьте форму повторно'},
                status=404)
        return JsonResponse(f.errors, status=400)

