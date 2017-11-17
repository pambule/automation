# nedd to set the location of ipmitool in sysytem emvironmental variables
from fabric.operations import local
import os


def funct1(cmd):
    result = local(cmd, capture=True)
    return result

def funct3(r):
    stringone = ''
    for t in r.split():
        stringone = stringone + t
    str1 = stringone.decode("hex")
    #return ''.join(ch for ch in str1 if ch.isalnum())
    return str1

if __name__ == '__main__':
    attr_cmd = {}
    attr_res = {}
    cmd = "ipmitool.exe -I lanplus -H 100.100.226.176 -U root -P dell_123 raw 0x06 0x59 0x00 0xd1 0x00 0x00"
    cmd="ipmitool.exe -I wmi raw 0x06 0x37"
    #cmd = "ipmitool.exe -I lanplus -H 100.100.226.176 -U root -P dell_123 raw 0x06 0x01"    
    attr_cmd = {"System GUID": cmd}
    # funct1(cmd)
    # funct2()
    r = ''
    for att, key in attr_cmd.iteritems():
        r = str(funct1(cmd))
        resp = r
        if "raw" in cmd:
            resp = funct3(r)
        attr_res[att] = resp
    print attr_res
    # print type(r)
