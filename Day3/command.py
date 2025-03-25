import argparse

if __name__ =="__main__":
    parser = argparse. ArgumentParser()
    parser.add_argument("no1", help = "first no")
    parser.add_argument("no2", help = "second no")
    parser.add_argument("operation", help = "operation")
    args = parser.parse_args()
    
    print(args.no1)
    print(args.no2)
    print(args.operation)
    
    n1 = int(args.no1)
    n2 = int(args.no2)
    result = None
    if args.operation =="add":
        result = n1+n2
        
    print(result)