# -*- encoding=utf8 -*-
__author__ = "lwintermelon"

from airtest.core.api import *
from airtest.core.error import TargetNotFoundError

ST.OPDELAY = 0.4
auto_setup(__file__)
count = 0

def try_touch(v):
    auto_setup(__file__)
    coor = exists(v)
    if coor:
        touch(coor)
    return coor

def click_corner():
    auto_setup(__file__)
    touch([1582, 889])
    touch([1566, 884])

def hs_clear():
    auto_setup(__file__)
    try_touch(Template(r"T取消.png", record_pos=(-0.072, 0.044), resolution=(1600, 900)))
    click_corner()

def dig_from_bag():
    auto_setup(__file__)
    hs_clear()
    
    try_touch(Template(r"P背包.png", threshold=0.5, rgb=False, record_pos=(0.474, 0.191), resolution=(1600, 900)))

    try_touch(Template(r"P藏宝图.png", record_pos=(0.098, -0.118), resolution=(1600, 900)))
    try_touch(Template(r"T使用.png", record_pos=(0.179, 0.166), resolution=(1600, 900)))

    sleep(0.8)

def sell_equip():
    auto_setup(__file__)
#     seventy=Template(r"T70.png", threshold=0.87, rgb=True, target_pos=9, record_pos=(0.139, -0.072), resolution=(1600, 900)) 
    eighty=Template(r"T80.png", threshold=0.84, rgb=False, target_pos=9, record_pos=(0.139, -0.07), resolution=(1600, 900)) # 卖80级的装备
    tml = eighty


    while True:
        coor = exists(tml)
        if coor == False:
            break

        touch(coor)
        try_touch(Template(r"T更多.png", record_pos=(0.061, 0.002), resolution=(1600, 900)))

        try_touch(Template(r"T出售.png", record_pos=(0.061, -0.034), resolution=(1600, 900)))

        try_touch(Template(r"T确认.png", threshold=0.8, rgb=True, record_pos=(0.069, 0.043), resolution=(1600, 900)))
        sleep(0.9)

def combine_jewelry():
    auto_setup(__file__)
    hs_clear()
    try_touch(Template(r"P展开.png", threshold=0.4, rgb=False, record_pos=(0.471, 0.246), resolution=(1600, 900)))
    try_touch(Template(r"P打造.png", threshold=0.5, record_pos=(0.369, 0.247), resolution=(1600, 900)))
    try_touch(Template(r"P首饰.png", threshold=0.5, record_pos=(0.367, 0.083), resolution=(1600, 900)))

    sleep(2)
    touch([409, 175])  # 玉佩

    touch([409, 238])
    for i in range(8):
        touch([1119, 751])
    touch([430, 306])
    for i in range(5):
        touch([1119, 751])
    touch([430, 375])
    for i in range(5):
        touch([1119, 751])
    touch([417, 436])
    for i in range(5):
        touch([1119, 751])
    touch([409, 175])

    touch([423, 242])  # 项链

    touch([409, 317])
    for i in range(8):
        touch([1119, 751])
    touch([430, 375])
    for i in range(5):
        touch([1119, 751])
    touch([430, 448])
    for i in range(5):
        touch([1119, 751])
    touch([417, 507])
    for i in range(5):
        touch([1119, 751])
    touch([409, 243])

    touch([423, 319])  # 手镯

    touch([409, 391])
    for i in range(8):
        touch([1119, 751])
    touch([430, 467])
    for i in range(5):
        touch([1119, 751])
    touch([430, 524])
    for i in range(5):
        touch([1119, 751])
    touch([417, 591])
    for i in range(5):
        touch([1119, 751])

    click_corner()

def abandon_task():
    auto_setup(__file__)
    hs_clear()
    try_touch(Template(r"T任务.png", record_pos=(0.388, -0.193), resolution=(1600.0, 900.0)))
    try_touch(Template(r"T超级宝藏.png", record_pos=(-0.245, -0.161), resolution=(1600.0, 900.0)))
    try_touch(Template(r"T放弃.png", record_pos=(0.109, 0.192), resolution=(1600, 900)))
    try_touch(Template(r"T确认.png", threshold=0.8, rgb=True, record_pos=(0.069, 0.043), resolution=(1600, 900)))
    click_corner()

def auto_sell_equip():
    auto_setup(__file__)
    hs_clear()
    touch([1560, 752])  # 背包
    sleep(1.2)
    touch([1191, 748])  # 整理
    mylists = [[861, 187], [958, 201], [1059, 199],[1128, 193], [1221, 193]]  # 5个背包栏
    for coor in mylists:
        touch(coor)
        sell_equip()
        sleep(0.8)
    touch([873, 197])  # 回到第一个背包栏
    sleep(2.0)
    touch([1191, 748])  # 整理
    hs_clear()

def auto_wabao():

    global count

    auto_setup(__file__)
    
    dig_from_bag()

    try_touch(Template(r"T确认.png", threshold=0.8, rgb=True, record_pos=(0.069, 0.043), resolution=(1600, 900)))

    while True:
        sleep(8)
        try:
            coor = wait(Template(r"T确认.png", threshold=0.8, rgb=True, record_pos=(0.069, 0.043), resolution=(1600, 900)), timeout=6, interval=3)
        except Exception:
            abandon_task()
            return

        touch(coor)
        try_touch(Template(r"T确认.png", threshold=0.8, rgb=True, record_pos=(0.069, 0.043), resolution=(1600, 900)))
        count += 1
        if count % 80 == 0:
            sleep(9)

            combine_jewelry()
            auto_sell_equip()
            count = 0

try_touch(Template(r"T取消.png", record_pos=(-0.072, 0.044), resolution=(1600, 900)))
# sell_equip()
# auto_sell_equip()
# combine_jewelry()

while True:
    auto_wabao()
