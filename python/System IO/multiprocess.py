import os
from multiprocessing import Pool

def run_process(task):
    os.system('JUPYTER_TOKEN=c9de56fa4deed24899803e93c227592aef6538f93025fe01 NOTEBOOK_DIR=examples bash {}'.format(task))


if __name__ == "__main__":
    
    pool = Pool(processes=30)
    pool.map(run_process, ["~/nbexec/examples/example2_stream.sh" for _ in range(30)])
    pool.close()
    
    #run_process("~/nbexec/examples/list.sh")
