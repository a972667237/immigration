#coding: utf-8
from uuid import uuid4
from datetime import datetime
def upload_video_cover(instance,filename):
    ext = filename.split('.')[-1] #日期目录和 随机文件名
    filename = '{}.{}'.format(uuid4().hex, ext)
    year = datetime.now().year
    month =datetime.now().month
    day = datetime.now().day #instance 可使用instance.user.id
    return "./{0}/{1}/{2}/{3}".format(year,month,day,filename)