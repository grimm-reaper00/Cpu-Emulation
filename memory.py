class Memory:
    def __init__(self, size: int = 8192):
        self._size = size
        self._data = bytearray(size)
    def read(self, address: int):
        if address < 0 or address >= self._size:
            raise IndexError(f"FATAL ERROR Invalid Memory Allocation 0x{address:04X}")
        return self._data[address]
    def write(self, address: int, value: int):
        if address < 0 or address >= self._size:
            raise IndexError(f"FATAL ERROR Invalid Memory Allocation 0x{address:04X}")
        truncated = value & 0xFF
        self._data[address] = truncated
    def load_binary(self, data: bytes, start_address: int = 0x0000):
        if start_address < 0 or (start_address + len(data)) > self._size:
            raise IndexError(f"FATAL ERROR Program binary exceeds memory capacity at 0x{start_address:04X}")
        for offset, byte in enumerate(data):
            self.write(start_address + offset, byte)



