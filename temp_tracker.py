
class TempTracker(object):
    """temp tracker class"""

    def insert(self):
        """record a new temp"""
        pass

    def get_max(self):
        """return highest temp seen so far"""
        pass

    def get_min(self):
        """return lowest temp seen so far"""
        pass

    def get_mean(self):
        """return mean of all temps seen so far"""
        pass

    def get_mode(self):
        """return mode of all temps seen so far"""
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
