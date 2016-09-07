#!/usr/bin/env python
# coding=utf-8
import urllib2
import json as JSON

if __name__ == '__main__':
    rsp = urllib2.urlopen('http://consul.jinyuen.com/v1/health/state/critical')
    content = rsp.read()
    result = JSON.loads(content)
    for data in result:
        service = data.get('ServiceID')
        if service[-6:] == 'server': # 是个service
            pass # TODO: restart

    path = '/data/test.txt'
    with open(path, 'wb') as f:
        f.write(content)
