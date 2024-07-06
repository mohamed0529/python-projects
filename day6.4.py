#example
product="realme |c55 |11000 "
mobile=product[:product.index("|")]
model=product[product.index("|")+1:product.rindex("|")]
price=product[product.rindex("|")+1:]
print(mobile)
print(model)
print(price)