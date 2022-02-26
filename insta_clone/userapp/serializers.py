from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Account

class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields = ["id", 'full_name', 'username','bio','profile_pic','private','user','following','followers']
