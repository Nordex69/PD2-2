partitions = [
    "System;/;50000;85",
    "Data;/home;150000;40",
    "Cache;/tmp;5000;10",
    "Backup;/mnt/backup;500000;92",
    "USB-Drive;/media/usb;16000;0",
    "Logs;/var/log;10000;95",
    "Database;/var/lib/mysql;80000;70",
    "Shared;/mnt/shared;200000;1",
    "Win-System;/mnt/win;100000;90",
    "Recovery;/recovery;2000;98"
]
for p in partitions:
    data = p.split(";")
    label = data[0]
    used_pct = int(data[3])
    if used_pct >= 90:
        print(f"UZMANIBU: {label} disks ir pilns")