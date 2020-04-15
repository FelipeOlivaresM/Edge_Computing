def leerDatos():
    with open("mitbih_test.csv", "r") as f:
        text = [i.split(",") for  i in f.readlines()]
        return text
    
        