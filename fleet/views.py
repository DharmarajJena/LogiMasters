from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from Users.models import Fleets
from .models import Notifications
# ,DrowsyDetails,Device
from .serializers import GetAllFleetSerializer,SendNotificationSerializer
# ,SaveDrowsyDetailsSerializer
import websockets,json, asyncio

class GetAllFleets(viewsets.ModelViewSet):
    queryset=Fleets.objects.all()
    serializer_class=GetAllFleetSerializer

    def list(self,request):
        serialized_data=self.serializer_class(self.queryset,many=True).data
        print(serialized_data)
        return Response(serialized_data)

async def send_notification(uri, data):
    print("hello")
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps(data))
            asyncio.sleep(2)
            await websocket.close()
    except Exception as e:
        print(f"Error sending notification: {e}")

#To send a new notification, it saves the notification in database and also sends to the fleet in real time. If the connection is already
        #established with the fleet it will show the notification to the driver which will pop on arrival of notification.
#If the notification is sent earlier and the fleet opens the app it has to go the old notifications section which will hit an api and will get all the old notifications based on its license number.
class SendNotifications(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = SendNotificationSerializer

    def create(self, request):
        data = request.data 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            registration_no = data['registration_no']
            fleets = Fleets.objects.filter(registration_no=registration_no).first()
            if fleets:
                serializer.save()
                websocket_uri = f"wss://logimasterssilicon.onrender.com/ws/sendnotification/{registration_no}/"
                print("hii")
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    loop.run_until_complete(send_notification(websocket_uri, serializer.data))
                    loop.close()
                    print("hii 2")
                
                    return Response({'message': 'Notification sent'}, status.HTTP_201_CREATED)
                except Exception as e:
                    return Response({'message':'Notification not sent'})
                # else:
                #     return Response({'message': 'Failed to send notification'}, status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'message': 'License no. does not exist'}, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
#To do :- Make a api to get all the notifications of the respective fleet.
    
class GetAllNotifications(viewsets.ModelViewSet):
    queryset=Notifications.objects.all()
    serializer_class=SendNotificationSerializer

    def list(self,request):
        serialized_data=self.serializer_class(self.queryset,many=True).data
        print(serialized_data)
        return Response(serialized_data)
    
# from firebase_admin import messaging

# def send_push_notification(token, title, body):
#     message = messaging.Message(
#         notification=messaging.Notification(title=title, body=body),
#         token=token,
#     )
#     response = messaging.send(message)
#     print('Successfully sent message:', response)

# class SaveDrowsyDetails(viewsets.ModelViewSet):
#     queryset=DrowsyDetails.objects.all()
#     serializer_class=SaveDrowsyDetailsSerializer

#     def create(self, request, *args, **kwargs):
#         data=request.data 
#         data['fleet']=Fleets.objects.get(hardware_id=data['fleet']).id
#         serializer=self.serializer_class(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             firebase_token=Device.objects.get(user=request.user).firebase_token
#             send_push_notification(firebase_token,"Alert","Drowsy Detected!")

#             return Response({"Message":"Got the drowsy details"})
#         return Response({"Message":"Invalid drowsy details"})
