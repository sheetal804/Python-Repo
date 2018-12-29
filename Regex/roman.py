x=r"(?:M|MM|MMM)?(?:C|CC|CCC|CD|D|DC|DCC|DCCC|CM)?(?:X|XX|XXX|XL|L|LX|LXX|LXXX|XC)?(?:I|II|III|IV|V|VI|VII|VIII|IX)?$"
import re

thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'

regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)

    # regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$" # You can also try with this.
