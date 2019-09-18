from django.shortcuts import render

# Create your views here.
def info(request):
	header_str='Customer Information'
	h3_str='Customer Information'
	h4_str='ษริษัท แมวเหมียว จำกัด'
	web_name='Mawmeow'
	nevbar1='Table'
	nevbar2='Add'
	context={
		'var1': header_str,
		'var2': h3_str,
		'var3': h4_str,
		'webname': web_name,
		'table': nevbar1,
		'info': nevbar2
	}
	return render(request, 'information.html', context)

def login(request):
	header_str='login'
	nevbar='mawmew'
	context={
		'var1': header_str,
		'var2': nevbar
	}
	return render(request, 'login.html', context)

def table_sample(request ):
	header_str='Information Table'
	web_name='Mawmeow'
	nevbar1='Table'
	nevbar2='Add'
	context={
		'var1': header_str,
		'webname': web_name,
		'table': nevbar1,
		'info': nevbar2,
		'entry1': 'First name',
		'entry2': 'Last name',
		'entry3': 'Phone',
		'entry4': 'E-mail',
		'entry5': 'Address',
		'entry6': 'pic',
	}
	return render(request, 'table_sample.html', context)

	