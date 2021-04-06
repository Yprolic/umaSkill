import aiohttp
import asyncio
from argparse import ArgumentParser
import errno
import os
import timeit
import tqdm
import shutil
import sys
from datetime import datetime

META_PATH = 'db/meta'
CSV_STR = '%Y%m%d.csv'

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def merge_path_dir(path: str) -> str:
    new_dir = os.path.dirname(path).replace('/', '.')
    return os.path.join(new_dir, os.path.basename(path))

def check_target_path(target: str):
    if not os.path.exists(os.path.dirname(target)):
        try:
            os.makedirs(os.path.dirname(target))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

async def download(session, source: str, target: str, http_proxy: str):
    if os.path.exists(target): # Empty file will not be redownload if timeout
        return
    async with session.get(source, proxy = http_proxy) as resp:
        if resp.status != 200:
            print(source)
        assert resp.status == 200
        check_target_path(target)
        with open(target, 'wb') as f:
            f.write(await resp.read())
            f.close()

def read_csv_data(path: str, folder_name: str, filter_str: str) -> set:
    download_set = set()
    with open(path, 'r') as f:
        for l in f:
            sp = l.split(',')
            if sp[0].strip() == '' or sp[1].strip() == '' or not sp[1].startswith('h'):
                continue
            mtuple = '%s/%s' % (folder_name, merge_path_dir(sp[0].strip())), sp[1].strip()
            download_set.add(mtuple)
    return download_set
    
def gen_download_list(new_csv: str, old_csv: str, folder_name: str, filter_str: str) -> set:
    new_set = read_csv_data(new_csv, folder_name, filter_str)
    if old_csv is None:
        return new_set
    return new_set - read_csv_data(old_csv, folder_name, filter_str)

async def main(new_csv: str, old_csv: str, folder_name: str, filter_str: str, http_proxy: str):
    download_set = gen_download_list(new_csv, old_csv, folder_name, filter_str)
    async with aiohttp.ClientSession() as session:     
        tasks = [
            download(session, source, target, http_proxy)
            for target, source in download_set] 
        for f in tqdm.tqdm(asyncio.as_completed(tasks), total=len(tasks), desc='Download progress'):
            await f

if __name__ == '__main__':
    #--Default--
    date_list = list(map(lambda x : datetime.strptime(x, CSV_STR), os.listdir(META_PATH)))
    date_list.sort()
    new = old = None
    if len(date_list) > 1:
        old = os.path.join(META_PATH, date_list[-2].strftime(CSV_STR))
    if len(date_list) > 0:
        new = os.path.join(META_PATH, date_list[-1].strftime(CSV_STR))
    folder_name = 'data'
    filter_str = None
    http_proxy = 'http://127.0.0.1:10809' # Change this
    #--Default--
    
    parser = ArgumentParser(description='Diff between versions and download the assets.')
    parser.add_argument('-n', type=str, help='Newer meta csv', default=new)
    parser.add_argument('-o', type=str, help='Older meta csv', default=old)
    parser.add_argument('-d', type=str, help='Download location', default=folder_name)
    parser.add_argument('-f', type=str, help='Filter string (Case sensitive)', default=filter_str)
    parser.add_argument('-p', type=str, help='Http Proxy (proxy link/None)', default=http_proxy)
    args = parser.parse_args()

    start = timeit.default_timer()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args.n, args.o, args.d, args.f, args.p))
    end = timeit.default_timer()

    print('Time spent: ' + str(end-start) + ' second.')
    
