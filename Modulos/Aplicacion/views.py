from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# ------------------Estudiantes-----------------------

def login(request):
    logout(request)
    return redirect("/")

@login_required
def homeEstudiantes(request):
    estudiantes = estudiante.objects.all()
    return render(request, "estudiantes.html", {"estudiantes": estudiantes})

def registrarEstudiante(request):
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    semestre = request.POST['txtSemestre']
    carrera = request.POST['txtCarrera']
    escuela = request.POST['txtEscuela']

    Estudiante = estudiante.objects.create(cedula = cedula, nombre = nombre, apellido = apellido, semestre = semestre, carrera = carrera, escuela = escuela)

    return redirect('/')

def eliminarEstudiante(request, cedula):
    Estudiante = estudiante.objects.get(cedula=cedula)
    Estudiante.delete()

    return redirect('/') 

def edicionEstudiante(request, cedula):
    Estudiante = estudiante.objects.get(cedula=cedula)

    return render(request, "edicionEstudiantes.html", {"Estudiante": Estudiante})

def editarEstudiante(request):
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    semestre = request.POST['txtSemestre']
    carrera = request.POST['txtCarrera']
    escuela = request.POST['txtEscuela']

    Estudiante = estudiante.objects.get(cedula=cedula)
    Estudiante.nombre = nombre
    Estudiante.apellido = apellido
    Estudiante.semestre = semestre
    Estudiante.carrera = carrera
    Estudiante.escuela= escuela
    Estudiante.save()

    return redirect('/') 

# ------------------Académicos-----------------------

def homeAcademicos(request):
    academicos = academico.objects.all()
    return render(request, "academicos.html", {"academicos": academicos})


def registrarAcademico(request):
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    escuela = request.POST['txtEscuela']

    Academico = academico.objects.create(cedula = cedula, nombre = nombre, apellido = apellido, escuela = escuela)

    return redirect('/ac')

def eliminarAcademico(request, cedula):
    Academico = academico.objects.get(cedula=cedula)
    Academico.delete()

    return redirect('/ac')

def edicionAcademico(request, cedula):
    Academico = academico.objects.get(cedula=cedula)

    return render(request, "edicionAcademico.html", {"Academico": Academico})

def editarAcademico(request):
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    escuela = request.POST['txtEscuela']

    Academico = academico.objects.get(cedula=cedula)
    Academico.nombre = nombre
    Academico.apellido = apellido
    Academico.escuela= escuela
    Academico.save()

    return redirect("/ac")

# ------------------Administrativos-----------------------

def homeAdministrativos(request):
    administrativos = administrativo.objects.all()
    return render(request, "administrativos.html", {"administrativos": administrativos})


def registrarAdministrativo(request):
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']

    Administrativo = administrativo.objects.create(cedula = cedula, nombre = nombre, apellido = apellido)

    return redirect('/ad')

def eliminarAdministrativo(request, cedula):
    Administrativo = administrativo.objects.get(cedula=cedula)
    Administrativo.delete()

    return redirect('/ad')

def edicionAdministrativo(request, cedula):
    Administrativo = administrativo.objects.get(cedula=cedula)

    return render(request, "edicionAdministrativo.html", {"Administrativo": Administrativo})

def editarAdministrativo(request):
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']

    Administrativo = administrativo.objects.get(cedula=cedula)
    Administrativo.nombre = nombre
    Administrativo.apellido = apellido
    Administrativo.save()

    return redirect("/ad")  

# --------------------Libros-----------------------

def homeLibros(request):
    libros = libro.objects.all()
    return render(request, "libros.html", {"libros": libros})


def registrarLibro(request):
    titulo = request.POST['txtTitulo']
    autor = request.POST['txtAutor']
    cota = request.POST['txtCota']
    editorial = request.POST['txtEditorial']
    edicion = request.POST['txtEdicion']
    año = request.POST['txtAño']
    cantidad = request.POST['txtCantidad']
    cantidadPres = prestamo.objects.filter(titulo=titulo).count()

    Libro = libro.objects.create(titulo = titulo, autor = autor, cota = cota, editorial = editorial, edicion = edicion, año = año, cantidad = cantidad, cantidadPres = cantidadPres)

    return redirect('/li')

def eliminarLibro(request, titulo):
    Libro = libro.objects.get(titulo=titulo)
    Libro.delete()

    return redirect('/li')

def edicionLibro(request, titulo):
    Libro = libro.objects.get(titulo=titulo)

    return render(request, "edicionLibros.html", {"Libro": Libro})

def editarLibro(request):
    titulo = request.POST['txtTitulo']
    autor = request.POST['txtAutor']
    cota = request.POST['txtCota']
    editorial = request.POST['txtEditorial']
    edicion = request.POST['txtEdicion']
    año = request.POST['txtAño']
    cantidad = request.POST['txtCantidad']
    cantidadPres = prestamo.objects.filter(titulo=titulo).count()

    Libro = libro.objects.get(titulo=titulo)
    Libro.autor = autor
    Libro.cota = cota
    Libro.editorial = editorial
    Libro.edicion = edicion
    Libro.año = año
    Libro.cantidad = cantidad
    Libro.cantidadPres = cantidadPres
    Libro.save()

    return redirect("/li")  

# --------------------Prestamos-----------------------

def homePrestamos(request):
    prestamos = prestamo.objects.all()
    libros = libro.objects.all()
    academicos = academico.objects.all()
    administrativos = administrativo.objects.all()
    estudiantes = estudiante.objects.all()
    context = {"prestamos": prestamos, "libros": libros, "academicos": academicos, "administrativos": administrativos, "estudiantes": estudiantes}
    return render(request, "prestamos.html", context)

def registrarPrestamo(request):
    if prestamo.objects.exists():
        codigo = prestamo.objects.latest('codigo').codigo + 1
    else:
        codigo = 1
    
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    escuela = request.POST['txtEscuela']
    titulo = request.POST['txtTitulo']
    autor = request.POST['txtAutor']
    semestre = request.POST['txtSemestre']
    tipoPrestamo = request.POST["txtTipoPrestamo"]
    tipoUsuario = request.POST["txtTipoUsuario"]
    fechaInicial = request.POST["txtFechaIni"]
    fechaFinal = request.POST["txtFechaFin"]
    bibliotecaria = request.POST["txtBiblio"]
    observaciones = request.POST["txtObservaciones"]

    Prestamo = prestamo.objects.create(codigo = codigo, tipoUsuario = tipoUsuario, tipoPrestamo = tipoPrestamo, titulo = titulo, autor = autor, cedula = cedula, nombre = nombre, apellido = apellido, semestre = semestre, escuela = escuela, fechaInicial = fechaInicial, fechaFinal = fechaFinal, bibliotecaria = bibliotecaria, observaciones = observaciones)

    libro.objects.filter(titulo=titulo).update(cantidadPres=F('cantidadPres'))

    return redirect('/pre')

def eliminarPrestamo(request, codigo):
    Prestamo = prestamo.objects.get(codigo=codigo)
    titulo = Prestamo.titulo
    Prestamo.delete()

    libro.objects.filter(titulo=titulo).update(cantidadPres=F('cantidadPres') - 1)

    return redirect('/pre')

def edicionPrestamo(request, codigo):
    Prestamo = prestamo.objects.get(codigo=codigo)
    libros = libro.objects.all()
    academicos = academico.objects.all()
    administrativos = administrativo.objects.all()
    estudiantes = estudiante.objects.all()
    context = {"Prestamo": Prestamo, "libros": libros, "academicos": academicos, "administrativos": administrativos, "estudiantes": estudiantes}

    return render(request, "edicionPrestamo.html", context)

def editarPrestamo(request):
    codigo = request.POST['txtCodigo']
    cedula = request.POST['txtCedula']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    escuela = request.POST['txtEscuela']
    titulo = request.POST['txtTitulo']
    autor = request.POST['txtAutor']
    semestre = request.POST['txtSemestre']
    tipoPrestamo = request.POST["txtTipoPrestamo"]
    tipoUsuario = request.POST["txtTipoUsuario"]
    fechaInicial = request.POST["txtFechaIni"]
    fechaFinal = request.POST["txtFechaFin"]
    bibliotecaria = request.POST["txtBiblio"]
    observaciones = request.POST["txtObservaciones"]

    Prestamo = prestamo.objects.get(codigo=codigo)
    Prestamo.autor = autor
    Prestamo.cedula = cedula
    Prestamo.nombre = nombre
    Prestamo.apellido = apellido
    Prestamo.escuela = escuela
    Prestamo.titulo = titulo
    Prestamo.semestre = semestre
    Prestamo.tipoPrestamo = tipoPrestamo
    Prestamo.tipoUsuario = tipoUsuario
    Prestamo.fechaInicial = fechaInicial
    Prestamo.fechaFinal = fechaFinal
    Prestamo.bibliotecaria = bibliotecaria
    Prestamo.observaciones =observaciones
    Prestamo.save()

    libro.objects.filter(titulo=titulo).update(cantidadPres=F('cantidadPres'))

    return redirect("/pre")  