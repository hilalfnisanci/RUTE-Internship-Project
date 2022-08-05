import random, json
from paho.mqtt import client as mqtt_client

class Mqtt():

    broker = 'localhost'
    topic = 'mqtt'
    client_id = f'python-mqtt-{random.randint(0, 100)}'
    barName = []
    value = []
    file = open('data.json')
    data = json.load(file)
    btnValue = []
    scrollDict = {}

    angle = None

    def on_connect(client, userdata,  flags, rc):
        client.subscribe(Mqtt().topic)
        
        for i in Mqtt.data['data']:
            client.publish(Mqtt.topic, json.dumps(i))
        # client.publish(Mqtt().topic, Mqtt().mqtt_msg)

    def on_publish(client, userdata, mid):
        print("Message published")
    
    def on_message(client, userdata,msg):
        # print(" **************  msg  ************** \n",msg.payload, " \n**************  msg  ************** \n")
        payload = json.loads(msg.payload)

        temp = str(msg.payload).find("barName")
        temp2 = str(msg.payload).find("btnValue")

        if temp != -1:
            if not payload['barName'] in Mqtt.barName:
                Mqtt.barName.append(payload['barName'])
                Mqtt.value.append(float(payload['value']))
            else:
                i = Mqtt.barName.index(payload['barName'])
                Mqtt.value[i] = float(payload['value'])

        if temp2 != -1:
            Mqtt.btnValue.clear()
            Mqtt.btnValue.append(int(payload['btnValue']))

        if (str(msg.payload).find("pantoScroll")) != -1:
            Mqtt.scrollDict["pantoScroll"] = int(payload["pantoScroll"])

        if (str(msg.payload).find("frenScroll")) != -1:
            Mqtt.scrollDict["frenScroll"] = int(payload["frenScroll"])
        
        if (str(msg.payload).find("mcbScroll")) != -1:
            Mqtt.scrollDict["mcbScroll"] = int(payload["mcbScroll"])

        if (str(msg.payload).find("gaugeMeterAngle")) != -1:
            Mqtt.angle = int(payload["gaugeMeterAngle"])

    def takeData(barName):
        for i in range(len(Mqtt.barName)):
            if barName == Mqtt.barName[i]:
                return Mqtt.value[i]

    def run(value):
        client = mqtt_client.Client(client_id=Mqtt().client_id)
        client.on_publish = Mqtt.on_publish
        client.on_connect = Mqtt.on_connect
        client.on_message = Mqtt.on_message
        client.connect(Mqtt().broker, 1883)

        if value == 1:
            client.loop_start()
            print("loop start")
            
        elif value == 0:
            client.loop_stop()
            client.disconnect()
            print("loop stop")

