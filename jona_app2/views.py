from django.shortcuts import render
from django.http import HttpsResponse
# Create your views here.
def displayList(request):
    return(HttpsResponse("<header>Holaaaa!</header><ul><li>soy una lista</li></ul><div><a href='https://www.youtube.com/watch?v=BuOADNq99Ms'></a></div>"))

def displayBotones(request):
    return(HttpsResponse("<form><label>formulario</label><input type='text'>Ingrese nombre: </input><input type='text'>Ingrese correo: </input><button>Enviar</button></form>"))