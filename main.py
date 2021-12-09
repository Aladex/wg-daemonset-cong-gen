#!/usr/bin/python3
import os
import yaml

def read_map():
    pod_name = os.getenv("MY_NODE_NAME")
    print(pod_name)
    pod_map = open("/wg-map.yaml").read()
    pod_keys = yaml.safe_load(pod_map)
    for pod in pod_keys["servers"]:
        if pod["name"] == pod_name:
            return pod.get("net")

if __name__ == "__main__":
    wg_net = read_map()
    print(wg_net)

    if wg_net != None:
        try:
            wg_conf = open("/config/wg0.conf").read()
            wg_pod_conf = wg_conf.replace("10.13.13", wg_net)
            new_conf = open("/config/wg0.conf", "w")
            new_conf.write(wg_pod_conf)
            new_conf.close()
        except Exception as e:
            print("No wg0.conf")
            print(e)
            quit()
