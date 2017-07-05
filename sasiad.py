sasiad = raw_input("Sasiad: ")

print "Witaj moj drogi sasiedzie, ", sasiad
print "Czego sie napijesz?"
napoj = raw_input("Napije sie ...")
if int(napoj) < 100:
    print "oto twoja herbata"
elif napoj == "kawa":
    print "Prosze kawe z mlekiem,"
    odpowiedz = raw_input(".:")
    if odpowiedz == "tak":
        print "Prosze o to mleko"
    else:
        print "Prosze kawe bez mleka"
else:
    print "Niestety nie mam ", napoj
