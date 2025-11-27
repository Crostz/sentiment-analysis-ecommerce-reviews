"""from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "base.html")"""
from django.shortcuts import render
import pickle, os

# Cargar tu modelo
ruta_modelo = os.path.join(os.path.dirname(__file__), "../../notebooks/LR_model.sav")
with open(ruta_modelo, "rb") as f:
    modelo = pickle.load(f)

def index(request):
    return render(request, "myapp/base.html")

def predecir(request):
    if request.method == "POST":
        texto = request.POST.get("texto")
        pred = modelo.predict([texto])[0]
        return render(request, "myapp/base.html", {
            "resultado": pred,
            "texto": texto   # Texto a template
        })
    return render(request, "myapp/base.html")
