import paho.mqtt.client as mqttClient
import Adafruit_DHT as dht
import time as t
 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
 
        print("Conectado ao Broker")
        global Connected                
        Connected = True
        
    else:
 
        print("Falha na conexão!")

Connected = False 
broker_address= "ENDEREÇO DO BROKER"
port = 'PORTA'
user = "SEU USUARIO"
password = "SUA SENHA"
 
client = mqttClient.Client("Publicador")               
client.username_pw_set(user, password=password)    
client.on_connect= on_connect                      
client.connect(broker_address, port=port)          
client.loop_start()       
 
while Connected != True:   
    t.sleep(0.1)
 
try:
    while True:
    
        umid, temp = dht.read_retry(dht.DHT11, 4)
        atemp = ('Temperatura: {0:0.1f}\nUmidade: {1:0.1f}'.format(temp, umid))
        print(a)
        client.publish("temp",a)
        t.sleep(4)
        
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()