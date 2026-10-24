entrieslist=list(map(int,input().split()))
class EmptyLogError(Exception):
    pass

def show_log(entries):
    if not entries:
        #the below line is without exception
        #print("No log entries to didplay")
        raise EmptyLogError("No log entries to display")
    for entry in entries:
        print(entry)
        
try:
    show_log(entrieslist)
except EmptyLogError as e:
    print(f"Error:,{e}")