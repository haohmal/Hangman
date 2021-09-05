
def what_to_do(instructions):
    simon = "simon says"
    ido = "won't do it!"
    if instructions.lower().startswith(simon + ' '):
        ido = instructions[len(simon) + 1:]
    elif instructions.lower().endswith(' ' + simon):
        ido = instructions[0:len(instructions) - (len(simon) + 1)]
    if ido.lower().endswith(' ' + simon):
        ido = ido[0:len(ido) - (len(simon) + 1)]
    return "I " + ido