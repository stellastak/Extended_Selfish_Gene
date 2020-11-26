"""
FirstTry.py
====================================
The core module of my example project
"""


def about_me(your_name):
    """
    Return the most important thing about a person.

    Parameters
    ----------
    your_name
        A string indicating the name of the person.
    """
    return "The wise {} loves Python.".format(your_name)


class FirstTry():

    def __init__(self, number_a, number_b):
        """
        Return Blah blah blah.

        Parameters
        ---------
        number_a, number_b
            To numbers to be calculated.
        """
        self.num_a = number_a
        self.num_b = number_b

    def __str__(self):
        return "I am a dummy calculator"

    def add(self):
        """
        Return the most important thing about a person.

        Parameters
        ----------
        number_a, number_b
        Two ints to be added.
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
        :type: string
        """
        return self.num_a * self.num_b

    def div(self):
        """
        :param: isitok
        """
        return self.num_a / self.num_b


if __name__ == "__main__":
    calc1 = FirstTry(5, 3)
    calc1.add()
