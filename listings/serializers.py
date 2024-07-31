from .models import Property
from typing import Iterable, List, Dict, Any

def serialize_properties(properties: Iterable[Property]) -> List[Dict[str, Any]]:
    data = []
    for property in properties:
        data.append({
            'title': property.title,
            'address': property.address,
            'type': property.type,
            'status': property.status,
            'rent_per_month': property.rent_per_month,
            'picture_url': property.picture.url,
        })
    return data
