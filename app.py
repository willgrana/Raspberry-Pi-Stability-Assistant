from flask import *
import time
from gpiozero import CPUTemperature
import subprocess
import psutil
import logging
import smbus

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

BUS = smbus.SMBus(1)
ADDRESS = 0x48

@app.route('/', methods=['GET'])
def home():
	return(app.send_static_file("temp.html"))

@app.route('/tempdata', methods=['GET'])
def gettemp():
	#Get temp
	cpu = CPUTemperature()
	temperature = cpu.temperature
	#Get Frequency
	f = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")
	coreclock = (int(f.read()) / 1000)
	#Get Voltage
	process = subprocess.Popen(['vcgencmd measure_volts'],shell=True,stdout=subprocess.PIPE)
	output = process.stdout.readline()
	voltage = output[:12]
	voltage = voltage.decode('utf8')
	voltage = voltage[5:]
	#Get CPU Usage
	cpuusage = str(psutil.cpu_percent())
	#Get Ram Usage
	ramusage = str(psutil.virtual_memory()[2])
	#Get Ambient Temp
	rvalue0 = BUS.read_word_data(ADDRESS,0)
	rvalue1 = (rvalue0 & 0xff00) >> 8
	rvalue2 = rvalue0 & 0x00ff
	rvalue = (((rvalue2 * 256) + rvalue1) >> 4 ) * .0625
	ambienttemp = str(rvalue)
	#Return Data
	data = "CPU Temperature: "+str(temperature)+"&#176 Celsius"+"<br>"+"Core Frequency: "+str(coreclock)+" Mhz"+"<br>"+"Core Voltage: "+voltage+"<br>"+"CPU Usage: "+cpuusage+" %"+"<br>"+"Ram Usage: "+ramusage+" %"+"<br>"+"Ambient Temperature/Oil Bath Temperature: "+ambienttemp+"&#176 Celsius"
	return(data)
