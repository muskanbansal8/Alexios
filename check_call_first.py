#!/usr/bin/python
#Python2

import dbus
from incoming_call import incoming_call

def checkfirst():
    while(True):
        bus = dbus.SystemBus()

        manager = dbus.Interface(bus.get_object('org.ofono', '/'),
                                'org.ofono.Manager')

        modems = manager.GetModems()

        for path, properties in modems:
            print "[ %s ]" % (path)
            print("Currently in check_call_first.py")

            if "org.ofono.VoiceCallManager" not in properties["Interfaces"]:
                continue

            mgr = dbus.Interface(bus.get_object('org.ofono', path),
                            'org.ofono.VoiceCallManager')
            
            calls = mgr.GetCalls()
            
            for path, properties in calls:
                state = properties["State"]
                print "[ %s ] %s" % (path, state)
                print("Currently in check_call_first.py")

                if state == "incoming":
                    incoming_call()
                    return 1
                else:
                    return 0

if __name__ == "__main__":
    checkfirst()
