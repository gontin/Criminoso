print("Responda com S/N")
contatin = input("Telefonou pra vitima?").upper().strip()
local = input("Esteve no local do crime?").upper().strip()
mora = input("Mora perto da vitima?").upper().strip()
agiota = input("Devia pra vitima?").upper().strip()
clt = input("Já trabalhou pra vítima?").upper().strip()
sus = 0
if contatin == "S":
    sus += 1
if local == "S":
    sus += 1
if mora == "S":
    sus += 1
if agiota == "S":
    sus += 1
if clt == "S":
    sus += 1


if sus == 0:
    print("hmm ta bom, pode ir")
elif sus <= 2:
    print("to de oio em vc, comédia")
elif sus <= 4:
    print("QUEM ESTAVA COM VC EM?? ME FALA, VC N PODE ESCONDER PRA SEMPRE")
elif sus >=5:
    print("FOI VC, ENCOSTA NA PAREDE DOG PERDEU PERDEU")
