def snail(array):
    n = len(array)
    movement_count = n + (n-1)
    lst = []

    Top_Row = 0
    Top_Row_Start_Position = 0
    Top_Row_End_Position = n-1

    Bottom_Row = n-1
    Bottom_Row_Start_Position = -2
    Bottom_Row_End_Position = 0

    Right_Column = -1
    Left_Column = 0

    counter = 0

    if n == 1:
        return array[0]
    else:
    
        while counter < movement_count:
        
            #Top Row Movement - Forward
            for num in array[Top_Row][Top_Row_Start_Position:Top_Row_End_Position]:
                lst.append(num)
            counter+=1
            Top_Row_Start_Position += 1
            Top_Row_End_Position -= 1
    
            #Right Column Vertical Movement - Down
            for num in array[Top_Row:Bottom_Row+1]:
                lst.append(num[Right_Column])
            counter+=1
            Right_Column -= 1
    
            #Bottom Row Movement - Backwards
            for num in array[Bottom_Row][Bottom_Row_Start_Position:Bottom_Row_End_Position:-1]:
                lst.append(num)
            counter+=1
            Bottom_Row_Start_Position -= 1
            Bottom_Row_End_Position += 1

            #Left Column Vertical Movement - Up
            for num in array[Bottom_Row:Top_Row:-1]:
                lst.append(num[Left_Column])
            counter+=1
            Left_Column += 1

            Top_Row += 1
            Bottom_Row -= 1
        
        return lst
