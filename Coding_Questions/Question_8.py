def checkmoney(x):
    if x in range(7000,10001):
        print("Cool, thanks sis! {} rupees will certainly help.".format(x))
    elif x<7000:
        print("Ahem, can you rethink this number please?")
    elif x>10000:
        print("Wow sis! You are a queen!")
    return

sis=8500
checkmoney(sis)
