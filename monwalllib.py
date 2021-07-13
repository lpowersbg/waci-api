from nec_pd_sdk.nec_pd_sdk import *

mon = NECPD.open('192.168.0.1')
mon.helper_set_destination_monitor_id('ALL')

mon.command_power_status_set(1)

mon.close()