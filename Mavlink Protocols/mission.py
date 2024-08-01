from pymavlink import mavutil, mavwp


the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (the_connection.target_system, the_connection.target_component))

wp= mavwp.MAVWPLoader()
frame= mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT

def mission(seq,lat,lon,alt):
    wp.add(mavutil.mavlink.MAVLink_mission_item_message(
        the_connection.target_system, 
        the_connection.target_component,
        seq,frame,176,
        0,0,0,0,0,0,lat,lon,alt))

    the_connection.waypoint_clear_all_send()
    the_connection.waypoint_count_send(wp.count())
    
    for i in range (wp.count()):
        msg= the_connection.recv_match(type=["MISSION_REQUEST"], blocking= True)
        msg2= the_connection.recv_match(type=["COMMAND_ACK"], blocking= True)
        the_connection.mav.send(wp.wp(msg.seq))
        print("Sending waypoints {0}".format(msg.seq))
        print(msg2)


mission(0, 39.9234948, 32.8456610, 30)
mission(1, 39.9244739, 32.8457174, 30)
mission(2, 39.9246899, 32.8471819, 30)
mission(3, 39.9242271, 32.8483540, 30)
mission(4, 39.9233590, 32.8480804, 30)
