from uvicorn.logging import logging

import os
import sys
import json

from collections import OrderedDict
from time import sleep

days = OrderedDict(())

cur_dir = os.path.dirname(__file__)


def run_challenges():
    for day in os.listdir(cur_dir):
        if "day" in day and "py" not in day:
            for ch in os.listdir(f"{cur_dir}/{day}"):
                if day not in days:
                    days[day] = [ch]
                else:
                    days[day].append(ch)
    auto_run = False
    day_input = 0
    ch_input = 0
    print(f"\n\n\n\n")
    # small change to reload
    # + autorun
    while(not auto_run):
        with open(f"{cur_dir}/auto_run.json") as json_file:
            data = json.load(json_file)
            if data["auto_run"] == True:
                auto_run = True
                day_input = data["day"]
                ch_input = data["challenge"]
            
        print("Welcome to Hyphen's AdventOfCode December!")
        if auto_run:
            print("AUTOMATIC RUN TURNED ON, SKIPPING MENU")

        if not auto_run:
            [print(f"{list(days.keys()).index(k)+1}) To choose {k}") for k in days]
            day_input = int(input(f"What Day would you like to see?\n"))
        ch_dic = list(days.items())[(day_input-1)]
        chosen_day = ch_dic[0]
        print(f"You chose: {chosen_day}")

        challenges = [ch for ch in ch_dic[1] if "ch" in ch]

        if not auto_run:
            [print(f"{i+1}) To choose {challenges[i]}") for i in range(len(challenges))]
            ch_input = int(input(f"What Challenge would you like to see?\n"))
        
        chosen_challenge = challenges[(ch_input-1)]

        print(f"You chose: {chosen_challenge}")
        print("Starting.")

        sleep(1/40)
        print(". . . .")
        sleep(1/40)
        print(". . .")
        sleep(1/40)
        print(". .")
        sleep(1/40)
        print(".")
        sleep(1/2)
        print(f"Day {day_input}: Challenge {ch_input} [START]\n")

        os.system(f"python {cur_dir}/{chosen_day}/{chosen_challenge}")
        
        print(f"\nDay {day_input}: Challenge {ch_input} [END]")
        sleep(1/40)
        print(". ")
        sleep(1/40)
        print(". . ")
        sleep(1/40)
        print(". . .")
        sleep(1/40)
        print(". . . .")
        sleep(1/2)
