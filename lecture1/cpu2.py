from memory import Memory


class CPU:
    """A class implementing a PicoBlaze CPU.
    """

    def __init__(self):
        """Set up the initial state of the processor.
        """

        self.flags = {"zero": False,
                      "carry": False}

        self.registers = [0] * 16

        self.memory = Memory(256)
