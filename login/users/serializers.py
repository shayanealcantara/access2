from rest_framework import serializers
from . import models #importa tudo que tá em models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', )