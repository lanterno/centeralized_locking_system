import factory

from .models import Resource


class ResourceFactory(factory.django.DjangoModelFactory):
    '''
    Automatically create resources with good names
    '''
    class Meta:
        model = Resource

    name = factory.Faker('file_name')
