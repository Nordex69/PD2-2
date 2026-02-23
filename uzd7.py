partitions = [
    "System;/;50000;85",
    "Data;/home; 150000;40",
    "Cache;/tmp; 5000;10",
    "Backup;/mnt/backup; 500000;92",
    "USB-Drive;/media/usb;16000;0",
    "Logs;/var/log;10000;95",
    "Database;/var/lib/mysql;80000;70",
    "Shared;/mnt/shared; 200000;15",
    "Win-System;/mnt/win;100000;90",
    "Recovery;/recovery; 2000;98"
]

def get_used_space(plist):
    res = []
    for p in plist:
        d = p.split(";")
        mb = int(int(d[2]) * (int(d[3]) / 100))
        res.append({"Label": d[0], "UsedMB": mb})
    return res

print(get_used_space(partitions))