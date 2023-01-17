menu = ('스테이크', 50000)
VAT = 0.15
print(f"{menu[0]}  {menu[1]:,}")
print(f"+ VAT      {int(menu[1] * VAT):,}")
print(f"총계 ₩    {int(round(menu[1] *(1+VAT))):,}")
