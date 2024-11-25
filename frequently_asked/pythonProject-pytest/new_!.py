name = 'linda'
rotate =1

length = len(name)
rsult = name[rotate: ] + name[0: rotate]
print(rsult)

# import subprocess
# import shlex
#
# HOST = '10.204.90.31'
#
# cmd = "ssh {}".format(HOST)
# subprocess.call(shlex.split(cmd))





class Employee:

    def find_smallest_in_list(self, l):
        self.l = l
        self.l.sort()
        return l[0]
    def sort(self, l):
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[j] < l[i]:
                    l[j], l[i] = l[i], l[j]
        return l[0]


    def find_reverse_of_string(self,s):
        reverse=''
        for i in s:

            reverse = i + reverse
        return reverse

if __name__ == "__main__":
    obj = Employee()
    print("smallest in [6,3,4,1,1,2,3]")
    print(obj.find_smallest_in_list([6,3,4,1,1,2,3]))
    print(obj.sort([6,3,4,1,1,2,3]))
    print('asgsfhf')
    print(obj.find_reverse_of_string('asgsfhf jdjcaks'))






















