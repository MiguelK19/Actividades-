import threading

myArray = [1, 2, 2, 5, 4, 6, 7, 8, 8, 8]

class LongestSequenceThread(threading.Thread):
    def init(self, threadID, name, array):
        threading.Thread.init(self)
        self.threadID = threadID
        self.name = name
        self.array = array

    def run(self):
        longitud = 1
        numero = self.array[0]
        current = 1
        for i in range(1, len(self.array)):
            if self.array[i] == self.array[i-1]:
                current += 1
            else:
                if current > longitud:
                    longitud = current
                    numero = self.array[i-1]
                current = 1
        if current > longitud:
            longitud = current
            numero = self.array[-1]
        print("longitud: {} numero: {}".format(longitud, numero))

thread = LongestSequenceThread(1, "LongestSequenceThread", myArray)
thread.start()