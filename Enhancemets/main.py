import dimensionEqualizer
import synonymPair

def main():

    string1 = "Your dog is pretty"
    string2 = "Your cat is a beautiful cat"

    string1, string2 = string1.split(), string2.split()

    string1, string2 = synonymPair.getSynonyms(string1, string2)
    string1, string2 = dimensionEqualizer.equalizeDimensions(string1, string2)

    print(string1, string2)


if __name__ == "__main__":
    main()
