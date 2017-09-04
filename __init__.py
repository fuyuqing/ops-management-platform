#(:_*_coding:utf-8_*_:)

import salt.client
import salt.config
import json

local = salt.client.LocalClient()
passwd_list = local.cmd('fuyuqing-server','cmd.run','cat /etc/passwd')['fuyuqing-server'].split('\n')
master_opts = salt.config.master_config('/etc/salt/master')
minion_opts = salt.config.minion_config('/etc/salt/minion')

'''
local.cmd('*', ['grains.items','sys.doc','cmd.run',],[[],[],['uptime'],]) # multi functions and multi args
'''

if __name__ == '__main__':
    print json.dumps(master_opts,indent=3)
    print json.dumps(minion_opts,indent=3)
    print passwd_list

