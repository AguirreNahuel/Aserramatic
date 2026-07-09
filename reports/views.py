from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from users.models import Empleado
from inventory.models import MateriaPrima, Producto
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, landscape


# Create your views here.

def reports_index(request):
    return render(request, 'reports/reports_index.html')


def reporte_empleados(request):
    empleados = Empleado.objects.all()

    return render(
        request,
        'reports/reporte_empleados.html',
        {'empleados': empleados}
    )


def reporte_empleados_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte_empleados.pdf"'

    pdf = SimpleDocTemplate(response)
    empleados = Empleado.objects.all()
    styles = getSampleStyleSheet()

    generado_por = request.user.get_display_name2()

    elementos = []

    elementos.append(
        Paragraph(
            "ASERRAMATIC",
            styles['Title']
        )
    )

    elementos.append(
        Paragraph(
            "Reporte de Empleados",
            styles['Heading2']
        )
    )

    elementos.append(
        Paragraph(
            f"Fecha de emisión: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            styles['Normal']
        )
    )

    elementos.append(
        Paragraph(
            f"Reporte generado por: {generado_por}",
            styles['Normal']
        )
    )

    elementos.append(Spacer(1, 20))

    datos = [['Nombre', 'Apellido', 'DNI/CUIL']]

    for empleado in empleados:
        datos.append([
            empleado.nombre,
            empleado.apellido,
            empleado.dni_cuil
        ])

    tabla = Table(
        datos,
        colWidths=[150, 150, 120]
    )

    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    elementos.append(tabla)
    elementos.append(Spacer(1, 15))

    elementos.append(
        Paragraph(
            f"Total de empleados: {empleados.count()}",
            styles['Normal']
        )
    )

    pdf.build(elementos)

    return response


def reporte_materias_primas(request):
    materias_primas = MateriaPrima.objects.all()

    return render(
        request,
        'reports/reporte_materias_primas.html',
        {'materias_primas': materias_primas}
    )


def reporte_materias_primas_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte_materia_prima.pdf"'

    pdf = SimpleDocTemplate(response)
    materias_primas = MateriaPrima.objects.all()
    styles = getSampleStyleSheet()

    generado_por = request.user.get_display_name2()

    elementos = []

    elementos.append(
        Paragraph(
            "ASERRAMATIC",
            styles['Title']
        )
    )

    elementos.append(
        Paragraph(
            "Reporte de Materias Primas",
            styles['Heading2']
        )
    )

    elementos.append(
        Paragraph(
            f"Fecha de emisión: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            styles['Normal']
        )
    )

    elementos.append(
        Paragraph(
            f"Reporte generado por: {generado_por}",
            styles['Normal']
        )
    )

    elementos.append(Spacer(1, 20))

    datos = [[
        'Especie',
        'Cantidad de Rollizos',
        'Fecha de Ingreso'
    ]]

    for materia in materias_primas:
        datos.append([
            materia.especie,
            materia.cantidad_rollizos,
            materia.fecha_ingreso.strftime('%d/%m/%Y')
        ])

    tabla = Table(
        datos,
        colWidths=[180, 150, 140]
    )

    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    elementos.append(tabla)
    elementos.append(Spacer(1, 15))

    elementos.append(
        Paragraph(
            f"Total de materias primas: {materias_primas.count()}",
            styles['Normal']
        )
    )

    pdf.build(elementos)

    return response

def reporte_productos(request):
    productos = Producto.objects.all()

    return render(
        request,
        'reports/reporte_productos.html',
        {'productos': productos}
    )


def reporte_productos_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte_productos.pdf"'

    pdf = SimpleDocTemplate(
        response,
        pagesize=landscape(letter)
    )

    productos = Producto.objects.all()
    styles = getSampleStyleSheet()

    generado_por = request.user.get_display_name2()

    elementos = []

    elementos.append(
        Paragraph(
            "ASERRAMATIC",
            styles['Title']
        )
    )

    elementos.append(
        Paragraph(
            "Reporte de Productos",
            styles['Heading2']
        )
    )

    elementos.append(
        Paragraph(
            f"Fecha de emisión: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            styles['Normal']
        )
    )

    elementos.append(
        Paragraph(
            f"Reporte generado por: {generado_por}",
            styles['Normal']
        )
    )

    elementos.append(Spacer(1, 20))

    datos = [[
        'Nombre',
        'Materia Prima',
        'Espesor',
        'Ancho',
        'Largo',
        'Cantidad',
        'Pies Tablares'
    ]]

    for producto in productos:
        datos.append([
            producto.nombre,
            producto.materia_prima.especie,
            f'{producto.espesor_pulgadas}"',
            f'{producto.ancho_pulgadas}"',
            f"{producto.largo_pies} pies",
            producto.cantidad_piezas,
            f"{producto.total_pies_tablares():.2f}"
        ])

    tabla = Table(
        datos,
        colWidths=[120, 110, 70, 70, 70, 70, 90]
    )

    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    elementos.append(tabla)
    elementos.append(Spacer(1, 15))

    elementos.append(
        Paragraph(
            f"Total de productos: {productos.count()}",
            styles['Normal']
        )
    )

    pdf.build(elementos)

    return response