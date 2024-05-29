from queue import Queue
import threading
import time
import csv
import numpy as np
from config import get_config
from client import client_

def sequencer_logic(config):
    g_seq_num = 0

    while True:
        msg = config.client.recv_tom()
        if len(msg) == 1:
            g_seq_num += 1
            config.client.send_tom(msg[0], str(g_seq_num).encode())
