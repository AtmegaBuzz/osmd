import json
from asgiref.sync import async_to_sync
from channels.generic.websocket  import WebsocketConsumer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print("connected")
        #join group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        print(self.room_group_name,"--|--",self.channel_name)
        
        self.accept()
        
         
    def disconnect(self,close_code):
        #leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
    #recieve message from websocket
    def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        #send message to the room
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )
        
    #recieve message from chat room
    
    def chat_message(self,event):
        message = event['message']
        
        #send message to websocket
        self.send(text_data=json.dumps({
            'message':message
        }))
        
    
        
    