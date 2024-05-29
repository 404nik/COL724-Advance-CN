from config import get_config
from client import client
from queue import Queue
import threading
import time
import csv
import numpy as np

def client_logic(config):
    q1 = Queue(100)
    q2 = Queue(100)

    def rcv1(q):
        while True:
            msg = config.client.recv_uno()
            q.put(msg)

    def rcv2(q):
        while True:
            msg = config.client.recv_tom()
            q.put(msg)

    def send_commands():
        with open(config.com, 'r') as f:
            reader = csv.reader(f)
            cmd = list(reader)
            for item in cmd:
                if item[0] == "Multicast" and item[1] == config.id:
                    config.client.send_tom((config.id + "###" + item[2]).encode())
                elif item[0] == "sleep":
                    time.sleep(int(item[1]))
                elif item[0] == config.id:
                    config.client.send_uno(item[1].encode(), (config.id + "###" + item[2]).encode())

    def tom_uno():
        cmd_list = []
        seq_list = []
        l_seq_num = 0

        with open(config.o + f"/test_result_{config.id}_tom.txt", 'wb', 0) as g, \
             open(config.o + f"/test_result_{config.id}_uno.txt", 'wb', 0) as h:
            while True:
                if not q1.empty():
                    item1 = q1.get()
                    h.write((item1.decode("ascii") + "\n").encode())

                if not q2.empty():
                    item2 = q2.get()
                    if len(item2) == 1:
                        cmd_list.append(item2)
                    else:
                        seq_list.append(item2)

                if len(seq_list) > 0:
                    if int(seq_list[0][1].decode("ascii")) == (l_seq_num + 1):
                        if [seq_list[0][0]] in cmd_list:
                            idx = cmd_list.index([seq_list[0][0]])
                            g.write((cmd_list[idx][0].decode("ascii") + "\n").encode())
                            del cmd_list[idx]
                            del seq_list[0]
                            l_seq_num += 1

    threading.Thread(target=rcv1, args=(q1,)).start()
    threading.Thread(target=rcv2, args=(q2,)).start()
    threading.Thread(target=send_commands).start()
    threading.Thread(target=tom_uno).start()