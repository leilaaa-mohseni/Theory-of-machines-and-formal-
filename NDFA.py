def recursive_ndfa(string, current_states, transition, final_states):
    if not string:
        return any(state in final_states for state in current_states)
    next_states = set()
    for state in current_states:
        symbol_transitions = transition.get((state, string[0]), set())
        next_states.update(symbol_transitions)
    return recursive_ndfa(string[1:], next_states, transition, final_states)

number_of_test=int(input())
for i in range(number_of_test):    
        number_of_operartor=int(input())
        list_operator=[]
        op1=input()
        list_operator=(op1.split())

        number_of_state=int(input())
        list_state=[]
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
                if (list_startState[i],list_optransion[i]) in transitions:
                        transitions[(list_startState[i],list_optransion[i])].append((list_finalState[i]))
                else:
                        transitions[(list_startState[i],list_optransion[i])] = [list_finalState[i]]

        start_state=input()
        number_of_final_state=int(input())
        final_state=input()

        number_of_test=int(input())
        list_string=[]
        for i in range(number_of_test):
            string=input()
            list_string.append(string)

        for i in range(len(list_string)):
            print(recursive_ndfa(list_string[i],{start_state},transitions,{final_state}))
        print("------")
        
#test 1 -> t,t,t,t
#test 2 -> t,f,f,t
#test 3 -> f,t,f,t