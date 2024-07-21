from django.shortcuts import render, redirect
from django.core.management import call_command
from django.contrib import messages

# Create your views here.
def home (request):
	return render(request, 'home.html')


def import_students(request):
	if request.method == 'POST':
		try:
			call_command('importstudent')
			messages.success(request, 'Student data imported successfully')
		except Exception as e:
			messages.error(request, f'Error: {e}')
		return redirect('home')
	else:
		return redirect('home')