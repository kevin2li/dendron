# %%
import os
import glob
from pathlib import Path
import os.path as osp
import shutil
import re
import yaml
from datetime import datetime
import traceback
from pprint import pprint

def insert_metadata(src_path: str, dst_path:str, type="file"):
    if osp.exists(src_path) and osp.isfile(src_path):
        try:
            with open(src_path, "r", encoding="utf-8") as f:
                data = f.readlines()
            pattern = '---\n'
            start = data.index(pattern)
            end = start+data[start+1:].index(pattern)+1
            frontmatter = data[start+1: end]
            content = data[end+1:]
            
            frontmatter = yaml.safe_load("".join(frontmatter))
            # 添加category
            p = Path(src_path)
            parts = p.name.split(".")
            category = parts[0]
            frontmatter["category"] = category
            
            # 添加date
            t = datetime.fromtimestamp(frontmatter['created']/1000.)
            date = datetime.strftime(t, "%Y-%m-%d %H:%M:%S")
            frontmatter["date"] = date
            
            new_frontmatter = yaml.safe_dump(frontmatter, encoding="utf-8", allow_unicode=True).decode("utf-8")
            
            # 目录页
            if type!="file":
                content.append("<AutoCatalog />")
                return
            with open(dst_path, "w", encoding="utf-8") as f:
                f.writelines([pattern, new_frontmatter, pattern, *content])
        except:
            print(new_frontmatter)
            traceback.print_exc()
    else:
        print("\033[1;31m",f"'{src_path}' does not exist","\033[0m")

target_dir = Path(r"C:\Users\kevin\Dendron\.vuepress\src")
keep_list = [
    ".vuepress",
    "README.md",
]

# 清理目标文件夹
# out = os.listdir(target_dir)
# for item in out:
#     if not (item in keep_list):
#         path = osp.join(target_dir, item)
#         if osp.isdir(item):
#             shutil.rmtree(path)
#         else:
#             os.remove(path)

# 按类型分组拷贝到目标文件夹
md_list = glob.glob(osp.join(osp.abspath("."), "*.md"))
dir_dict = {k: False for k in md_list}
for path in md_list:
    p = Path(path)
    parts = p.stem.split(".")
    if len(parts) == 1:
        dir_dict[path] = True
        continue
    parent = str(p.parent / f'{".".join(parts[:-1])}.md')
    if parent in dir_dict:
        dir_dict[parent] = True

for path in md_list:
    p = Path(path)
    parts = p.name.split(".")
    if dir_dict[path]: # 是目录
        dst_dir = (target_dir / "/".join(parts[:-1]))
        dst_dir.mkdir(exist_ok=True, parents=True)
        dst_path = dst_dir / "README.md"
        insert_metadata(path, dst_path, type='dir')
    else: # 是文件
        dst_dir = (target_dir / "/".join(parts[:-2]))
        dst_dir.mkdir(exist_ok=True, parents=True)
        dst_path = dst_dir / ".".join(parts[-2:])
        insert_metadata(path, dst_path)