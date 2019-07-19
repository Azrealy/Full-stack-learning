import os 
from multiprocessing import Pool

def run_process(task):
    os.system('JUPYTER_TOKEN=4656a9832efe99b9927940f71b6b04459f3bcea5836d32b7 NOTEBOOK_DIR=examples bash {}'.format(task))


if __name__ == "__main__":
    pool = Pool(processes=30)
    pool.map(run_process, ["~/nbexec/examples/example2_stream.sh" for _ in range(30)])
    pool.close()