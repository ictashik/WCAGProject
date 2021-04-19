from wcag_zoo.validators.anteater import Anteater
from wcag_zoo.validators.ayeaye import Ayeaye
from wcag_zoo.validators.glowworm import Glowworm
from wcag_zoo.validators.molerat import Molerat
from wcag_zoo.validators.anteater import Anteater
import automated_accessibility_testing

filename ="colortest.html"

with open(filename, "r", encoding='utf-8') as f:
    text= f.read()

my_html = b'text'
a = Anteater()
b = Ayeaye()
c = Glowworm()
d = Molerat()

ra = a.validate_document(my_html)
rb = b.validate_document(my_html)
rc = c.validate_document(my_html)
rd = d.validate_document(my_html)

print("\nValidating ", filename, "...")

print("\t\t\t\t\t SUCC \t\t FAIL \t\t WARN \t\t SKIP")

print("\nAnteater: Images :     \t",end = "\t\t  ")
for each in ra:
    i = 0
    for item in ra[each]:
        if len(item) > 0:
            i =i +1
    print(i,end = "\t\t")

print("\nAyeaye: Access Keys :     \t",end = "\t  ")
for each in rb:
    i = 0
    for item in rb[each]:
        if len(item) > 0:
            i =i +1
    print(i,end = "\t\t")
print("\nGlowworm: Focus Outlines:  \t",end = "\t  ")
for each in rc:
    i = 0
    for item in rc[each]:
        if len(item) > 0:
            i =i +1
    print(i,end = "\t\t")
print("\nMolerat: Color Contrast :\t",end = "\t  ")
for each in rd:
    i = 0
    for item in rd[each]:
        if len(item) > 0:
            i =i +1
    print(i,end = "\t\t")


print((automated_accessibility_testing.check_accessibility(text)))
