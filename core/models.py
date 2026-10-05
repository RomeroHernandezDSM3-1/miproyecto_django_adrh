# render: ya estaba desde la Semana 3; junta una plantilla con datos y devuelve la página
from django.shortcuts import render
# Servicio: NUEVO — el modelo del paso 02, importado desde este mismo directorio (el punto = "esta app")
from .models import Servicio

# servicios: la vista que responde en /servicios/
def servicios(request):
    # .objects.all(): pide TODOS los servicios a MySQL (Django lo traduce a SELECT * FROM core_servicio)
    lista_servicios = Servicio.objects.all()
    # entrega la lista a la plantilla con el nombre "servicios", igual que en la Semana 3
    return render(request, 'core/servicios.html', {'servicios': lista_servicios})

# class Servicio: se convierte en la tabla "core_servicio" dentro de MySQL
class Servicio(models.Model):
    # propietario: relaciona este servicio con el usuario dueño
    # on_delete=CASCADE: si se borra ese usuario, se borran también sus servicios
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    # titulo: texto corto y obligatorio, máximo 120 caracteres
    titulo = models.CharField(max_length=120)

    # descripcion: texto largo, sin límite fijo de caracteres
    descripcion = models.TextField()

    # precio: número decimal — hasta 8 dígitos en total, 2 después del punto (ej. 1500.00)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    # categoria: texto corto para clasificar el servicio (ej. "Tutorías", "Diseño")
    categoria = models.CharField(max_length=60)

    # creado_en: Django guarda automáticamente la fecha y hora cuando se crea el registro
    creado_en = models.DateTimeField(auto_now_add=True)

    # __str__: define qué texto se muestra al "imprimir" este objeto (ej. en el panel /admin)
    def __str__(self):
        # devuelve el título en vez de algo genérico como "Servicio object (1)"
        return self.titulo 