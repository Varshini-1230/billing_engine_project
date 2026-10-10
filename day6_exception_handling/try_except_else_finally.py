try:
    total=int(open("scores.txt").read())
except FileNotFoundError:
    print("file is missing")
except ValueError:
    print("file is not a number")
else:
    print(f"Total is {total}")
finally:
    print("Done checking")
    

    