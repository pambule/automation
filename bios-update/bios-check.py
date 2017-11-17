import os
import re


def SysInfo():
    values = {}
    cache = os.popen2("SYSTEMINFO")
    source = cache[1].read()
    #sysOpts = ["Host Name", "OS Name", "OS Version", "Product ID", "System Manufacturer", "System Model", "System type", "BIOS Version", "Domain", "Windows Directory", "Total Physical Memory", "Available Physical Memory", "Logon Server"]
    sysOpts = ["System Model", "BIOS Version"]

    for opt in sysOpts:
        values[opt] = [item.strip() for item in re.findall(
            "%s:\w*(.*?)\n" % (opt), source, re.IGNORECASE)][0]
    return values


if __name__ == "__main__":
    """resp = SysInfo()
    model = resp["System Model"]
    bios = resp["BIOS Version"]"""
    model = "Latitude E5470"
    bios = "Dell Inc. 1.7.3, 6/15/2016"
    bios_ver = bios.split(",")[0][-5:]
    #os.chdir(os.getcwd() + "\\" + model)
    exee = os.listdir("."+"\\"+model)
    one = '@echo off\n' + 'set LOG=\"' + os.getcwd() + "\\PE2600.log\"\n" + 'set PKG=\"' + os.getcwd() + "\\" + model + "\\"+str(exee[0])+"\""
    batstring = one + '''
    echo Executing %PKG% >>%LOG%
    %PKG% /s /l=%LOG%
    set ExitCode=%ErrorLevel%
    if %ExitCode% EQU 0 echo Result: SUCCESSFUL >>%LOG%
    if %ExitCode% EQU 1 echo Result: UNSUCCESSFUL >>%LOG%
    if %ExitCode% EQU 2 echo Result: REBOOT_REQUIRED >>%LOG%
    if %ExitCode% EQU 3 echo Result: DEP_SOFT_ERROR >>%LOG%
    if %ExitCode% EQU 4 echo Result: DEP_HARD_ERROR >>%LOG%
    if %ExitCode% EQU 5 echo Result: QUAL_HARD_ERROR >>%LOG%
    if %ExitCode% EQU 6 echo Result: REBOOTING_SYSTEM >>%LOG%'''
    with open(os.getcwd() + r"\\update.bat","r+") as openfile:
        openfile.write(batstring)
    #os.system(os.getcwd() + r"\\update.bat")
        
