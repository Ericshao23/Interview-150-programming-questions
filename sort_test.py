import random
from datetime import datetime 
import shell_sort
import bubble_sort

class MainTest:
    def MainTest(self,):
        test_list = []
        for i in range(1000):
            test_list.append(random.randint(1, 10000))
        print(test_list)
        print('\n')

        start = datetime.now()
        # shell_sort.shell_sort(test_list)
        # bubble_sort.optimize_bubble_sort(test_list)
        end = datetime.now()
        print(test_list)
        print(start, end, (start - end).seconds)
        
test = MainTest()
test.MainTest()