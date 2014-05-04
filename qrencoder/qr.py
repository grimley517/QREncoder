class qrc(object):
    sizemin = 1
    sizemax = 40
    
    def __init__ (self, size = 0, msg = '', quality = 'L'):
        self.size = size
        self.msg = msg
        self.quality = quality
        
    def __repr__(self):
        return self.msg