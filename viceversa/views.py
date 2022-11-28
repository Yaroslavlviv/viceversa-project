from django.shortcuts import render
import string

def home(request):
	return render(request, 'home.html')
def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	result_word = str(len(user_text.split()))
	return render(request, 'reverse.html', {'usertext':user_text,
		'reversedtext':reversed_text,'resultword':result_word})
