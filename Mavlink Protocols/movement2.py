from pymavlink import mavutil
import time

the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (the_connection.target_system, the_connection.target_component))


#the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(0, the_connection.target_system,
#                         the_connection.target_component, 1, int(0b010111111000), 
#                         0, 500, -50, 
#                         0, 0, 0, 
#                         0, 0, 0, 
#                         0, 0))

the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_global_int_message(0, the_connection.target_system,
                        the_connection.target_component, 6, int(0b110111111000), 
                        int(10.06260021551959 * 10 ** 7), int(-2.4980322869905915 * 10 ** 7), 60, 
                        0, 0, 0, 
                        0, 0, 0, 
                        0,0))


while 1:
    msg = the_connection.recv_match(
        type='LOCAL_POSITION_NED', blocking=True)
    print(msg)

    time(60)