import itertools

def weeklyExpenses(input):

    expenses = {
    26:"TOI",
    20.5:"Hindu",
    34: "ET",
    10.5:"BM",
    18:"HT",
    };
    prices=[26,20.5,34,10.5,18]
    papers=[]

    combination=list(itertools.combinations(prices, 2))
    for i in combination:
        if sum(i)<=input: 
            papers.append(i)
    
    np=[]
    for i in range(len(papers)):
        val1=papers[i][0]
        val2=papers[i][1]
        np.append((expenses[val1],expenses[val2])) 
    print(np)


input=int(input())
weeklyExpenses(input)