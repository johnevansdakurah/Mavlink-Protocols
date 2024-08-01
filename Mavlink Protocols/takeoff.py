from pymavlink import mavutil
from time import sleep

the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))


def get_current_alt():
    altitude=the_connection.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
    if altitude:
        return (altitude.alt/1000)

def takeoff(alt): 
    the_connection.mav.command_long_send(
        the_connection.target_system, the_connection.target_component, 
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0 ,0,0,0, 0,0,alt)

    msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)

    while 1:
        current_alt = get_current_alt()
        print(f"{abs(current_alt-alt)} meters to takeoff point")

        if abs(current_alt-alt) <= 1:
            print("Takeoff point reached succsfullyy")
            break
    
    sleep(1)


takeoff(50)
