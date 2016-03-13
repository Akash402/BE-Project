import paho.mqtt.client as mqtt # https://eclipse.org/paho/clients/python/
import os,  urlparse
import HeadCounter


# Define event callbacks
def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

client  = mqtt.Client()
# Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#client.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
#os.environ["CLOUDMQTT_URL"] = ""
url_str ='mqtt://qcljoebr:kFD1ZOxwAujW@m10.cloudmqtt.com:10840'
#os.environ.get('CLOUDMQTT_URL', 'mqtt://localhost:1883')
url = urlparse.urlparse(url_str)

# Connect
client.username_pw_set(url.username, url.password)
client.connect(url.hostname, url.port)

# Start subscribe, with QoS level 0
client.subscribe("Canteen/HeadCount", 0)

# Publish a message
client.publish("Canteen/HeadCount", HeadCounter.Percentage)

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = client.loop()
print("rc: " + str(rc))


