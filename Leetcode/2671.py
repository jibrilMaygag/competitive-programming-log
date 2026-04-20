class FrequencyTracker:

    def __init__(self):
        self.num_count={}
        self.freq_count={}
        

    def add(self, number) :
        old_freq=self.num_count.get(number,0)
        new_freq=old_freq+1
        #decrease old freq
        if old_freq>0:
            self.freq_count[old_freq]-=1
            if self.freq_count[old_freq]==0:
                del self.freq_count[old_freq]
        #increase new frequency count
        self.freq_count[new_freq]=self.freq_count.get(new_freq,0)+1

        self.num_count[number]=new_freq
    def deleteOne(self, number) :
        if number not in self.num_count:
            return
        old_freq=self.num_count.get(number)
        new_freq=old_freq-1
        # decrease old
        self.freq_count[old_freq]-=1
        if self.freq_count[old_freq]==0:
            del self.freq_count[old_freq]


        if new_freq==0:
            del self.num_count[number]
        else:
            self.num_count[number]=new_freq
            self.freq_count[new_freq]=self.freq_count.get(new_freq,0)+1
    def hasFrequency(self, frequency):
        return self.freq_count.get(frequency,0)>0
        

