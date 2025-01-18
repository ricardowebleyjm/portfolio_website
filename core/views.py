from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import csv

def home(request):
    return render(request, "core/index.html")

class SaveEmailView(View):
    def post(self, request, *args, **kwargs):
        try:
            email = request.POST.get('email', None)
            with open('emails.csv', 'a', newline='') as csvfile:
                fieldnames = ['Email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'Email': email})

            return JsonResponse({'success': True, 'message': 'Email saved successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'An error occurred: ' + str(e)})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)


class HireMe(View):
    def post(self, request, *args, **kwargs):
        try:
            email = request.POST.get('email', None)
            with open('clients.csv', 'a', newline='') as csvfile:
                fieldnames = ['Email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'Email': email})

            return JsonResponse({'success': True, 'message': 'Thank you for reaching out! I will get back to you soon.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'An error occurred: '})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)