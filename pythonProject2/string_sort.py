class Finder:
    def __init__(self, l):
        self.l = l

    def find(self,ele):
        for i in self.l:
            print(i)
            '''
            item = ''.join(sorted(i))
            if item == ''.join(sorted(ele)):
                print(i)
            '''
finder = Finder(['asd','asdd', 'fre'])
finder.find('dsda')