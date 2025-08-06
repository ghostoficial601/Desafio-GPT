acerto = "3"



question = str(input("tentativa: "))
if question != acerto:
    print("Errou")
    for i in range(2):
        question = str(input("tentativa: "))
        if question != acerto:
            print("Errou")
        elif question == acerto:
            break
        