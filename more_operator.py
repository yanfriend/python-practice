class Array:  
    __list = []  
  
    def __init__(self):  
        print "constructor"  
  
    def __del__(self):  
        print "destructor"  
  
    def __str__(self):  
        return "this self-defined array class"  
  
    def __getitem__(self, key):  
        return self.__list[key]  
  
    def __len__(self):  
        return len(self.__list)  
  
    def Add(self, value):  
        self.__list.append(value)  
  
    def Remove(self, index):  
        del self.__list[index]  
  
    def DisplayItems(self):  
        print "show all items----"  
        for item in self.__list:  
            print item  
  
arr = Array()   #constructor  
print arr    #this self-defined array class  
print len(arr)   #0  
arr.Add(1)  
arr.Add(2)  
arr.Add(3)  
print len(arr)   #3  
print arr[0]   #1  
arr.DisplayItems()  
#show all items----  
#1  
#2  
#3  
arr.Remove(1)  
arr.DisplayItems()  
#show all items----  
#1  
#3  
#destructor  
