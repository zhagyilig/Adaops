# coding=utf-8
# auth: zhangyiling
# time: 2019-05-19 16:08
# description: 获取线上云主机信息，POST 到 CMDB.

import requests
import boto3
import json

server_info = """{
    'ip': '{}',
    'hostname': '{}',
    'cpu': '{}',
    'mem': '{}',
    'disk': '{}',
    'os': '{}',
    'manufacturer': 'dell',
    'model_name': 'ec2',
    'uuid': '{}
}""".format(ip, hostname, cpu, mem, disk, os, uuid)
