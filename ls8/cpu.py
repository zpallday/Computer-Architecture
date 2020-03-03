"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.register = [0] * 8
        self.pc = 0
        self.sp = 256
        pass

    def load(self, program_file):
        """Load a program into memory."""

        address = 0
        # For now, we've just hardcoded a program:

        program = []

        with open(str(program_file)) as f:
            for line in f:
                line = line.split(' ')[0].rstrip()
                if len(line) == 8:
                    program.append(line)

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True
        while running:
            if self.ram[self.pc] == '10000010':
                self.register[int(self.ram[self.pc + 1], 2)] = self.ram[self.pc + 2]
                self.pc += 3

            elif self.ram[self.pc] == '01000111':
                print(int(self.register[int(self.ram[self.pc + 1],2 )], 2))
                self.pc += 2

            elif self.ram[self.pc] == '10100010':
                a = self.register[int(self.ram[self.pc + 1], 2)]
                b = self.register[int(self.ram[self.pc + 2], 2)]
                a = int(str(a), 2)
                b = int(str(b), 2)
                print(a * b)
                self.pc += 3

            elif self.ram[self.pc] == '10100000':
                first = self.register[int(self.ram[self.pc +1], 2)]
                second = self.register[int(self.ram[self.pc + 2], 2)]
                byte = bin(int(first, 2) + int(second, 2)).lstrip('0b')
                byte = '0' * (8 - len(byte)) + byte 
                self.register[int(self.ram[self.pc + 1], 2)] = byte
                self.pc += 3

            elif self.ram[self.pc] == '01000101':
                self.sp -= 1
                self.ram[self.sp] = self.register[int(self.ram[self.pc + 1], 2)]
                self.pc += 2

            elif self.ram[self.pc] == '01010000':
                self.sp -= 1
                self.ram[self.sp] = self.pc + 2
                self.pc = int(self.register[int(self.ram[self.pc + 1], 2)], 2)

            elif self.ram[self.pc] == '00010001':
                 self.pc = self.ram[self.sp]
                 self.sp += 1

            elif self.ram[self.pc] == '01000110':
                self.ram[self.sp] = self.register[int(self.ram[self.pc + 1], 2)] = self.ram[self.sp]
                self.sp += 1
                self.pc += 2

            elif self.ram[self.pc] == '00000001':
                    self.pc = 0
                    break
            else: 
                    print(f'{self.ram[self.pc]} is unknown')
                    break
        def ram_read(self, address):
            return self.ram[int(str(address), 2)]
        def ram_write(self, address, value):
            self.ram[int(str(address), 2)] = value
    pass