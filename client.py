from opcua import Client 
import time
from random import randint
import datetime

url = "opc.tcp://192.168.1.15:4840" 

client = Client(url)

client.connect()

print("Client Connected")

while True:
  
  Temp= client.get_node("ns=2;i=4")
  #T = randint(10,50)
  Temperature = Temp.get_value()
  print (Temperature) 

  Press= client.get_node("ns=2;i=3")
  #P = randint(200,999)
  Pressure = Press.get_value()
  print (Pressure)

  TIME= client.get_node("ns=2;i=5")
  #T = datetime.datetime.now()
  TIME_Value = TIME.get_value()
  print (TIME_Value)

  time.sleep(2)
