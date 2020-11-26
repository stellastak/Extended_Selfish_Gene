class first_try:

    def __init__(self, number_a, number_b):
        self.num_a = number_a
        self.num_b = number_b

    def __str__(self):
        return "I am a dummy calculator"

    def add(self):
        """
        comments here
        """
        return self.num_a + self.num_b

    def sub(self):
        """
        Take this self.

        :returns: number
        """
        return self.num_a - self.num_b

    def mul(self):
        """
        :type name: string
        """
        return self.num_a * self.num_b

    def div(self):
        """
        :param name: isitok
        """
        return self.num_a / self.num_b
