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
def process_slider2023(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        slider_value = data.get("value")

        # Build filename and check validity
        dates={
            1: "23-2-2.jpeg",
            2: "23-4-7.jpeg",
            3: "23-6-2.jpeg",
        }
        filename1=f"latebloomers/static/latebloomers/yellow"+dates[int(slider_value)]
        filename2=f"latebloomers/static/latebloomers/nvdi"+dates[int(slider_value)]
        is_valid = isSuperBloom(filename1, filename2)
        print(is_valid)
        return JsonResponse({"is_valid": is_valid})

@csrf_exempt
def process_slider2022(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        slider_value = data.get("value")

        # change files
        dates={
            1: "23-2-2.jpeg",
            2: "23-4-7.jpeg",
            3: "23-6-2.jpeg",
        }
        filename1=f"latebloomers/static/latebloomers/yellow"+dates[int(slider_value)]
        filename2=f"latebloomers/static/latebloomers/nvdi"+dates[int(slider_value)]
        is_valid = isSuperBloom(filename1, filename2)
        print(is_valid)
        return JsonResponse({"is_valid": is_valid})
