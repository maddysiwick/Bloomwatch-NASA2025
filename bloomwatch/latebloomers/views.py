from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .detectSuperbloom import isSuperBloom
from django.views.decorators.csrf import csrf_exempt
from .calculations.allcode.putting_it_together import (
    prec_june_sept_22_avg, prec_oct_feb_22_avg,
    prec_june_sept_23_avg, prec_oct_feb_23_avg,
    temp_oct_feb_22_avg, temp_oct_feb_23_avg, temp_variation_22, temp_variation_23,
)


# Create your views here.
def home(request):
    context = {
        "prec_june_sept_22_avg": prec_june_sept_22_avg,
        "prec_oct_feb_22_avg": prec_oct_feb_22_avg,
        "prec_june_sept_23_avg": prec_june_sept_23_avg,
        "prec_oct_feb_23_avg": prec_oct_feb_23_avg,
        "temp_oct_feb_22_avg": temp_oct_feb_22_avg,
        "temp_oct_feb_23_avg": temp_oct_feb_23_avg,
        "temp_variation_22": temp_variation_22,
        "temp_variation_23": temp_variation_23,
    }
    return render(request, "home.html", context)

def superbloom2022(request):
    context = {
        "prec_june_sept_22_avg": prec_june_sept_22_avg,
        "prec_oct_feb_22_avg": prec_oct_feb_22_avg,
        "temp_oct_feb_22_avg": temp_oct_feb_22_avg,
        "temp_varoiation_22": temp_variation_22,
    }
    return render(request, "superbloom2022.html", context)

def superbloom2023(request):
    context = {
        "prec_june_sept_23_avg": prec_june_sept_23_avg,
        "prec_oct_feb_23_avg": prec_oct_feb_23_avg,
        "temp_oct_feb_23_avg": temp_oct_feb_23_avg,
        "temp_variation_23": temp_variation_23,
    }
    return render(request, "superbloom2023.html", context)


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

