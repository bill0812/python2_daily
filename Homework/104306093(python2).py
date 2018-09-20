#Problem 1 ( Cosine Similarity )
def cosine_similarity(A,B):
    ### write your code here ###
    result_value = float()
    fractions_reresult_value = float()
    numerator_reresult_value = float()
    fractions_reresult_value = 0
    numerator_reresult_value = 0
    for i in range(len(A)):
        fractions_reresult_value = fractions_reresult_value + A[i]*B[i]
    for i in range(len(A)):
        numerator_reresult_value = numerator_reresult_value + A[i]*A[i]
    for i in range(len(B)):
        numerator_reresult_value = numerator_reresult_value + B[i]*B[i]
    
    result_value = fractions_reresult_value/(numerator_reresult_value**0.5)
    return result_value

#Problem 2 ( Grades )
def grades(file_path):
    import csv
    dict_grades = dict()
    tuple_grades = tuple()
    reader = csv.reader(open(file_path,"r"))
    dict_reader = csv.DictReader(open(file_path,"r"))
    file = open("new.csv","w")
    each_score = list()
    each_row = list()

    for row in dict_reader:
        each_score.append(int(row[' Score']))
        
    
    next(reader)
    for i in reader:
        i[1] = i[1].replace(" ","")
        i[2] = i[2].replace(" ","")
        each_row.append(tuple(i))
    
   
    each_row = sorted(each_row,key = lambda x:(x[0],x[1],x[2]))
    tuple_grades = (tuple)(each_row)
        
    for i in range(10):
        first_score = i*10
        last_score = i*10 + 9
        dict_grades[str(first_score) +'~' + str(last_score) ] = 0
        
    for i in range(len(each_score)):
        if((each_score[i]/10)==9):
            dict_grades['90~99'] +=1
        elif((each_score[i]/10)==8):
            dict_grades['80~89'] +=1
        elif((each_score[i]/10)==7):
            dict_grades['70~79'] +=1
        elif((each_score[i]/10)==6):    
            dict_grades['60~69'] +=1
        elif((each_score[i]/10)==5):    
            dict_grades['50~59'] +=1
        elif((each_score[i]/10)==4):    
            dict_grades['40~49'] +=1
        elif((each_score[i]/10)==3):    
            dict_grades['30~39'] +=1
        elif((each_score[i]/10)==2):    
            dict_grades['20~29'] +=1
        elif((each_score[i]/10)==1):    
            dict_grades['10~19'] +=1
        elif((each_score[i]/10)==0):    
            dict_grades['0~9'] +=1
            
    for key,value in dict_grades.items():
        print(type(dict_grades.items()))
        if(dict_grades[key]==0):
            del dict_grades[key]
    
    for row in tuple_grades:
        file.write(row[0]+", ")
        file.write(row[1]+", ")
        file.write(row[2]+"\n")
    
    
    
    return dict_grades, tuple_grades

#Problem 3 ( The valid of password )
def valid_password(passwords):
    result_list = list()    
    for every_pwd in passwords:
       
        if(len(every_pwd) > 10 or len(every_pwd) < 5):
            break
        else:
            countUpper = 0
            countLower = 0
            countnumber = 0
            countotherchc = 0
            for pwdstr in every_pwd:
                
                if(pwdstr.isupper()):
                    countUpper += 1
                if(pwdstr.islower()):
                    countLower += 1
                if(pwdstr.isdigit()):
                    countnumber += 1
                if(pwdstr == '%' or pwdstr == '!' 
                   or pwdstr == '?' or pwdstr == '#' or pwdstr =='@'
                   or pwdstr == '$'):
                    countotherchc += 1
                    
            if(countUpper >= 1 and countLower >= 1
               and countnumber >= 2 and countotherchc >= 1):
                result_list.append(every_pwd)
             
    return result_list



if __name__ == "__main__":
    pro_1_value = cosine_similarity([1,2,3],[4,5,6])
    pro_2_dict, pro_2_tuple = grades('./example.csv')
    pro_3_list = valid_password(['Ab12!','AA1234!?','AbCdEfGh','12345AaBa!', '12Zz!?98Aa#@'])
    print pro_1_value
    print pro_2_dict
    print pro_2_tuple
    print pro_3_list
