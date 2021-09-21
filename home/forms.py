from home.models import Domain, Suffix, Category
from django import forms


class DomainSearchForm(forms.Form):
    english_name = forms.CharField(max_length=100, label="جستجوی نام انگلیسی دامنه", required=False)
    persian_name = forms.CharField(max_length=100, label="جستجوی نام فارسی دامنه", required=False)
    content = forms.BooleanField(label="شامل محتوا و سایت", required=False)
    agreement_price = forms.BooleanField(label="قیمت توافقی", required=False)
    top_domains = forms.BooleanField(label="برترین دامنه ها", required=False)
    category_name = forms.ModelChoiceField(label="دسته بندی دامنه", queryset=Category.objects.all(), required=False)
    suffix_name = forms.ModelChoiceField(label="پسوند دامنه", queryset=Suffix.objects.all(), required=False)


