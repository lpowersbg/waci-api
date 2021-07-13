import socket

host = '10.51.201.100'
port = 1000
on = b'<T0000681001000079>'
off = b'<T0000681000000078>'
status = b'<T0000681100000079>'
son = b'<F000068110100007a>'
soff = b'<F0000681100000079>'
goff = b'<F0000681000000078>'

def comms(comm):
    ven = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ven.sendto(comm, (host, port))
    return ven.recvfrom(1024)[0]

def venusoff():
    ven = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if comms(status) == son:
        comms(off)
    ven.close()

def venuson():
    ven = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if comms(status) == soff:
        comms(on)
    ven.close()

def venusres():
    ven = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if comms(status) == son:
        if comms(off) == goff:
            reply = comms(status)
            while reply != soff:
                reply = comms(status)
            comms(on)
    ven.close()