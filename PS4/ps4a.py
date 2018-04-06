# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def get_permutations(sequence):
    alist = []
    beg=sequence[0:0]
    end=sequence[:]
    def f(beg,end,alist):
        if len(end) <= 1:
            if beg+end not in alist:
                return alist.append(beg+end)
            return
        else:
            for i in range(len(end)):
                temp = end[:i] + end[i+1:]
                f(beg+end[i],temp,alist)
    f(beg,end,alist)
    return alist
    
if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input2 = 'emr'
    print('Input:', example_input2)
    print('Expected Output:', ['emr','erm','rme','rem','mer','mre'])
    print('Actual Output:', get_permutations(example_input2))
    
    example_input3 = 'eb'
    print('Input:', example_input3)
    print('Expected Output:', ['eb','be'])
    print('Actual Output:', get_permutations(example_input3))
    