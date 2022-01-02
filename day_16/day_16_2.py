from math import prod

with open('input.txt', 'r') as f:
    bits_code = f.read().strip()
#bits_code = 'C200B40A82'
#bits_code = '04005AC33890'
#bits_code = '880086C3E88112'
#bits_code = 'CE00C43D881120'
#bits_code = 'D8005AC2A8F0'
#bits_code = 'F600BC2D8F'
#bits_code = '9C005AC2F8F0'
#bits_code = '9C0141080250320F1802104A08'
bits_code = ''.join([f"{int(hex_, 16):0{4}b}" for hex_ in bits_code])

def parse_header(packet):
    version, opcode = '', ''
    iterator = iter([c for c in packet])
    # read version, opcode, and length type id from header
    for _ in range(3):
        version += next(iterator)
    for _ in range(3):
        opcode += next(iterator)
    if opcode == '100': # if literal, no length type id or length
        return (version, opcode, None, None)
    length_type_id = int(next(iterator))
    # read length depending on length type id
    length = ''
    for _ in range(11 if length_type_id else 15):
        length += next(iterator)
    length = int(length, 2)
    return (version, opcode, length_type_id, length)

def parse_literal(data):
    iterator = iter([c for c in data])
    for _ in range(6):
        next(iterator)
    not_last, literal = 1, ''
    while not_last:
        not_last = int(next(iterator))
        for _ in range(4):
            literal += next(iterator)
        return int(literal, 2)

def get_packet_length(data):
    version, opcode, length_type_id, length = parse_header(data)
    if length_type_id == 1: # number of packets
        length_sum = 18
        data = data[18:]
        for packet in range(length):
            subpacket_length = get_packet_length(data)
            length_sum += subpacket_length
            data = data[subpacket_length:]
            #data = [7 + (11 if self.length_type_id else 15):]
        return length_sum
    elif length_type_id == 0: # number of bits
        return 22 + length
    else: # literal
        iterator = iter(enumerate(data))
        for _ in range(6):
            next(iterator)
        not_last = 1
        while int(not_last):
            index, not_last = next(iterator)
            for _ in range(4):
                next(iterator)
        return index + 4 + 1
        
class Packet:
    def __init__(self, data):
        self.version, self.opcode, self.length_type_id, self.length = parse_header(data)
        self.subpackets = []
        self.literal = None
        if self.opcode == '100': # literal
            self.literal = parse_literal(data)
            return
        data = data[18 if self.length_type_id else 22:]
        if self.length_type_id == 1: # number of packets
            for _ in range(self.length):
                subpacket_length = get_packet_length(data)
                self.subpackets.append(Packet(data[:subpacket_length]))
                data = data[subpacket_length:]
        elif self.length_type_id == 0: # number of bits
            while len(data) > 10: # minimum size of meaningful packet
                subpacket_length = get_packet_length(data)
                self.subpackets.append(Packet(data[:subpacket_length]))
                data = data[subpacket_length:]
        else: # Error
            raise RuntimeError

def calc_packets(packet):
    for child in packet.subpackets:
        if child.literal == None:
            calc_packets(child)
    if packet.opcode == '000': # sum
        packet.literal = sum([x.literal for x in packet.subpackets])
    elif packet.opcode == '001': # product
        packet.literal = prod([x.literal for x in packet.subpackets])
    elif packet.opcode == '010': # minimum
        packet.literal = min([x.literal for x in packet.subpackets])
    elif packet.opcode == '011': # maximum
        packet.literal = max([x.literal for x in packet.subpackets])
    elif packet.opcode == '100': # literal
        return
    elif packet.opcode == '101': # greater than
        literals = [x.literal for x in packet.subpackets]
        packet.literal = int(literals[0] > literals[1])
    elif packet.opcode == '110': # less than
        literals = [x.literal for x in packet.subpackets]
        packet.literal = int(literals[0] < literals[1])
    elif packet.opcode == '111': # equal
        literals = [x.literal for x in packet.subpackets]
        packet.literal = int(literals[0] == literals[1])
    else:
        raise RuntimeError

root_packet = Packet(bits_code)
calc_packets(root_packet)
print(root_packet.literal)
