from django.shortcuts import render
from django.http import JsonResponse
import csv

def home(request):
    return render(request, "core/index.html")

def save_email(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email') 

            # Create or open the CSV file in append mode
            with open('emails.csv', 'a', newline='') as csvfile:
                fieldnames = ['Email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'Email': email})

            return JsonResponse({'success': True, 'message': 'Email saved successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'An error occurred: ' + str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'method not allowed'})