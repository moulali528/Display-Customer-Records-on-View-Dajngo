from django.shortcuts import render, redirect
from .models import CustomerRecords, CustomerDeletedRecords
from .forms import AddRecordForm, DeletedRecordForm
from django.contrib import messages


from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.

def generate_pdf(request):
    buf = io.BytesIO()
    lines = []
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    records = CustomerRecords.objects.all()
    for record in records:
        lines.append(record.first_name + ' ' + record.last_name + '  Details')
        lines.append(record.email)
        lines.append(record.phone)
        lines.append(record.address)
        lines.append(record.city)
        lines.append(record.state)
        lines.append(record.postcode)
        #lines.append(record.created_at)
        #lines.append(record.id)
        lines.append('===========================================\n')
        lines.append(" ")
    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='customer_records.pdf')

def home_page(request):
    records = CustomerRecords.objects.all()
    return render(request, 'home_page.html', {'records':records})

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            messages.success(request, 'Customer record added successfully...')
            return redirect('home')
        
        return render(request, 'add_record.html', {'form':form})
    else:
        return render(request, 'add_record.html', {'form':form})

def update_record(request, record_id):
    record = CustomerRecords.objects.get(id=record_id)
    form = AddRecordForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'update_record.html', {'form':form, 'record': record} )


def delete_record(request, record_id):
    record = CustomerRecords.objects.get(id=record_id)
    record.delete()
    return redirect('home')



