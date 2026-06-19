def main():
    miles = int(input("Miles? "))
    minutes=int(input("Minutes"))
    pace = get_pace(miles, minutes)
    print(f"you need to run each mile in {round(pace, 2)} minutes")

def get_pace(m, min):
    if not min> 0:
    # specific valueError exception should be raise. A message could also be displayed for user
        raise ValueError("Minutes cannot be zero") 
        #raise Exception() # general exception
    return min/m

if __name__ == "__main__":
    main()