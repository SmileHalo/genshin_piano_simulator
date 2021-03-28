#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   main.py    
@Contact :   hookhook@foxmail.com
@Desc    :   
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/27 20:38   yang      1.0         None
"""
import time
import mido
import win32api
import win32con
from multiprocessing import Process

note_to_keyboard = {
    'E1': 'C',
    'F1': 'V',
    'G1': 'B',
    'A1': 'N',
    'B1': 'M',
    'C2': 'A',
    'D2': 'S',
    'E2': 'D',
    'F2': 'F',
    'G2': 'G',
    'A2': 'H',
    'B2': 'J',
    'C3': 'Q',
    'D3': 'W',
    'E3': 'E',
    'F3': 'R',
    'G3': 'T',
    'A3': 'Y',
    'B3': 'U',
    # 'C4': 'Q', #  Unsupported on genshin
    # 'D4': 'W',
    # 'E4': 'E',
    # 'F4': 'R',
    # 'G4': 'T',
    # 'A4': 'Y',
    # 'B4': 'U',
    # 'C5': 'I',
    # 'D5': 'O',
    # 'E5': 'P',
    # 'F5': '[',
    # 'G5': ']',
    # 'A5': '\\',
    # 'B5': '`',
    # 'C6': '1',
}
DEFAULT_TEMPO = 0.4
DEFAULT_OFFSET = -24  # down 2 key for every note
VK_CODE = {
    'backspace': 0x08,
    'tab': 0x09,
    'clear': 0x0C,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'caps_lock': 0x14,
    'esc': 0x1B,
    'spacebar': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'select': 0x29,
    'print': 0x2A,
    'execute': 0x2B,
    'print_screen': 0x2C,
    'ins': 0x2D,
    'del': 0x2E,
    'help': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'A': 0x41,
    'B': 0x42,
    'C': 0x43,
    'D': 0x44,
    'E': 0x45,
    'F': 0x46,
    'G': 0x47,
    'H': 0x48,
    'I': 0x49,
    'J': 0x4A,
    'K': 0x4B,
    'L': 0x4C,
    'M': 0x4D,
    'N': 0x4E,
    'O': 0x4F,
    'P': 0x50,
    'Q': 0x51,
    'R': 0x52,
    'S': 0x53,
    'T': 0x54,
    'U': 0x55,
    'V': 0x56,
    'W': 0x57,
    'X': 0x58,
    'Y': 0x59,
    'Z': 0x5A,
    'numpad_0': 0x60,
    'numpad_1': 0x61,
    'numpad_2': 0x62,
    'numpad_3': 0x63,
    'numpad_4': 0x64,
    'numpad_5': 0x65,
    'numpad_6': 0x66,
    'numpad_7': 0x67,
    'numpad_8': 0x68,
    'numpad_9': 0x69,
    'multiply_key': 0x6A,
    'add_key': 0x6B,
    'separator_key': 0x6C,
    'subtract_key': 0x6D,
    'decimal_key': 0x6E,
    'divide_key': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'F13': 0x7C,
    'F14': 0x7D,
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F18': 0x81,
    'F19': 0x82,
    'F20': 0x83,
    'F21': 0x84,
    'F22': 0x85,
    'F23': 0x86,
    'F24': 0x87,
    'num_lock': 0x90,
    'scroll_lock': 0x91,
    'left_shift': 0xA0,
    'right_shift ': 0xA1,
    'left_control': 0xA2,
    'right_control': 0xA3,
    'left_menu': 0xA4,
    'right_menu': 0xA5,
    'browser_back': 0xA6,
    'browser_forward': 0xA7,
    'browser_refresh': 0xA8,
    'browser_stop': 0xA9,
    'browser_search': 0xAA,
    'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC,
    'volume_mute': 0xAD,
    'volume_Down': 0xAE,
    'volume_up': 0xAF,
    'next_track': 0xB0,
    'previous_track': 0xB1,
    'stop_media': 0xB2,
    'play/pause_media': 0xB3,
    'start_mail': 0xB4,
    'select_media': 0xB5,
    'start_application_1': 0xB6,
    'start_application_2': 0xB7,
    'attn_key': 0xF6,
    'crsel_key': 0xF7,
    'exsel_key': 0xF8,
    'play_key': 0xFA,
    'zoom_key': 0xFB,
    'clear_key': 0xFE,
    '+': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    ';': 0xBA,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE,
    '`': 0xC0
}


def create_note_dict():
    """
        note table from note to note_name
    :return:
    """

    index = 'ABCDEFG'
    ret = {}
    tmp1 = 0
    last_note_name = 'G'
    skipped = 0
    for i in range(20, 109):
        if last_note_name in 'ACDFG' and skipped == 0:
            skipped = 1
            continue
        skipped = 0
        last_note_name = index[tmp1 % len(index)]
        ret[i] = '{}{}'.format(last_note_name, i // 12 - 1)
        tmp1 += 1
    return ret


def conv_note_name(note):
    if note in note_to_note_name:
        return note_to_note_name[note]
    else:
        # print('note {} down'.format(note))
        return note_to_note_name[note - 1]  # 处理不了的黑键给它降tmd半个音


note_to_note_name = create_note_dict()


def ticks2s(ticks, tempo, ticks_per_beat):
    return ticks / ticks_per_beat * tempo


def handle_all_tracks(tracks, ticks_per_beat, tempo=DEFAULT_TEMPO):
    notes = {}
    all_tracks = []
    pressed_keys = set()
    for i, track in enumerate(tracks):
        ret_track = []
        total_time = 0
        for message in track:
            t = ticks2s(message.time, tempo, ticks_per_beat)
            total_time += t
            if isinstance(message, mido.MetaMessage):
                if message.type == "set_tempo":
                    tempo = message.tempo / 10 ** 6
                elif message.type == "end_of_track":
                    pass
                else:
                    print("Unsupported metamessage: " + str(message))

            else:  # Note
                if (message.type == "program_change" or message.type == "control_change") and \
                        message.time != 0 and len(pressed_keys) != 0:
                    ret_track += [(t, None, 0)]
                    pass
                elif message.type == "note_on" or message.type == "note_off":
                    if message.note not in notes:
                        notes[message.note] = 0
                    if message.type == "note_on" and message.velocity != 0:
                        notes[message.note] += 1
                        if notes[message.note] == 1:
                            ret_track += \
                                [(t, message.note, message.velocity)]
                            pressed_keys.add(message.note)
                    else:
                        notes[message.note] -= 1
                        if notes[message.note] == 0:
                            if message.type == "note_off":
                                ret_track += [(t, message.note, 0)]
                            else:
                                ret_track += [(t, message.note, message.velocity)]
                            pressed_keys.add(message.note)
                else:
                    pass
                    # print(message)
        all_tracks.append(ret_track)
        print("total time: " + str(total_time) + "s")
    return all_tracks


def note_down(note):
    print('note {} down'.format(note))
    return note - 1


def resize_note(note):
    if int(note[1]) < 2 and note[0] in 'CD':
        tmp = '2'
    elif int(note[1]) > 3:
        tmp = '3'
    else:
        tmp = '1'
    if tmp is None:
        print('note {} cannot resize!'.format(note))
        raise ValueError
    print('{} resized '.format(note))
    return '{}{}'.format(note[0], tmp)


def play(every_track):
    for t, note, velocity in every_track:
        if t:
            time.sleep(t)
        if note:
            note += DEFAULT_OFFSET
            if note not in range(20, 109):
                continue
            tmp_note = note_to_note_name[note] if note in note_to_note_name else note_to_note_name[note_down(note)]
            if tmp_note not in note_to_keyboard:
                # continue
                tmp_note = resize_note(tmp_note)
            if velocity != 0:
                # print('press {} {}'.format(tmp_note, t))
                win32api.keybd_event(VK_CODE[note_to_keyboard[tmp_note]], 0, 0, 0)  # enter
            else:
                # print('release {}'.format(tmp_note))
                win32api.keybd_event(VK_CODE[note_to_keyboard[tmp_note]], 0, win32con.KEYEVENTF_KEYUP, 0)  # release


if __name__ == '__main__':
    music = mido.MidiFile(r'midi_files\canon.mid', clip=True, debug=True)
    all_notes_name = []
    # walk every note
    all_notes = set()
    for track in music.tracks:
        for v in track:
            if isinstance(v, mido.Message) and v.type == 'note_on':
                all_notes.add(v.note)
    for each in list(all_notes):
        all_notes_name.append(conv_note_name(each))

    merge_track = handle_all_tracks(music.tracks, music.ticks_per_beat)
    time.sleep(2)  # to switch window manually

    processlist = []
    for each in merge_track:
        processlist.append(Process(target=play, args=(each,)))
    for each in processlist:
        each.start()
    input('done')
