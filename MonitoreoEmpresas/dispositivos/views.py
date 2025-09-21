from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from datetime import datetime, timedelta
from .models import Device, Zone, Category, Measurement, Alert
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    try:
        org = request.user.userprofile.organization
    except AttributeError:
        return render(request, 'dispositivos/dashboard.html', {'error': 'No tienes una organización asignada.'})

    one_week_ago = datetime.now() - timedelta(days=7)

    alerts_by_severity = Alert.objects.filter(device__organization=org, timestamp__gte=one_week_ago).values('severity').annotate(count=Count('id'))

    context = {
        'devices_by_category': Device.objects.filter(organization=org).values('category__name').annotate(count=Count('id')),
        'devices_by_zone': Device.objects.filter(organization=org).values('zone__name').annotate(count=Count('id')),
        'latest_measurements': Measurement.objects.filter(device__organization=org).order_by('-timestamp')[:10],
        'alerts_by_severity': alerts_by_severity,
    }
    return render(request, 'dispositivos/dashboard.html', context)

@login_required
def device_list(request):
    org = request.user.userprofile.organization
    devices = Device.objects.filter(organization=org)

    categoria_id = request.GET.get('categoria')
    if categoria_id:
        devices = devices.filter(category_id=categoria_id)

    categories = Category.objects.filter(organization=org)

    return render(request, 'dispositivos/device_list.html', {'devices': devices, 'categories': categories})

@login_required
def device_detail(request, device_id):
    org = request.user.userprofile.organization
    device = get_object_or_404(Device, id=device_id, organization=org)
    measurements = Measurement.objects.filter(device=device).order_by('-timestamp')
    alerts = Alert.objects.filter(device=device).order_by('-timestamp')

    return render(request, 'dispositivos/device_detail.html', {'device': device, 'measurements': measurements, 'alerts': alerts})

@login_required
def alert_list(request):
    org = request.user.userprofile.organization
    one_week_ago = datetime.now() - timedelta(days=7)
    alerts = Alert.objects.filter(device__organization=org, timestamp__gte=one_week_ago).order_by('-timestamp')

    return render(request, 'dispositivos/alert_list.html', {'alerts': alerts})

@login_required
def measurement_list(request):
    org = request.user.userprofile.organization
    measurements = Measurement.objects.filter(device__organization=org).order_by('-timestamp')[:50]

    return render(request, 'dispositivos/measurement_list.html', {'measurements': measurements})

@login_required
def zone_list(request):
    org = request.user.userprofile.organization
    zones = Zone.objects.filter(organization=org)

    return render(request, 'dispositivos/zone_list.html', {'zones': zones})

@login_required
def category_list(request):
    org = request.user.userprofile.organization
    categories = Category.objects.filter(organization=org)

    return render(request, 'dispositivos/category_list.html', {'categories': categories})