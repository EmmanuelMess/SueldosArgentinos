from django.http import HttpResponse
from django.template import Context, Engine, Template


def index(request):
    """View function for home page of site."""

    base_template: Template = Engine.get_default().get_template("mainapp/base.html")
    index_content_template: Template = Engine.get_default().get_template("mainapp/index.html")
    wage_list_template: Template = Engine.get_default().get_template("mainapp/by-wage-item.html")

    aa: int = 758244
    monthly: str = f"{aa}"
    yearly: str = f"{aa * 13}"
    position: str = "EXPERTO EN INGENIERÍIA SATELITAL Y PLATAFORMA - NIVEL B"

    wage_list_element_context: Context = Context({
        "monthly": monthly,
        "yearly": yearly,
        "position": position,
    })

    context: Context = Context({
        "title": "Salarios Argentinos",
        "content": index_content_template.render(Context()),
        "wage_list": wage_list_template.render(wage_list_element_context)
    })

    return HttpResponse(base_template.render(context))
