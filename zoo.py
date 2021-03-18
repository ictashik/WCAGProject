from wcag_zoo.validators.anteater import Anteater
from wcag_zoo.validators.ayeaye import Ayeaye
from wcag_zoo.validators.glowworm import Glowworm
from wcag_zoo.validators.molerat import Molerat


with open("test.html", "r", encoding='utf-8') as f:
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


print("\n\nAnteater: Images : \n",ra)
print("\n\nAyeaye: Access Keys  \n",rb)
print("\n\nGlowworm: Focus Outlines \n",rc)
print("\n\nMolerat: Color Contrast \n",rd)
