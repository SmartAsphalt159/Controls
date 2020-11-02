import time



"""Call when all sensor have been updated"""
def onAllUpdated():
    global last_updated
    _now = time.time()
    _delta_t = last_updated - _now
    last_updated = _now




def checkUpdated():


if __name__=="__main__":
    last_updated = time.time()
    precision = 1 #cm
