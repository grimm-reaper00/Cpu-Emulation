## 0x0_ = controle de sistema; 0x1_ = registradores; 0x2_ = ULA; 0x3_ = desvios de salto
from enum import IntEnum
class OpCode(IntEnum):
    NOP = 0x00
    HALT = 0x0F
    LOAD = 0x10
    STORE = 0x11
    ADD = 0x20
    SUB = 0x21
    AND = 0x22
    OR = 0x23
    JMP = 0x30
    JZ = 0x31
class Flag(IntEnum):
    ZERO = 1 << 0
    CARRY = 1 << 1
    NEGATIVE = 1 << 2

