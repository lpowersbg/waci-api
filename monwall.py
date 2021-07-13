# https://github.com/NECDisplaySolutions/necpdsdk
# Requires this

from nec_pd_sdk.nec_pd_sdk import *

host = '192.168.0.1'

def monoff():
    mon = NECPD.open(host)
    mon.helper_set_destination_monitor_id('ALL')
    mon.command_power_status_set(4)
    mon.close()

def monon():
    mon = NECPD.open(host)
    mon.helper_set_destination_monitor_id('ALL')
    mon.command_power_status_set(1)
    mon.close()