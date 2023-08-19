from decimal import Decimal
total_kcal = 0
COST_PER_KCAL = 0.32541

KCAL_OF_RABBIT = 197
KCAL_OF_OSTRICH_EGG = 118
KCAL_OF_SEABASS = 123
KCAL_OF_SWEET_RED_PEPPERS = 26
KCAL_OF_PARSLEY = 45
KCAL_OF_BANANAS = 87
KCAL_OF_WAFFLES = 425
KCAL_OF_WHEAT_BREAD_MADE_OF_FIRST_GRADE_FLOUR = 246
KCAL_OF_PISTACHIOS = 555
KCAL_OF_KEFIR = 51

product_portion_rabbit = input('Enter your product portion of the rabbit >>>')
quantity = int(product_portion_rabbit)
kcal_of_rabbit = KCAL_OF_RABBIT * quantity / 100
total_kcal += kcal_of_rabbit
print(f'kcal_of_rabbit {kcal_of_rabbit}')
print(f'total_kcal {total_kcal}')

product_portion_ostrich_egg = input('Enter your product portion of the ostrich egg >>>')
quantity2 = int(product_portion_ostrich_egg)
kcal_of_ostrich_egg = KCAL_OF_OSTRICH_EGG * quantity2 / 100
total_kcal += kcal_of_ostrich_egg
print(f'kcal_of_ostrich_egg {kcal_of_ostrich_egg}')
print(f'total_kcal {total_kcal}')

product_portion_seabass = input('Enter your product portion seabass >>>')
quantity3 = int(product_portion_seabass)
kcal_of_seabass = KCAL_OF_SEABASS * quantity3 / 100
total_kcal += kcal_of_seabass
print(f'kcal_of_seabass {kcal_of_seabass}')
print(f'total_kcal {total_kcal}')

product_portion_sweet_red_peppers = input('Enter your product portion red peppers >>>')
quantity4 = int(product_portion_sweet_red_peppers)
kcal_of_sweet_red_peppers = KCAL_OF_SWEET_RED_PEPPERS * quantity4 / 100
total_kcal += kcal_of_sweet_red_peppers
print(f'kcal_of_sweet_red_peppers {kcal_of_sweet_red_peppers}')
print(f'total_kcal {total_kcal}')

product_portion_parsley = input('Enter your product portion parsley >>>')
quantity5 = int(product_portion_parsley)
kcal_of_parsley = KCAL_OF_PARSLEY * quantity5 / 100
total_kcal += kcal_of_parsley
print(f'kcal_of_parsley {kcal_of_parsley}')
print(f'total_kcal {total_kcal}')

product_portion_bananas = input('Enter your product portion bananas >>>')
quantity6 = int(product_portion_bananas)
kcal_of_bananas = KCAL_OF_BANANAS * quantity6 / 100
total_kcal += kcal_of_bananas
print(f'kcal_of_bananas {kcal_of_bananas}')
print(f'total_kcal {total_kcal}')

product_portion_waffels = input('Enter your product portion waffels >>>')
quantity7 = int(product_portion_waffels)
kcal_of_waffles = KCAL_OF_WAFFLES * quantity7 / 100
total_kcal += kcal_of_waffles
print(f'kcal_of_waffles {kcal_of_waffles}')
print(f'total_kcal {total_kcal}')

product_portion_wheat_bread_made_of_frist_grade_flour = input('Enter your product portion wheat bread made of frist grade flour >>>')
quantity8 = int(product_portion_wheat_bread_made_of_frist_grade_flour)
kcal_of_wheat_bread_made_of_frist_grade_flour = KCAL_OF_WHEAT_BREAD_MADE_OF_FIRST_GRADE_FLOUR * quantity8 / 100
total_kcal += kcal_of_wheat_bread_made_of_frist_grade_flour
print(f'kcal_of_wheat_bread_made_of_frist_grade_flour {kcal_of_wheat_bread_made_of_frist_grade_flour}')
print(f'total_kcal {total_kcal}')

product_portion_pistachios = input('Enter your product portion pistachios >>>')
quantity9 = int(product_portion_pistachios)
kcal_of_pistachios = KCAL_OF_PISTACHIOS * quantity9 / 100
total_kcal += kcal_of_pistachios
print(f'kcal_of_pistachios {kcal_of_pistachios}')
print(f'total_kcal {total_kcal}')

product_portion_kefir = input('Enter your product portion kefir >>>')
quantity10 = int(product_portion_kefir)
kcal_of_kefir = KCAL_OF_KEFIR * quantity10 / 100
total_kcal += kcal_of_kefir
print(f'kcal_of_kefir {kcal_of_kefir}')
print(f'total_kcal {total_kcal}')

cost = total_kcal * COST_PER_KCAL
rounded_cost = round(cost, 2)

price = Decimal(str(rounded_cost)).quantize(Decimal('0.01'))
print(f'total:{price}')

if total_kcal<1000:
    print('i am hungry')

elif total_kcal<1500:
    print('i am ')
else:
    print('westen mein')
