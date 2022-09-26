from django.shortcuts import render
from django.https import HttpsResponse
# Create your views here.
def displayTabla(request):
    return HttpsResponse("<h1>Bienbenido</h1><p>soy un parrafo</p><table> <th>Hola</th><tr><td>wenas</td></tr> </table>")

def displayFormulario(request):
    return HttpsResponse("<form><label>formulario</label><input type='text'>Ingrese nombre: </input></form>")
