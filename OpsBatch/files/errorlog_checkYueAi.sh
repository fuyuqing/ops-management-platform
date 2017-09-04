#!/bin/bash

dir="/mnt/logs/yueai-server/error"
logfile="error.$(date  +%Y%m%d).log"
cd $dir
if [[ -e ${logfile} ]]; then
    line_num=`wc -l ${logfile}|awk '{print $1}'` 
    curline=`tail -n 1 /tmp/zabbix/cache_YueAi.txt`
    if [[ ${line_num} -eq 0 ]]; then
        pass
    elif [[ ${line_num} -eq ${curline} ]]; then
        pass
    else
        echo $line_num >> /tmp/zabbix/cache_YueAi.txt
    fi
fi
