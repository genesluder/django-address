import googlemaps

from django.conf import settings

from address.models import create_address


def geolocate(address):

    gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
    response = gmaps.geocode(address)

    if isinstance(response, list) and len(response) > 0:
        result = response[0]
        data = {}
        # Grab address components
        address_components = result.get('address_components')
        if address_components:
            component_map = [
                ('street_number', 'street_number'),
                ('route', 'route'),
                ('neighborhood', 'neighborhood'),
                ('locality', 'locality'),
                ('administrative_area_level_1', 'state'),
                ('country', 'country'),
                ('postal_code', 'postal_code'),
            ]
            for comp in address_components:
                for item in component_map:
                    if item[0] in comp['types']:
                        data[item[1]] = comp['long_name']


        if 'formatted_address' in result:
            data['formatted'] = result['formatted_address']

        if 'place_id' in result:
            data['place_id'] = result['place_id']

        if 'geometry' in result and 'location' in result['geometry']:
            data['lat'] = result['geometry']['location']['lat']
            data['lng'] = result['geometry']['location']['lng']

        data['raw'] = address

        return data


def resolve_address(raw_address):
    result = geolocate(raw_address)
    if result:
        result['raw'] = raw_address
        return create_address(result)
    return None

