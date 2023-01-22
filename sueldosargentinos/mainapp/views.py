from django.http import HttpResponse
from django.template import Context, Engine, Template

import django_filters

from mainapp.models import Wage


class ProductFilter(django_filters.FilterSet):
    position = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Wage
        fields = ['monthly']

    @property
    def qs(self):
        parent = super().qs
        parent = parent[:5]

        return parent


def index(request):
    """View function for home page of site."""

    index_content_template: Template = Engine.get_default().get_template("mainapp/index.html")

    aa: int = 758244
    position: str = "EXPERTO EN INGENIERÍIA SATELITAL Y PLATAFORMA - NIVEL B"

    if not Wage.objects.all():
        _ = Wage.objects.create(position=position, monthly=aa)
        _ = Wage.objects.create(position=position, monthly=aa)
        _ = Wage.objects.create(position=position, monthly=aa)
        _ = Wage.objects.create(position=position, monthly=aa)

    filter = ProductFilter(request.GET, queryset=Wage.objects.all())
    show_dropdown = len(filter.qs) != 0

    context: Context = Context({
        "title": "Salarios Argentinos",
        "content": index_content_template.render(Context()),
        "wage_list": Wage.objects.all()[:5],
        "show_dropdown": show_dropdown,
        "filter": filter,
    })

    return HttpResponse(index_content_template.render(context))
