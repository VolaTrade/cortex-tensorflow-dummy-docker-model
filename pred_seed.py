import requests 
from random import randint
from json import dumps

def get_pseduo_random_row():
    return {"instances": [[
        float(randint(20000, 30000)), float(randint(20000, 30000)), float(randint(20000, 30000)), 
        float(randint(20000, 30000)), float(randint(20000, 30000)), float(randint(20000, 30000)),
        float(randint(20000, 30000)), float(randint(20000, 30000)), float(randint(20000, 30000)), 
        float(randint(20000, 30000)), float(randint(20000, 30000)), 
        0.09283, 0.006, 0.048998, 0.085046, 0.022647, 1.999338, 0.006, 0.033589, 0.006, 23123.59, 23124.11, 23124.12, 23124.64, 23124.65, 23124.66, 23124.79, 23125.08, 23125.24, 23125.72, 9.455407, 0.003, 0.006, 2.70083, 4.7, 0.006, 0.621, 0.021627, 1000]]}


if __name__ == '__main__':
    while True: 
        resp = requests.post(
                "http://localhost:8501/v1/models/dummy-rnn:predict", 
                data=dumps(get_pseduo_random_row()),
                headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

                )

        print(resp.status_code)
        print(resp.json())
