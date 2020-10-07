from test_postitoimipaikka import hae_postinumerot

def inputptp():
    etsittava = input('Kirjoita postitoimipaikka: ').strip().upper()
    return etsittava

def luo_lista():
    postinumerot = hae_postinumerot()

    toimipaikat_ja_numerot = {}

    for numero, toimipaikka in postinumerot.items():
        if toimipaikka in toimipaikat_ja_numerot:
            toimipaikat_ja_numerot[toimipaikka].append(numero)
        else:
            toimipaikat_ja_numerot[toimipaikka] = [numero]
    
    return toimipaikat_ja_numerot

'''Testaa toteuttamasi logiikka ainakin tapauksissa, joissa:

annettua nimeä ei löydy lainkaan aineistosta
postitoimipaikan nimellä löytyy yksi postinumero
postitoimipaikan nimellä löytyy useita postinumeroita'''

def etsi(etsittava, toimipaikat_ja_numerot):

    if etsittava in toimipaikat_ja_numerot:
        loydetyt = toimipaikat_ja_numerot[etsittava]
        return loydetyt
    else:
        return False


def test_etsi_nolla():

    etsittava = 'ZSLNISDGPN'

    toimipaikat_ja_numerot = luo_lista()
    
    loydetut = etsi(etsittava, toimipaikat_ja_numerot)
    
    assert loydetut == False

def test_etsi_yksi():

    etsittava = 'MUTALA'

    toimipaikat_ja_numerot = luo_lista()
    
    loydetut = etsi(etsittava, toimipaikat_ja_numerot)

    assert len(loydetut) == 1

def test_etsi_monta():

    etsittava = 'HELSINKI'

    toimipaikat_ja_numerot = luo_lista()
    
    loydetut = etsi(etsittava, toimipaikat_ja_numerot)

    assert len(loydetut) > 1

def tulostus(loydetyt):
    if loydetyt == False:
        print('Postitoimipaikkaa ei löytynyt :(')
    else:
        print('Postinumerot: ' + ', '.join(loydetyt))

def main():

    toimipaikat_ja_numerot = luo_lista()

    etsittava = inputptp()

    loydetyt = etsi(etsittava, toimipaikat_ja_numerot)

    tulostus(loydetyt)


if __name__ == '__main__':
    main()