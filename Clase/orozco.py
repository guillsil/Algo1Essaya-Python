LETRA_OROZCO = """Nosotros no somos como los orozco,
Yo los conozco, son ocho los monos:
Pocho, toto, cholo, tom, moncho, rodolfo, otto, pololo.
Yo pongo los votos solo por rodolfo.
Los otros son locos. yo los conozco.
No los soporto, stop. stop.

Pocho orozco: odontólogo ortodoxo doctor-como borocotó-
Oncólogo jodón - morocho tordo - groncho jocoso - trosko -
Chocó con los montos - colocó molotov.
Bonzo, stop, stop.

Toto orozco: colocón - drogón como pocos -
Tomó todos los hongos - monologó solo por dos otoños -
Votó - formol por los ojos - tomó cloformo -
Bols - ron - porrón - torronto - toso norton con bordon -
¿lo votó o no? - doblo los codos como loco - coño!!, sos vos toto? -
Corroboró - socorro como tomó - morfó hot dog - mondongo -
Pollo con porotos - lloró, lloró con dolor - por comó lloró tomo dos hongos -
Tocó fondo - torró como locos - contó todo, todo, todo.
Bochornoso como coppolo, stop, stop.

Cholo orozco: mocoso - soplón - moroso - bocón -
Chorro como grosso - robó dos potros por comodoro -
Los montó - los trotó por bolsón, por los toldos, por chocón.
Doloroso, stop, stop.

Tom orozco: proctólogo morboso - compró por los shops fotos porno color -
Compró como dos tomos - trozos - cosos - colchón roto -
Homos como gomón - trolos gozosos con condón -
Pomos con moños rococó -todos polvos cortos.
Fogozo, stop, stop.

Nosotros no somos como los orozco,
Yo los conozco, son ocho los monos:
Pocho, toto, cholo, tom, moncho, rodolfo, otto, pololo.
Yo pongo los votos solo por rodolfo.
Los otros son locos. yo los conozco.
No los soporto, stop. stop.

Moncho orozco: solo probó porro - votó con los ojos rojos por los polos -
Votó por bonn - por hong kong - por london soñó con yoko ono -
Lloró por john - voló por vos - voló por nosotros - brotó como flor bordó -
Roló pot, nos contó - los tronchos son grosos como los corchos.
Bocho borroso, stop, stop.

Rodolfo orozco: con voz como john scott - ronco, ronco -
Formó todos los coros - tocó: dobro con mollo - mombo con moro -
Ton ton con pomo - joropo con tormo - bongó con don johnson -
Tocó con t.o.t.o - los lobos - los door - los moscos -
Compró dos vox - tocó "socorro" con pol - nos contó con honor -
Tocó con bob!! tocó con bob!! - sopló como trombón -
Tocó son sonoro con los cocos - rock - pop - folk - pogo -
Nos contó como oyo todos los: oh, oh, oh, oh,...!!! -
Tocó con todos - por poco no toco con colón.
Coloso, stop, stop.

Otto orozco: con otros rollos - con poco protocolo - copó todo como los born -
Troncoso don floro o los lococo - logró otro confort - ojo por ojo -
Controló todo - convocó por fono los otros orozco - cortó con todos -
Cobró todos los bonos bocon - colocó montos gorsos por boston -
Cobró dos lotos - compró dos ford - ocho volvo - dos gol - oro -
Motos - toros - compró los coto - rodó - coconor.
Zorro, stop, stop.

Pololo orozco: gordo fofo con olor - mormóm - glotón con jopo -
Rostro poroso - rotoso - roñoso - como con motor roto - sólo como croto -
Sólo como topo - sólo como don bosco con poncho.
Choto, stop, stop.

Nosotros no somos como los orozco,
Yo los conozco, son ocho los monos:
Pocho, toto, cholo, tom, moncho, rodolfo, otto, pololo.
Yo pongo los votos solo por rodolfo.
Los otros son locos. yo los conozco.
No los soporto, stop. stop."""
LETRAS_O =('o','O', 'Ó', 'ó', 'Ö', 'ö')

def cantidad_de_letras_o(letra):
    #recorremos con un ciclo todos los carateres de la letra si es una o
    cantidad = 0
    for c in letra:
        if c in LETRAS_O:
            cantidad += 1
    return cantidad
def main():
    cantidad = cantidad_de_letras_o(LETRA_OROZCO)
    print("Los orozco tienen", cantidad, "letras o")

main()

