from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Device, Zone, Category, Organization, Measurement, Alert

# Create your views here.

def dashboard(request):
    org_id = request.session.get('organization_id')
    if not org_id:
        return redirect('login')

    context = {
        'devices_by_category': Device.objects.filter(organization_id=org_id).values('category__name').annotate(count=Count('id')),
        'devices_by_zone': Device.objects.filter(organization_id=org_id).values('zone__name').annotate(count=Count('id')),
        'latest_measurements': Measurement.objects.filter(device__organization_id=org_id).order_by('-timestamp')[:10],
    }
    return render(request, 'dispositivos/dashboard.html',context)

def device_list(request):
    org_id = request.session.get('organization_id')
    if not org_id:
        return redirect('login')

    devices = Device.objects.filter(organization_id=org_id)
    categories = Category.objects.filter(organization_id=org_id)

    return render(request, 'dispositivos/device_list.html', {'devices': devices, 'categories': categories})

def device_detail(request, device_id):
    org_id = request.session.get('organization_id')
    if not org_id:
        return redirect('login')

    device = get_object_or_404(Device, id=device_id, organization_id=org_id)
    measurements = Measurement.objects.filter(device=device).order_by('-timestamp')
    alerts = Alert.objects.filter(device=device).order_by('-timestamp')

    return render(request, 'dispositivos/device_detail.html', {'device': device, 'measurements': measurements, 'alerts': alerts})