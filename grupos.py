
def calSubGrupos (lista = [], nSubGrupos = 0):
    if (nSubGrupos <= 0): return []
    if (nSubGrupos == 1): return [[e] for e in lista]
    subGruposSubLista = calSubGrupos (lista = lista[1:], nSubGrupos= nSubGrupos - 1)
    # print ("nSubGrupos: ", nSubGrupos, "subGruposSubLista = ", subGruposSubLista)
    subGrupos = []
    for i in range(len(subGruposSubLista)):
        # print (nSubGrupos, ": ", [subGrupo for subGrupo in subGruposSubLista[i:]])
        subGrupos.append ([[lista[i]] + subGrupo for subGrupo in subGruposSubLista[i:]])
    return subGrupos


lista = ["React", "Ionic", "Xamarin", "Java"]

nSubGrupos = int (input ("Ingrese numero de sub-grupos: "))


subGrupos = calSubGrupos (lista = lista, nSubGrupos = nSubGrupos)

for e in subGrupos:
    print (e)
