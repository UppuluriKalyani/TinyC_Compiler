class Operand:
    pass


class Variable(Operand):
    def __init__(self, symbol_entry):
        self.symbol_entry = symbol_entry

    def getDatatype(self):
        return self.symbol_entry.getDataType()

    def print(self):
        return self.symbol_entry.getSymbolName()

    def getValue(self):
        return self.symbol_entry.getSymbolName()


class Constant(Operand):
    def __init__(self, value):
        self.value = value

    def print(self):
        return self.value

    def getDatatype(self):
        return type(self.value)

    def getValue(self):
        return self.value


class Quadruple:
    def __init__(self, opd1, opd2, result, opcode):
        self.opd1 = opd1
        self.opd2 = opd2
        self.result = result
        self.opcode = opcode

    def getopd1(self):
        return self.opd1

    def getopd2(self):
        return self.opd2

    def getresult(self):
        return self.result

    def getopcode(self):
        return self.opcode

    def getDatatype(self):
        return self.result.getDatatype()

    def print(self):
        if self.opd2 is not None:
            if isinstance(self.opd1, Quadruple) and not isinstance(self.opd2, Quadruple):
                print(f"\t\t{self.getresult().getName()} = "
                      f"{self.getopd1().getresult().getName()} {self.getopcode()} {self.getopd2().getValue()}")
            elif not isinstance(self.opd1, Quadruple) and isinstance(self.opd2, Quadruple):
                print(f"\t\t{self.getresult().getName()} = {self.getopd1().getValue()} "
                      f"{self.getopcode()} {self.getopd2().getresult().getName()}")
            elif isinstance(self.opd1, Quadruple) and isinstance(self.opd2, Quadruple):
                print(f"\t\t{self.getresult().getName()} = "
                      f"{self.getopd1().getresult().getName()} {self.getopcode()} {self.getopd2().getresult().getName()}")
            else:
                print(f"\t\t{self.getresult().getName()} = {self.getopd1().getValue()} {self.getopcode()} {self.getopd2().getValue()}")
        else:
            if isinstance(self.opd1, Quadruple):
                print(f"\t\t{self.getresult().getValue()} = {self.getopd1().getresult().getName()}")
            else:
                print(f"\t\t{self.getresult().getValue()} = {self.getopd1().getValue()}")


class NewTemp:
    inc = 0

    def __init__(self, datatype):
        NewTemp.inc += 1
        self.temp = f"t{NewTemp.inc}"
        self.datatype = datatype

    def print(self):
        return self.temp

    def getDatatype(self):
        return self.datatype

    def getName(self):
        return self.temp
