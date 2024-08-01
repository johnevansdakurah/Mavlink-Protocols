from pymavlink import mavutil

the_connection = mavutil.mavlink_connection('udp:localhost:14551')


the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))


while 1:
    msg = the_connection.recv_match(type="ATTITUDE",blocking=True)
    #msg = the_connection.recv_match(type="MISSION_ITEM", blocking=True)
    print(msg)

    if msg.get_type() == 'MISSION_ITEM':

        # current mission
        # Process mission item
       seq = msg.seq
       frame = msg.frame
       command = msg.command
       param1 = msg.param1
       param2 = msg.param2
       param3 = msg.param3
       param4 = msg.param4
       x = msg.x
       y = msg.y
       z = msg.z

    print(f"Waypoint {seq}: {frame}, {command}, {param1}, {param2}, {param3}, {param4}, {x}, {y}, {z}")