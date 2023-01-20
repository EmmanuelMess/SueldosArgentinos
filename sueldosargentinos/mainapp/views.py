from django.http import HttpResponse
from django.template import Context, Engine, Template

from mainapp.models import Wage


def index(request):
    """View function for home page of site."""

    index_content_template: Template = Engine.get_default().get_template("mainapp/index.html")

    aa: int = 758244
    position: str = "EXPERTO EN INGENIERÍIA SATELITAL Y PLATAFORMA - NIVEL B"

    temp = Wage.objects.create(position=position, monthly=aa)

    context: Context = Context({
        "title": "Salarios Argentinos",
        "content": index_content_template.render(Context()),
        "wage_list": [temp, temp, temp, temp]
    })

    return HttpResponse(index_content_template.render(context))
