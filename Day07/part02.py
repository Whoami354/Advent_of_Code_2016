import re
from typing import List, Set
def parse_input(filename: str) -> List[List[str]]:
    ips = [re.split(r'\[([^\]]+)\]', line.strip()) for line in open(filename).readlines()]
    return ips

def has_bab(parts: List[str], aba) -> bool:
    a, b = aba[0], aba[1]
    bab = b + a + b
    for part in parts:
        if bab in part:
            return True
    return False

def find_abas(parts: List[str]) -> Set[str]:
    abas = []
    for part in parts:
        for i in range(len(part) - 2):
            if part[i] == part[i + 2] and part[i] != part[i + 1]:
                abas.append(part[i: i + 3])
    return set(abas)

def supports_ssl(ip: List[str]) -> bool:
    supernet = ip[::2]
    hypernet = ip[1::2]
    abas = find_abas(supernet)
    for aba in abas:
        if has_bab(hypernet, aba):
            return True
    return False

def part2(ips: List[List[str]]) -> int:
    return sum([1 for ip in ips if supports_ssl(ip)])

ips = parse_input('input')
print(f'Part 2: {part2(ips)}')