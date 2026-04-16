def flames(first_name,second_name):
    leng=0
    for i in first_name:
        for j in second_name:
            if i != j:
                leng=leng+1

    flame=["F - Friends","L - Love","A - Affection","M - Marriage","E - Enemy","S - Siblings"]
    div = leng % 6
    return(flame[div])

first_name=list(input("Enter your first name: ").split(" "))
first_name="".join(first_name)
second_name=list(input("Enter your second name: ").split(" "))
second_name="".join(second_name)

flames_obj = flames(first_name,second_name)
print(flames_obj) 