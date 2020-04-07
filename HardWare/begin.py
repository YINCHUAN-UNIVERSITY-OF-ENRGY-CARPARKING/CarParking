'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-07 20:22:08
@LastEditors: Mar Ping
@LastEditTime: 2020-04-07 23:30:34
'''
import serial
import serial.tools.list_ports

#----------------------------------串口查找函数-------------------------------------------

def find_port():
    port_list = list(serial.tools.list_ports.comports())

    if len(port_list) == 0:
        return False
    else:
        return port_list                               #返回包含所有端口的列表

#----------------------------------串口初始化---------------------------------------------

def start_port(ports,speed,timex):                      #端口_波特率_超时时间

    if find_port() == False:
        return False
    else:
        ser = serial.Serial()
        ser.port = ports
        ser.baudrate = speed
        ser.timeout = timex
        ser.open()

    return ser




