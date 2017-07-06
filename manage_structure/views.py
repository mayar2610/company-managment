from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader, Context, RequestContext
from .models import Company
from .forms import CompanyForm

def company_new(request):
	if request.method == "POST":
		form = CompanyForm(request.POST)
		if form.is_valid():
			company = form.save()
			company.save()
			return redirect('company_list')
	else:
		form = CompanyForm()
	return render(request, 'company_edit.html', {'form': form})


def company_edit(request, pk):
	company = get_object_or_404(Company, pk=pk)
	if request.method == "POST":
		form = CompanyForm(request.POST, instance=company)
		if form.is_valid():
			company = form.save()
			company.save()
			return redirect('company_list')
	else:
		form = CompanyForm(instance=company)
	return render(request, 'company_edit.html', {'form': form})


def company_detail(request, pk):
	company = get_object_or_404(Company, pk=pk)
	return render(request, 'company_detail.html', {'company': company})

def company_remove(request, pk):
	company = get_object_or_404(Company, pk=pk)
	company.delete()
	return redirect('company_list')

def company_list(request):
	nodes = list(Company.objects.all())

	for node in nodes:
		total = 0
		if node.get_ancestors() is True:
			children = node.get_ancestors()
			for child in children:
				total += child.earnings
			total += node.earnings
		else:
			total = None
		
	return render(request, 'company_list.html', {'nodes': nodes})
	

