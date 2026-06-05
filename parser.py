import gdstk

def parser(file):
    """Parse a GDSII file and return a list of gdstk.Cell objects."""
    return gdstk.read_gds(file)

out = parser("u_s_r.magic.gds")

print(type(out))