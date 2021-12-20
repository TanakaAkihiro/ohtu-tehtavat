from konsoli_io import KonsoliIO
from peli import Peli


def main():
    
    io = KonsoliIO

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus in "abc":
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

        if vastaus.endswith("a"):
            kaksinpeli = Peli.luo_kaksinpeli(io)
            kaksinpeli.pelaa()

        elif vastaus.endswith("b"):
            yksinpeli = Peli.luo_tekoaly_peli(io)
            yksinpeli.pelaa()

        elif vastaus.endswith("c"):
            haastava_yksinpeli = Peli.luo_parempi_tekoaly_peli(io)
            haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
