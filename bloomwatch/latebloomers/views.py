from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .detectSuperbloom import isSuperBloom
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request, "home.html")

def superbloom2022(request):
    return render(request, "superbloom2022.html")
def superbloom2023(request):
    return render(request, "superbloom2023.html")

# views.py
@csrf_exempt
def process_slider(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        slider_value = data.get("value")

        # Build filename and check validity
        dates={
            1: "2023",
            2: "2023",
            3: "2023",
            4: "2023",
            5: "2023"
        }
        filename1=f"latebloomers/static/latebloomers/{dates[int(slider_value)]}-yellow.jpeg"
        filename2=f"latebloomers/static/latebloomers/{dates[int(slider_value)]}-nvdi.jpeg"
        is_valid = isSuperBloom(filename1, filename2)
        print(is_valid)
        return JsonResponse({"is_valid": is_valid})
