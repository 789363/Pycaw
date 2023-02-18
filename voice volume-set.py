# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:41:31 2023

@author: Yuwei
"""
import pycaw

def get_audio_status():
    sessions = pycaw.utils.AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(pycaw.utils.IAudioMeterInformation).GetPeakValue()
        if volume > 0:
            return "Music is playing, volume:", volume
    return "Music is not playing."

print(get_audio_status())