def recursive_dfa(input_string,current_state,transitions):
    if not input_string:
        return current_state in transitions['final']   
    next_state = transitions.get((current_state, input_string[0]))
    if next_state is not None:
        return recursive_dfa(input_string[1:], next_state, transitions)
    else:
        return False
    
number_of_test=int(input())
for i in range(number_of_test):
    number_of_operartor=int(input())
    op1=input()
    list_operator=(op1.split())

    number_of_state=int(input())
    state=input()
    list_state=(state.split())
    
    number_of_transitions=int(input())
    list_startState=[]
    list_optransion=[]
    list_finalState=[]
    for i in range(number_of_transitions):
        transition=input()
        x=transition.split()
        list_startState.append(x[0])
        list_optransion.append(x[1])
        list_finalState.append(x[2])
        x=None
        
    transitions = {}
    for i in range(len(list_optransion)):
            transitions[(list_startState[i],list_optransion[i])] = list_finalState[i]

    start_state=input()
    number_of_final_state=int(input())
    final_state=input()
    transitions['final']=final_state
    
    number_of_test=int(input())
    list_string=[]
    for i in range(number_of_test):
        string=input()
        list_string.append(string)
        
    for i in range(len(list_string)):
        print(recursive_dfa(list_string[i],start_state,transitions))
        
    print("-------")

#test 1  ->   t,f,t,f
#test 2  ->   t,f,t,t
#test 3  ->   f,t,t,t