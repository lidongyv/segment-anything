# %%
import wget
import os
from tqdm import tqdm
import requests
f = open(r'D:\SAM\segment-anything\file_list.txt','r')
files = f.readlines()
f.close()
files = files[1:]
files.sort()
def download(url: str, fname: str):
    # 用流stream的方式获取url的数据
    resp = requests.get(url, stream=True)
    # 拿到文件的长度，并把total初始化为0
    total = int(resp.headers.get('content-length', 0))
    # 打开当前目录的fname文件(名字你来传入)
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
# %%
save_path = r'D:\SAM'
f = open(r'D:\SAM\segment-anything\downloaded_files.txt','r')
downloaded_files = f.readlines()
f.close()
downloaded_files = [i.split('\n')[0] for i in downloaded_files]
print('downloaded file ', len(downloaded_files), ': ' ,downloaded_files)
for file in tqdm(files):
    file_name = file.split('\t')[0]
    download_path = file.split('\t')[1].split('\n')[0]
    if file_name not in downloaded_files:
        print(file_name, downloaded_files)
        download(download_path, file_name)
        # wget.download(download_path, out=os.path.join(save_path, file_name))
        f = open(r'D:\SAM\segment-anything\downloaded_files.txt','a')
        f.write(file_name+'\n')
        f.flush()
        f.close()
# %%

