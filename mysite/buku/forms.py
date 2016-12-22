from django import forms

class BukuSearchForm(forms.Form):
    query = forms.CharField(label=_('Filter'), required=False)

    def filter_queryset(self, request, queryset):
        if self.cleaned_data['name']:
            return queryset.filter(name__icontains=self.cleaned_data['query'])
        return queryset

