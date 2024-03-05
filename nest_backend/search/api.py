from django.http import JsonResponse
from rest_framework.decorators import api_view

from account.models import User
from account.serializers import UserSerializer

from django.db.models import Q

@api_view(['POST'])
def search(request):
    data = request.data
    query = data.get('query', '')

    # Define the fields you want to search on
    search_fields = ['username', 'email']

    # Create a Q object that combines queries for each field
    search_query = Q()

    for field in search_fields:
        if '__' in field:
            # If it's a related field, navigate through relationships
            related_fields = field.split('__')
            current_query = Q()
            for related_field in related_fields:
                current_query |= Q(**{f'{related_field}__icontains': query})
            search_query |= current_query
        else:
            # If it's a direct field, use icontains directly
            search_query |= Q(**{f'{field}__icontains': query})

    # Use the Q object in the filter to get the matching users
    users = User.objects.filter(search_query)

    users_serializer = UserSerializer(users, many=True)

    return JsonResponse({
        'users': users_serializer.data
    }, safe=False)
