class persistencia():

    def main():
        arquivo = open(r"persist", "a")
        for i in range(100):
            arquivo.write("\n")

persistencia.main()