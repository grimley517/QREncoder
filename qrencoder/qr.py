import math
class qrc(object):
    sizemin = 1
    sizemax = 40
    sizeList =[[41,34,27,17],
        [77,63,48,34],
        [127, 101, 77,58],
        [187, 149, 111,82],
        [255, 202, 144,106],
        [322, 255, 178,139],
        [370, 293, 207,194],
        [461, 365, 259,202],
        [552, 432, 312,235],
        [652, 513, 364,288],
        [772, 604, 427, 331],
        [883, 691, 489, 371],
        [1022,796, 580,427],
        [1101, 871, 621, 468],
        [1250, 991, 702, 503],
        [1408, 1082, 775, 602],
        [1548, 1212, 876, 674],
        [1725, 1346, 948, 746],
        [1903, 1500, 1063, 813],
        [2061, 1600, 1159, 919],
        [2232, 1708, 1224, 969],
        [2409, 1872, 1359, 1056],
        [2620, 2059, 1468, 1108],
        [2812, 2188, 1588, 1228],
        [3057, 2395, 1718, 1286],
        [3283, 2544, 1804, 1425],
        [3517, 2701, 1933, 1501],
        [3669, 2857, 2085, 1581],
        [3909, 3035, 2181, 1677],
        [4158, 3289, 2358, 1782],
        [4417, 3486, 2473, 1897],
        [4686, 3693, 2670, 2022],
        [4965, 3909, 2805, 2157],
        [5253, 4134, 2949, 2301],
        [5529, 4343, 3081, 2361],
        [5836, 4588, 3244, 2524],
        [6153, 4775, 3417, 2625],
        [6479, 5039, 3599, 2735],
        [6743, 5313, 3791, 2927],
        [7089, 5596, 3993, 3057]]
    
    def __init__ (self, msg = '', quality = 'L'):
        self.msg = str(msg)
        self.quality = quality
        if self.msg.isdigit():
            self.msgtype = 0
            self.size = self.getSizeNumeric(msg)
        elif self.msg.isalnum():
            self.msgtype = 1
        else:
            raise TypeError('message type not recognised')
    
    def getSizeNumeric(self, message, enc=2):
        messageLength = len(message)
        answer = 1
        for i,n in enumerate(self.sizeList):
            if messageLength > n[enc]:
                answer = answer +1
        if answer > 40:
            raise ValueError('Size too large for any version')
        return (answer)
        
    def __repr__(self):
        return self.msg