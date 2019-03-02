#coding:utf-8
def next_step(dataset,data_directory):
    while(True):
        menu.main_menu()
        choice = input("Enter your choice:\n=>")
        if choice == 1 :
            print "Wait..."
            finish = Q1.Question_1(dataset,data_directory)
            for length in range(len(finish)):
                print "Rank {} is number {}, which distance is {}".format(length+1,finish[length][0],finish[length][1])
                print "=================================================="
            print "Finish !!!"
            leave = raw_input("Enter any key to leave :\n=>")
        elif choice == 2:
            print "Wait..."
            finish = Q2.Question_2(dataset,data_directory)
            for length in range(len(finish)):
                print "Rank {} is number {}, which distance is {}".format(length+1,finish[length][0],finish[length][1])
                print "=================================================="
            print "Finish !!!"
            leave = raw_input("Enter any key to leave :\n=>")
        elif choice == 3:
            x =  Q3.Question_3(dataset,data_directory)
            X = np.array(x)
            kmeans = KMeans(n_clusters=10).fit(X)
            print kmeans.labels_
            leave = raw_input("Enter any key to leave :\n=>")
        elif choice == 4:
            print("尚未完成 QQ")
            leave = raw_input("Enter any key to leave :\n=>")
        elif choice == 5:
            break
        else:
            print("Enter Again...(Wait for few second)")
            time.sleep(3)

if __name__== "__main__" :
    import time
    from sklearn.cluster import KMeans
    import numpy as np
    import H3_104306093_menu as menu
    import H3_104306093_Q1 as Q1
    import H3_104306093_Q2 as Q2
    import H3_104306093_Q3 as Q3
    while(True):
        menu.choose_data()
        data_choice = input("Enter your choice:\n=>")
        if data_choice == 1:
            dataset = "dataset_clothes/*.jpg"
            data_directory = "dataset_clothes"
            next_step(dataset,data_directory)
        elif data_choice == 2:
            dataset = "dataset_life/*.jpg"
            data_directory = "dataset_life"
            next_step(dataset,data_directory)
        elif data_choice == 3:
            break;
        else:
            print("Enter Again...(Wait for few second)")
            time.sleep(3)
