from django.views.generic.edit import FormMixin
from django.views.generic import ListView,DetailView,TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count 
from itertools import chain
from .models import TBuku,TKota,TPenerbit
from django import forms

class BukuSearchForm(forms.Form): #pendefisian pada form pencarian
    query = forms.CharField(label=('Cari'),required=False)

    def filter_queryset(self, request, queryset):
        #if self.cleaned_data['judul_buku']:
        return queryset.filter(judul_buku__icontains=self.cleaned_data['query'])
        #return queryset

class FilteredListView(FormMixin, ListView): #fitur pencarian
	def get_form_kwargs(self):
		return {
			'initial': self.get_initial(),
			'prefix': self.get_prefix(),
			'data': self.request.GET or None
		}	
		
	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset()
		form = self.get_form(self.get_form_class())
		if form.is_valid():
			self.object_list = form.filter_queryset(request, self.object_list)
		context = self.get_context_data(form=form, object_list=self.object_list)
		return self.render_to_response(context)	
	      
	
buku_list = FilteredListView.as_view( #view tampilan data tabel buku
	form_class=BukuSearchForm,
    queryset=TBuku.objects.all(), 
    template_name='list.html',
	#ajax_template_name='list_hasil.html',
    paginate_by=15,
)

buku_detail = DetailView.as_view( #view tampilan detil informasi tiap buku
    queryset=TBuku.objects.select_related(),
    template_name='detail.html',
	#template_name='det_tb.html',
)

map_vi = ListView.as_view(# view tampilan peta lokasi penerbit buku
	#queryset = TPenerbit.objects.all().values('kota_penerbit').annotate(jum=Count('kota_penerbit')),
	queryset = TPenerbit.objects.all().values('kota_penerbit').annotate(jum=Count('kota_penerbit')).filter(tbuku__id_penerbit__isnull=False),	
	template_name='mv.html',
)


buku_detail_penerbit = DetailView.as_view(
    queryset=TPenerbit.objects.all(),
    template_name='detail.html',	
)