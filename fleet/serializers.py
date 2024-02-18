from rest_framework import serializers
from Users.models import Fleets
from .models import Notifications
# ,DrowsyDetails
class GetAllFleetSerializer(serializers.ModelSerializer):

    class Meta:
        model=Fleets
        fields='__all__'
    
class SendNotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Notifications
        fields='__all__'

# class SaveDrowsyDetailsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model=DrowsyDetails
#         fields=["fleet"]