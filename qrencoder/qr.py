class qrc(object):
    sizemin = 1
    sizemax = 40
    sizelist = [26,44,70,100,134,172,196,242,292,346,404,466,532, 582, 655,733, 
    835,901,991,1085,1156,1258,1364, 1474, 1588, 1706, 1828, 1921, 2051, 2185, 
    2323, 2465, 2611, 2761, 2876, 3034, 3196, 3362, 3532, 3706]
    
    def __init__ (self, msg = '', quality = 'L'):
        self.msg = str(msg)
        self.quality = quality
        if self.msg.isdigit():
            self.msgtype = 0
            
        elif self.msg.isalnum():
            self.msgtype = 1
        else:
            raise typeerror
        
        
    def __repr__(self):
        return self.msg