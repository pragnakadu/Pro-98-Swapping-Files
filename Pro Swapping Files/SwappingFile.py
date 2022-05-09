def swapFileData() : 
        file1 = input("Name the file1 which needs to be swaped: ")
        file2 = input("Name the file2 which needs to be swaped: ")
        with open(file1 , 'r') as a:
             data_a =a.read()

        with open(file2 , 'r') as b:
              data_b = b.read()

        with open(file1 , 'w+') as a:
             a.write(data_b)

        with open(file2 , 'w+') as b:
             b.write(data_a)
swapFileData()




        
