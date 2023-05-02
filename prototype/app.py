from models import ElegantPant

elegant_pant = ElegantPant("Yellow", "Velvet", "Frida Giannini", "Gucci")

elegant_pant_2 = elegant_pant.clone()
elegant_pant_2.color = "Red"

print(
    f"Elegant pant color #1: {elegant_pant.color}",
    f"Elegant pant color #2: {elegant_pant_2.color}",
    sep="\n",
)

print(
    f"Elegant pant memory id #1 {id(elegant_pant)}",
    f"Elegant pant memory id #2 {id(elegant_pant_2)}",
    sep="\n",
)
