from django.shortcuts import render
from home.models import Suffix, Domain, Category
from home.forms import DomainSearchForm


def home(request):
    domains = Domain.objects.all()
    search_form = DomainSearchForm(request.GET)
    if search_form.is_valid():
        if search_form.cleaned_data["english_name"]:
            domains = domains.filter(english_name__contains=search_form.cleaned_data["english_name"])
        if search_form.cleaned_data["persian_name"]:
            domains = domains.filter(persian_name__contains=search_form.cleaned_data["persian_name"])
        if search_form.cleaned_data["category_name"] is not None:
            domains = domains.filter(category__name=search_form.cleaned_data["category_name"])
        if search_form.cleaned_data["suffix_name"] is not None:
            domains = domains.filter(suffix_name=search_form.cleaned_data["suffix_name"])
        # domains = Domain.objects.filter(english_name__contains=search_form.cleaned_data["english_name"])
        # domains = Domain.objects.filter(persian_name__contains=search_form.cleaned_data["persian_name"])
        if search_form.cleaned_data["content"]:
            domains = domains.filter(content=True)
        if search_form.cleaned_data["top_domains"]:
            domains = domains.filter(top_domains=True)
        if search_form.cleaned_data["agreement_price"]:
            domains = domains.filter(agreement_price=True)

    context = {
        "domains": domains,
        "search_form": search_form,
    }
    return render(request, "home/home.html", context)



