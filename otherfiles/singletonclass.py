# Singleton Borg pattern
class Borg:

	# state shared by each instance
	__shared_state = dict()

	# constructor method
	def __init__(self):

		self.__dict__ = self.__shared_state
		self.state = 'GeeksforGeeks'

	def __str__(self):

		return self.state






class NewClass(object):
    _instance = None

    def __init__(self):
        if self._instance is None:
            self._instance = 10


n = NewClass()
n._instance = 6

n2 = NewClass()
print(n2._instance)
