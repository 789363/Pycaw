# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:46 2023

@author: Yuwei
"""

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# 判断是否静音，mute为1代表是静音，为0代表不是静音
mute = volume.GetMute()
if mute == 1:
    print('当前是静音状态')
else:
    print('当前是非静音状态')

# 获取音量值，0.0代表最大，-65.25代表最小
vl = volume.GetMasterVolumeLevel()
print('当前音量值为%s' % vl)