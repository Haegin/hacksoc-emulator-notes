class Memory:
    """A class to represent the memory store of our processor.
    """

    def __init__(self, size):
        """Set up the memory, and reset it to all blanks.
        """

        self.data = []
        self.size = size

        self.reset()

    def reset(self):
        """Clear the contents of the memory.
        """

        self.data = [0] * self.size

    def read(self, address):
        """Read a value from memory, wrapping around from the top.
        """

        pass

    def write(self, address, value):
        """Write a value to memory (in the range 0 to 255), wrapping around
        from the top.
        """

        pass
