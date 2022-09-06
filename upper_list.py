
def write():

    grid = ["aoesmentieauup",
    "ubbuqvaporeonc",
    "uhslluaipepeoh",
    "lvcoreihafawoa",
    "njpalusreatear",
    "ioofkbaptwtesm",
    "vaellizselrvaa",
    "yanrtapmaoeetn",
    "seljbercsbneud",
    "adohhmoeteltce",
    "ueeoesunotrurr",
    "rtouokiarninbl",
    "hhcharizardsoi",
    "hoetovoeinchet"]

    f = open("pokemon_names.dic", "x",)
    for l in grid:
        f.write(l.upper()+('\n'))

write()
