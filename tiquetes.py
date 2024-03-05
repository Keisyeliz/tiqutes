nombreStr = input('Nombre del usuario -> ')
presupuestoFlt = float(input('Monto -> '))
var_opcionStr = int(input('<<<MENÚ DE OPCIONE>>>\n\n1. Vip\n2. Turista\n3. Economico\n ->')) 

if  var_opcionStr == 1:
    descFlt = presupuestoFlt * 0.05
    valor_tiqueteInt = presupuestoFlt - descFlt

if var_opcionStr == 2:
    descFlt = presupuestoFlt * 0.10
    valor_tiqueteInt = presupuestoFlt - descFlt

if var_opcionStr == 3:
    descFlt = presupuestoFlt * 0.15
    valor_compradoInt = presupuestoFlt - descFlt


print('Nombre del usuario:',nombreStr)
print('Descuento aplicado:''$',descFlt)
print('Valor total a pagar es de:'' $',valor_tiqueteInt)
