class CPU:
    """A class implementing a PicoBlaze CPU.
    """

    def __init__(self):
        """Set up the initial state of the processor.
        """

        self.flags = {}
        self.registers = []
