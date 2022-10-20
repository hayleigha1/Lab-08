import math

def mean_func(lst):
    if len(lst) == 0:
        return 0.0
    
    else:
        sum_lst = 0.0

        for i in lst:
            sum_lst += i

        mean = sum_lst/len(lst)
        return mean

def std(lst):
    sum_lst = 0.0
    for i in lst:
        sum_lst += (i - mean_func(lst))**2

    std = math.sqrt((sum_lst/len(lst)))
    return std
    print(std)
        
     
    
        
def display_scores(t,a):
    num_tests = len(t)
    num_assignments = len(a)

    print(f'{"Type":<10}{"#":>10}{"min":>10}{"max":>10}{"avg":>10}{"avg":>10}')
    print("============================================================")

    if num_tests == 0:
        min_test = "n/a"
        max_test = "n/a"
        avg_test = "n/a"
        std_test = "n/a"

    else:
        min_test = min(t)
        max_test = max(t)
        avg_test = mean_func(t)
        std_test = std(t)

    print(f'{"Tests":<10}{num_tests:>10}{min_test:>10}{max_test:>10}{avg_test:>10}{std_test:>10}')

    if num_assignments == 0:
        amin_test = "n/a"
        amax_test = "n/a"
        aavg_test = "n/a"
        astd_test = "n/a"

    else:
        amin_test = min(a)
        amax_test = max(a)
        aavg_test = mean_func(a)
        astd_test = std(a)

    print(f'{"Programs":<10}{num_assignments:>10}{amin_test:>10}{amax_test:>10}{aavg_test:>10}{astd_test:>10}')
    print()

    we_scores = (avg_test * 0.60) + (aavg_test * 0.40)
    print("The weighted scores is",     we_scores)
        
        
    
        
    







test_scores = []
assignment_scores = []

while True:
    print("            Grade Menu")
    print("1 - Add Test")
    print("2 - Remove Test")
    print("3 - Clear Tests")
    print("4 - Add Assignment")
    print("5 - Remove Assignment")
    print("6 - Clear Assignments")
    print("D - Display Scores")
    print("Q - Quit")
    print()

    choice =input("==> ")
        

    if choice == "1":
        print()
        tscore = float(input("Enter the new test score 0-100 ==> "))
        print()

        while (tscore < 0) :
            print("The score must be gtreater than 0.")
            tscore = float(input("==> "))

        test_scores.append(tscore)

    elif choice == "2":
        print()
        tscore = float(input("Enter the Test score to remove ==> "))
        print()

        for i in test_scores:
            if tscore == i:
                test_scores.remove(i)

            else:
                print("Could not find that score to remove.")
                       
    elif choice == "3":
        test_scores.clear()
            
    elif choice == "4":
        print()
        ascore = float(input("Enter the new assignment score 0-100 ==> "))
        print()

        while (ascore < 0):
            print("The score must be greater than 0.")
            ascore = float(input("==> "))

        assignment_scores.append(ascore)

    elif choice == "5":
        print()
        ascore = float(input("Enter the assignment score to remove ==> "))
        print()

        for i in assignment_scores:
            if ascore == i:
                    assignment_scores.remove(i)

            else:
                print("Could not find that score to remove.")
            
    elif choice == "6":
        assignment_scores.clear()

    elif (choice == "D") or (choice == "d"):
        display_scores(test_scores, assignment_scores)

    elif (choice == "Q") or (choice == "q"):
        break

    else:
        print("Please enter a valid choice")
        print()



