import numpy as np

def conversion (coordfl,demdeltax,demdeltay, Dimterrain, precision_voulue):
    """In : coordfl : tuple de float (abscisse, ordonnée) , demdeltax: demi-plage 
    de précision(obtenue par Monte Carlo plage de valeur) sur l'abscisse, demdeltay: 
    demi-plage de précision(obtenue par Monte Carlo plage de valeur) sur l'ordonnée
    Dimterrain : tuple d'entiers (longueur,largeur ), 
    précision voulue: rayon du cercle autour du joueur dans lequel doit 
    se situer la donnée (on prend 2.1m pour avoir un carré de 3m de côté)
    Out: N :nombres de carrés à allumer et lstcarres liste de N tuples d'entiers 
    (coordonnées en carrés abscisse et ordonnée)"""
    cote=np.sqrt(2)*precision_voulue
    print(cote)
    coordA=(coordfl[0]-demdeltax,coordfl[1]-demdeltay)
    print(coordA)#coord du point en bas à gauche
    nbcarresx=round(Dimterrain[0]/cote)
    nbcarresy=round(Dimterrain[1]/cote)
    print(nbcarresx,nbcarresy)
    i,j=0,0
    
    while coordA[0]>cote*i:
        i+=1
    icarre=max(0,i-1)
    if icarre>=nbcarresx:
        icarre=nbcarresx-1
        print('trop long')
    
    while coordA[1]>cote*j:
        j+=1
    jcarre=max(0,j-1)
    
    if jcarre>=nbcarresy:
        jcarre=nbcarresy-1
        print('trop haut')
    
    lstcarres=[(icarre,jcarre)]
    print(lstcarres)
    if coordA[0]+2*demdeltax>(icarre+1)*cote:
        icarredroite,jcarredroite=icarre+1,jcarre
        if icarredroite<nbcarresx :
            lstcarres.append((icarredroite,jcarredroite))
    if coordA[1]+2*demdeltay>(jcarre+1)*cote:
        icarrehaut,jcarrehaut=icarre,jcarre+1
        if jcarrehaut<nbcarresy:
            lstcarres.append((icarrehaut,jcarrehaut))
    if len(lstcarres)==3:
        icarrediag,jcarrediag=icarre+1,jcarre+1
        lstcarres.append((icarrediag,jcarrediag))
    N=len(lstcarres)
    return N, lstcarres