import json
import re
#黑镜键值在这--------->  ^mirror.*?$

while True:
    input_text=input('请利用正则表达式输入待测键值:'+'\n')
    try:
        pattern = re.compile(input_text)
        break
    except:
        print("正则表达式无效 请重试")

#此处引用了M.py的代码

old_version = {}
with open("en_us.lang", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # 跳过空行和注释行
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            old_version[key.strip()] = value.strip()

#保存1.20.1版本文本
with open (r'en_us.json','r')as f:
    latest_version=json.load(f)
#获取1.20.1版本 黑镜文本的所有键值
key_list=list(latest_version.keys())
latest_blackmirror_key=[]
for key in key_list:
    result=pattern.findall(key)
    if result:
        latest_blackmirror_key.append(key)
#进行核对
IF_ALL_KEYS_CORRECT=None
for key in latest_blackmirror_key:
    text=latest_version[key]
    if text in old_version.values():
        print(f'{key} 所对应文本正确')
        IF_ALL_KEYS_CORRECT=1
    else:
        print(f'错误: {key} 所对应文本错误')
        IF_ALL_KEYS_CORRECT=0
if IF_ALL_KEYS_CORRECT:
    print('所有结果均正确')
else:
    print('请检查 文本中出现匹配错误或\n1.20.1版本中不含此键值')
