# python3
# Linda Slapina 221RDB214

def parallel_processing(n, m, data):
    output = []
    test = [(i,0) for i in range (n)]
    for i in range(m):
        test_index, test_end_time = min(test, key= lambda x: x[1])
        output.append((test_index, test_end_time))
        test[test_index] = (test_index, test_end_time+data[i])
    return output

def main():
    n,m = map (int, input().split())
    data = list(map(int, input().split()))
    
    result = parallel_processing(n,m,data)
    
    for i in range(m):
        print(result[i][0], result[i][1])



if __name__ == "__main__":
    main()
