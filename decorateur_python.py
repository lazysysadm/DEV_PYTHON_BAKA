#!/bin/python3.6

import os
import subprocess
import getopt
import sys

user = "Lambda"

def mon_decorateur(fonction):
    def autre_fonction():
        print("Action denied")

    if user != "Lambda":
        return autre_fonction

    return fonction

@mon_decorateur
def do_that():
    print("Execute Instrauctions")

do_that()