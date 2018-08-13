from __future__ import absolute_import
import os

from sentry.lang.native.minidump import merge_minidump_event


def test_minidump_linux():
    event = {'release': 'test-1.0.0'}
    minidump = os.path.join(os.path.dirname(__file__), 'fixtures', 'linux.dmp')
    merge_minidump_event(event, minidump)

    assert event == {
        'contexts': {
            'device': {
                'arch': 'x86_64'
            },
            'os': {
                'build': u'#1 SMP Mon Nov 6 16:00:12 UTC 2017',
                'name': u'Linux',
                'type': 'os',
                'version': u'4.9.60-linuxkit-aufs'
            }
        },
        'debug_meta': {
            'images': [
                {
                    'id': u'451a38b5-0679-79d2-0738-22a5ceb24c4b',
                    'image_addr': '0x7f514015d000',
                    'image_size': 1835008,
                    'name': u'/lib/x86_64-linux-gnu/libc-2.23.so',
                    'type': 'symbolic'
                },
                {
                    'id': u'59627b5d-2255-a375-c17b-d4c3fd05f5a6',
                    'image_addr': '0x7f5140cdc000',
                    'image_size': 155648,
                    'name': u'/lib/x86_64-linux-gnu/ld-2.23.so',
                    'type': 'symbolic'
                },
                {
                    'id': u'c0bcc3f1-9827-fe65-3058-404b2831d9e6',
                    'image_addr': '0x400000',
                    'image_size': 106496,
                    'name': u'/work/linux/build/crash',
                    'type': 'symbolic'
                }
            ]
        },
        'exception': {
            'mechanism': {
                'type': 'minidump',
                'handled': False
            },
            'stacktrace': {
                'frames': [
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x401dc0',
                        'package': u'/work/linux/build/crash'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x7f5140cdc000',
                        'package': None
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x400040',
                        'package': u'/work/linux/build/crash'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x7fff5aef1000',
                        'package': None
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x401de9',
                        'package': u'/work/linux/build/crash'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x401dc0',
                        'package': u'/work/linux/build/crash'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x414ca0',
                        'package': u'/work/linux/build/crash'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x401c70',
                        'package': u'/work/linux/build/crash'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x401dc0',
                        'package': u'/work/linux/build/crash'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x401c70',
                        'package': u'/work/linux/build/crash'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x7f514017d830',
                        'package': u'/lib/x86_64-linux-gnu/libc-2.23.so'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x414c30',
                        'package': u'/work/linux/build/crash'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x401ec0',
                        'package': u'/work/linux/build/crash'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x7f5140cebac6',
                        'package': u'/lib/x86_64-linux-gnu/ld-2.23.so'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x400000',
                        'package': None
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x7f51401e4800',
                        'package': u'/lib/x86_64-linux-gnu/libc-2.23.so'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x7f514025002e',
                        'package': u'/lib/x86_64-linux-gnu/libc-2.23.so'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x401d72',
                        'package': u'/work/linux/build/crash'
                    }
                ],
                'registers': {
                    u'r10': u'0x0000000000000131',
                    u'r11': u'0x00007f5140aca4c0',
                    u'r12': u'0x0000000000401dc0',
                    u'r13': u'0x00007fff5ae4ac90',
                    u'r14': u'0x00007fff5ae4aab0',
                    u'r15': u'0x0000000000000000',
                    u'r8': u'0x0000000000000000',
                    u'r9': u'0x0000000000000000',
                    u'rax': u'0xffffffffffffffff',
                    u'rbp': u'0x00007fff5ae4abb0',
                    u'rbx': u'0x00007fff5ae4aa20',
                    u'rcx': u'0x00007f5140521b20',
                    u'rdi': u'0x00007fff5ae4aab0',
                    u'rdx': u'0x00007f5140efc000',
                    u'rip': u'0x0000000000401d72',
                    u'rsi': u'0x0000000000000000',
                    u'rsp': u'0x00007fff5ae4aa20'
                }
            },
            'thread_id': 1304,
            'type': u'SIGSEGV',
            'value': u'Fatal Error: SIGSEGV'
        },
        'level': 'fatal',
        'message': u'Fatal Error: SIGSEGV',
        'platform': 'native',
        'release': 'test-1.0.0',
        'threads': [
            {
                'crashed': True,
                'id': 1304
            }
        ],
        'timestamp': 1522061032.0
    }


def test_minidump_macos():
    event = {'release': 'test-1.0.0'}
    minidump = os.path.join(os.path.dirname(__file__), 'fixtures', 'macos.dmp')
    merge_minidump_event(event, minidump)

    assert event == {
        'contexts': {
            'device': {
                'arch': 'x86_64'
            },
            'os': {
                'build': u'16G29',
                'name': 'macOS',
                'type': 'os',
                'version': u'10.12.6'
            }
        },
        'debug_meta': {
            'images': [
                {
                    'id': u'67e9247c-814e-392b-a027-dbde6748fcbf',
                    'image_addr': '0x109b9b000',
                    'image_size': 69632,
                    'name': u'/Users/travis/build/getsentry/breakpad-tools/macos/build/./crash',
                    'type': 'symbolic'
                },
                {
                    'id': u'9b2ac56d-107c-3541-a127-9094a751f2c9',
                    'image_addr': '0x7fffe7ee6000',
                    'image_size': 24576,
                    'name': u'/usr/lib/system/libdyld.dylib',
                    'type': 'symbolic'
                }
            ]
        },
        'exception': {
            'mechanism': {
                'type': 'minidump',
                'handled': False
            },
            'stacktrace': {
                'frames': [
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x7fffe7eeb235',
                        'package': u'/usr/lib/system/libdyld.dylib'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x7fffe7eeb235',
                        'package': u'/usr/lib/system/libdyld.dylib'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x109ba8c70',
                        'package': u'/Users/travis/build/getsentry/breakpad-tools/macos/build/./crash'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x109ba8c15',
                        'package': u'/Users/travis/build/getsentry/breakpad-tools/macos/build/./crash'
                    }
                ],
                'registers': {
                    u'r10': u'0x000000000000002e',
                    u'r11': u'0x00007fffe8105171',
                    u'r12': u'0x0000000000000000',
                    u'r13': u'0x0000000000000000',
                    u'r14': u'0x0000000000000000',
                    u'r15': u'0x0000000000000000',
                    u'r8': u'0x000000000c0008ff',
                    u'r9': u'0x0000000000000000',
                    u'rax': u'0x0000000000000001',
                    u'rbp': u'0x00007fff56064258',
                    u'rbx': u'0x00007fff56064120',
                    u'rcx': u'0x0000000000000000',
                    u'rdi': u'0x00007fff56064120',
                    u'rdx': u'0x0000000000000000',
                    u'rip': u'0x0000000109ba8c15',
                    u'rsi': u'0x00007fff56064140',
                    u'rsp': u'0x00007fff56064110'
                }
            },
            'thread_id': 775,
            'type': u'EXC_BAD_ACCESS / KERN_INVALID_ADDRESS',
            'value': u'Fatal Error: EXC_BAD_ACCESS / KERN_INVALID_ADDRESS'
        },
        'level': 'fatal',
        'message': u'Fatal Error: EXC_BAD_ACCESS / KERN_INVALID_ADDRESS',
        'platform': 'native',
        'release': 'test-1.0.0',
        'threads': [
            {
                'crashed': True,
                'id': 775
            }
        ],
        'timestamp': 1521713398.0
    }


def test_minidump_windows():
    event = {'release': 'test-1.0.0'}
    minidump = os.path.join(os.path.dirname(__file__), 'fixtures', 'windows.dmp')
    merge_minidump_event(event, minidump)

    assert event == {
        'contexts': {
            'device': {
                'arch': 'x86'
            },
            'os': {
                'build': u'',
                'name': 'Windows',
                'type': 'os',
                'version': u'10.0.14393'
            }
        },
        'debug_meta': {
            'images': [
                {
                    'id': u'3249d99d-0c40-4931-8610-f4e4fb0b6936-1',
                    'image_addr': '0x2a0000',
                    'image_size': 36864,
                    'name': u'C:\\projects\\breakpad-tools\\windows\\Release\\crash.exe',
                    'type': 'symbolic'
                },
                {
                    'id': u'971f98e5-ce60-41ff-b2d7-235bbeb34578-1',
                    'image_addr': '0x77170000',
                    'image_size': 1585152,
                    'name': u'C:\\Windows\\System32\\ntdll.dll',
                    'type': 'symbolic'
                },
                {
                    'id': u'ae131c67-27a7-4fa1-9916-b5a4aef41190-1',
                    'image_addr': '0x75810000',
                    'image_size': 790528,
                    'name': u'C:\\Windows\\System32\\rpcrt4.dll',
                    'type': 'symbolic'
                },
                {
                    'id': u'aec7ef2f-df4b-4642-a471-4c3e5fe8760a-1',
                    'image_addr': '0x70b70000',
                    'image_size': 151552,
                    'name': u'C:\\Windows\\System32\\dbgcore.dll',
                    'type': 'symbolic'
                },
                {
                    'id': u'd3474559-96f7-47d6-bf43-c176b2171e68-1',
                    'image_addr': '0x75050000',
                    'image_size': 917504,
                    'name': u'C:\\Windows\\System32\\kernel32.dll',
                    'type': 'symbolic'
                }
            ]
        },
        'exception': {
            'mechanism': {
                'type': 'minidump',
                'handled': False
            },
            'stacktrace': {
                'frames': [
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x771d0f44',
                        'package': u'C:\\Windows\\System32\\ntdll.dll'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x771d0f79',
                        'package': u'C:\\Windows\\System32\\ntdll.dll'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x750662c4',
                        'package': u'C:\\Windows\\System32\\kernel32.dll'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x2a2d97',
                        'package': u'C:\\projects\\breakpad-tools\\windows\\Release\\crash.exe'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x2a3435',
                        'package': u'C:\\projects\\breakpad-tools\\windows\\Release\\crash.exe'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x7584e9c0',
                        'package': u'C:\\Windows\\System32\\rpcrt4.dll'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x75810000',
                        'package': None
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x70b7ae40',
                        'package': u'C:\\Windows\\System32\\dbgcore.dll'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x70850000',
                        'package': None
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x7584e9c0',
                        'package': u'C:\\Windows\\System32\\rpcrt4.dll'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x2a28d0',
                        'package': u'C:\\projects\\breakpad-tools\\windows\\Release\\crash.exe'
                    },
                    {
                        'function': '<unknown>',
                        'instruction_addr': '0x2a2a3d',
                        'package': u'C:\\projects\\breakpad-tools\\windows\\Release\\crash.exe'
                    }
                ],
                'registers': {
                    u'eax': u'0x00000000',
                    u'ebp': u'0x010ff670',
                    u'ebx': u'0x00fe5000',
                    u'ecx': u'0x010ff670',
                    u'edi': u'0x013bfd78',
                    u'edx': u'0x00000007',
                    u'eflags': u'0x00010246',
                    u'eip': u'0x002a2a3d',
                    u'esi': u'0x759c6314',
                    u'esp': u'0x010ff644'
                }
            },
            'thread_id': 1636,
            'type': u'EXCEPTION_ACCESS_VIOLATION_WRITE',
            'value': u'Fatal Error: EXCEPTION_ACCESS_VIOLATION_WRITE'
        },
        'level': 'fatal',
        'message': u'Fatal Error: EXCEPTION_ACCESS_VIOLATION_WRITE',
        'platform': 'native',
        'release': 'test-1.0.0',
        'threads': [
            {
                'crashed': True,
                'id': 1636
            },
            {
                'crashed': False,
                'id': 3580,
                'stacktrace': {
                    'frames': [{
                        'function': '<unknown>',
                        'instruction_addr': '0x771d0f44',
                        'package': u'C:\\Windows\\System32\\ntdll.dll'
                    },
                        {
                        'function': '<unknown>',
                        'instruction_addr': '0x771d0f79',
                        'package': u'C:\\Windows\\System32\\ntdll.dll'
                    },
                        {
                        'function': '<unknown>',
                        'instruction_addr': '0x750662c4',
                        'package': u'C:\\Windows\\System32\\kernel32.dll'
                    },
                        {
                        'function': '<unknown>',
                        'instruction_addr': '0x771e016c',
                        'package': u'C:\\Windows\\System32\\ntdll.dll'
                    }],
                    'registers': {
                        u'eax': u'0x00000000',
                        u'ebp': u'0x0159faa4',
                        u'ebx': u'0x013b0990',
                        u'ecx': u'0x00000000',
                        u'edi': u'0x013b4af0',
                        u'edx': u'0x00000000',
                        u'eflags': u'0x00000216',
                        u'eip': u'0x771e016c',
                        u'esi': u'0x013b4930',
                        u'esp': u'0x0159f900'
                    }
                }
            },
            {
                'crashed': False,
                'id': 2600,
                'stacktrace': {
                    'frames': [{
                        'function': '<unknown>',
                        'instruction_addr': '0x771d0f44',
                        'package': u'C:\\Windows\\System32\\ntdll.dll'
                    },
                        {
                        'function': '<unknown>',
                        'instruction_addr': '0x771d0f79',
                        'package': u'C:\\Windows\\System32\\ntdll.dll'
                    },
                        {
                        'function': '<unknown>',
                        'instruction_addr': '0x750662c4',
                        'package': u'C:\\Windows\\System32\\kernel32.dll'
                    },
                        {
                        'function': '<unknown>',
                        'instruction_addr': '0x771e016c',
                        'package': u'C:\\Windows\\System32\\ntdll.dll'
                    }],
                    'registers': {
                        u'eax': u'0x00000000',
                        u'ebp': u'0x0169fb98',
                        u'ebx': u'0x013b0990',
                        u'ecx': u'0x00000000',
                        u'edi': u'0x013b7c28',
                        u'edx': u'0x00000000',
                        u'eflags': u'0x00000202',
                        u'eip': u'0x771e016c',
                        u'esi': u'0x013b7a68',
                        u'esp': u'0x0169f9f4'
                    }
                }
            },
            {
                'crashed': False,
                'id': 2920,
                'stacktrace': {
                    'frames': [{
                        'function': '<unknown>',
                        'instruction_addr': '0x771df3dc',
                        'package': u'C:\\Windows\\System32\\ntdll.dll'
                    }],
                    'registers': {
                        u'eax': u'0x00000000',
                        u'ebp': u'0x0179f2b8',
                        u'ebx': u'0x017b1aa0',
                        u'ecx': u'0x00000000',
                        u'edi': u'0x017b1a90',
                        u'edx': u'0x00000000',
                        u'eflags': u'0x00000206',
                        u'eip': u'0x771df3dc',
                        u'esi': u'0x000002cc',
                        u'esp': u'0x0179f2ac'
                    }
                }
            }
        ],
        'timestamp': 1521713273.0
    }
