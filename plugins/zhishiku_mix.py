from plugins.common import settings
from plugins.common import error_print 
zsk=[]
input_list = settings.library.mix.strategy.split(" ")
for item in input_list:
    item=item.split(":")
    from importlib import import_module
    zhishiku = import_module('plugins.zhishiku_'+item[0])
    if zhishiku is None:
        error_print("载入知识库失败",item[0])
    if item[0] == "rtst" and len(item) > 2:
        zsk.append({'zsk': zhishiku, "count": int(item[1]), "rtst_mem_name": item[2]})
    else:
        zsk.append({'zsk': zhishiku, "count": int(item[1])})
def find(s,step = 0):
    result=[]
    for item in zsk:
        result+=item['zsk'].find(s,step)[:item['count']]
    for item in zsk:
        if "rtst_mem_name" in item:
            result += item['zsk'].find(s, step, item['rtst_mem_name'])[:item['count']]
        else:
            result += item['zsk'].find(s, step)[:item['count']]
    return result[:int(settings.library.mix.count)]

