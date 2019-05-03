#!/usr/bin/env python3

import data_center

def init():
    data_center.main_loop_phase = "run"
    data_center.world_structure = data_center.WorldStructure()
    print("init:" + data_center.world_structure)

def main():
    print("run")

    data_center.main_loop_phase = "exit"

if __name__ == "__main__":
    while True:
        if data_center.main_loop_phase == "begin":
            init()
        elif data_center.main_loop_phase == "run":
            main()
        elif data_center.main_loop_phase == "exit":
            exit()