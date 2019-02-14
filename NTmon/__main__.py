from networktables import NetworkTables
import sys
import screen as scrn
import os

if len(sys.argv) != 2:
    print("Usage: python3 NTmon 10.TE.AM.2")
    exit(1)

NetworkTables.initialize(server=sys.argv[1])

def fmslisten(table, key, value, isNew):
    if key in scrn.screen_data and value == scrn.screen_data["fms_"+key]:
        return
    scrn.screen_data["fms_"+key] = f"FMSINFO: {key}:{value}"
    scrn.printscrn(scrn.screen_data)

def tellisten(table, key, value, isNew):
    if key in scrn.screen_data and value == scrn.screen_data["tel_"+key]:
        return
    scrn.screen_data["tel_"+key] = f"TELEMETRY: {key}:{value}"
    scrn.printscrn(scrn.screen_data)

def sdlisten(table, key, value, isNew):
    if key in scrn.screen_data and value == scrn.screen_data["sd_"+key]:
        return
    scrn.screen_data["sd_"+key] = f"SMARTDASHBOARD: {key}:{value}"
    scrn.printscrn(scrn.screen_data)

print("Connecting to FMSinfo")
fms = NetworkTables.getTable("FMSInfo")
fms.addEntryListener(fmslisten)

print("Connecting to SmartDashboard")
tel =  NetworkTables.getTable("SmartDashboard/Telemetry")
tel.addEntryListener(tellisten)

print("Connecting to SmartDashboard")
sd =  NetworkTables.getTable("SmartDashboard")
sd.addEntryListener(sdlisten)

os.system("clear")

while True:
    continue