from datetime import datetime
from django.shortcuts import render
from myapp.models import Airport
from .utils import get_flight_data ,city_to_iata

def home(request):
    return render(request, 'myapp/home.html')

def search_form(request):
    return render(request, 'myapp/flights.html')

def search_results(request):
    source_city = request.GET.get('source', '').strip()
    destination_city = request.GET.get('destination', '').strip()
    departure_date_str = request.GET.get('departure', '').strip()  # format: yyyy-mm-dd

    flights = []
    error_msg = ''
    departure_date = None

    if departure_date_str:
        try:
            departure_date = datetime.strptime(departure_date_str, '%Y-%m-%d').date()
        except ValueError:
            error_msg = "Invalid departure date."

    if source_city and destination_city and departure_date and not error_msg:
        source = city_to_iata(source_city)
        destination = city_to_iata(destination_city)

        if not source or not destination:
            error_msg = "Invalid city name. Please enter valid cities like Delhi or Mumbai."
        else:
            try:
                # Removed SearchQuery.objects.create(...) since saving is not required
                flights = get_flight_data(source, destination, None, '')
            except Exception as e:
                error_msg = f"Error fetching flight data: {str(e)}"

    context = {
        'source': source_city,
        'destination': destination_city,
        'departure_date': departure_date_str,
        'flights': flights,
        'error_msg': error_msg,
    }
    return render(request, 'myapp/results.html', context)


def popular_routes(request):
    return render(request, 'myapp/popular_routes.html')

def airport_info_view(request):
    if request.method == 'POST':
        airport_name = request.POST.get('airport_name')
        airport = Airport.objects.filter(name=airport_name).first()
        return render(request, 'myapp/airport_result.html', {'airport': airport})

    airports = Airport.objects.all()
    return render(request, 'myapp/airport_info.html', {'airports': airports})

def travel(request):
    return render(request, 'myapp/travel_tip.html')

