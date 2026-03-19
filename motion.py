#!/usr/bin/env python

import argparse
import rospy
import baxter_interface
from baxter_interface import CHECK_VERSION

import time

def run_file():

    left = baxter_interface.Limb('left')
    right = baxter_interface.Limb('right')
    grip_left = baxter_interface.Gripper('left', CHECK_VERSION)
    grip_right = baxter_interface.Gripper('right', CHECK_VERSION)
    lj = left.joint_names()
    rj = right.joint_names()
    print(lj)

    left.move_to_joint_positions({
        'left_s0': -.78,
        'left_s1': .78,
        'left_e0': 3.14,
        'left_e1': 0.8,
        'left_w0': 1.57,
        'left_w1': 0,
        'left_w2': 0,
    })
    # debug
    #mov_list = {1, 1.1, 2, 2.1, 3, 3.1}
    
    # Sequence 1
    #mov_list = [4, 1, 3, 1.1, 4.1, 4, 1, 3.1, 1.1, 4.1]

    # Sequence 2
    #mov_list = [4, 2, 4.1, 4, 2.1, 4.1]

    # Sequence 3
    mov_list = [2, 4, 1, 4.1, 1.1]

    # Sequence 4
    mov_list = [2, 2.2, 1, 3, 3.1, 2, 1.1]

    for m in mov_list:
        if m == 1:
            print("Flex Elbow")
            left.move_to_joint_positions({'left_e1': 2.5})
        if m == 1.1:
            print("Extend Elbow")
            left.move_to_joint_positions({'left_e1': 0.8})
        if m == 2:
            print("Wrist pronate")
            left.move_to_joint_positions({'left_w0': 3.0})
        if m == 2.1:
            print("Wrist supinate")
            left.move_to_joint_positions({'left_w0': 1.57})
        if m == 2.2:
            print("Wrist super supinate")
            left.move_to_joint_positions({'left_w0': 0})
        if m == 3:
            print("Wrist flex")
            left.move_to_joint_positions({'left_w1': 1.57})
        if m == 3.1:
            print("Wrist extend")
            left.move_to_joint_positions({'left_w1': 0})
        if m == 4:
            print("grip")
            grip_left.close()
            print("gripped sleep start")
            time.sleep(2)
            print("gripped sleep end")
        if m == 4.1:
            print("open grip")
            grip_left.open()
            print("opened sleep start")
            time.sleep(2)
            print("opened sleep end")

def main():
    epilog = """
    See help inside the example with the '?' key for key bindings.
        """
    arg_fmt = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=arg_fmt,
                                     description=main.__doc__,
                                     epilog=epilog)
    parser.parse_args(rospy.myargv()[1:])

    print("Initializing node... ")
    rospy.init_node("rsdk_test")
    print("Getting robot state... ")
    rs = baxter_interface.RobotEnable(CHECK_VERSION)
    init_state = rs.state().enabled

    def clean_shutdown():
        print("\nExiting example...")
        if not init_state:
            print("Disabling robot...")
            rs.disable()
    rospy.on_shutdown(clean_shutdown)

    print("Enabling robot... ")
    rs.enable()

    run_file()
   

if __name__ == '__main__':
    main()
