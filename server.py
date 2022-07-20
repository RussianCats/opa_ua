from opcua import Server
from random import randint
import time
import datetime
import os
from threading import Thread

server =Server()
url="opc.tcp://192.168.216.22:4841"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_Server"
addSpace =server.register_namespace(name)

node=server.get_objects_node()

ServerInfo=node.add_object(addSpace,"OPC Simulation Server")
Param = node.add_object(addSpace, "Parameters")

Temp=Param.add_variable(addSpace, "Temperature",0)
Press=Param.add_variable(addSpace, "Pressure",0)
Time=Param.add_variable(addSpace, "Time",0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

server.start()
print ("Server started at {}".format(url))
print("\nДля выхода введите любое число\n")
def fun():
  while True:
    Temperature = randint (10,50)
    Pressure = randint(200,999)
    TIME= datetime.datetime.now()
    print(Temperature, Pressure, TIME)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)
    time.sleep(1)

def stop():
  while True:
    try:
      answer = int(input("\n"))
    except TypeError:
      print("\nContinue\n")
    else:
      print("\nExit\n")
      break
  os.system("pkill python3")
thread1 = Thread(target = fun)
thread2 = Thread(target = stop)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
