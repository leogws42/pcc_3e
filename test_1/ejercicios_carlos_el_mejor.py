invitacion =['Carlos','Maria','Paula']

print(f"TE INVITO A ALMORZAR QUERID@  {invitacion[0]}")
print(f"TE INVITO A ALMORZAR QUERID@  {invitacion[1]}")
print(f"TE INVITO A ALMORZAR QUERID@  {invitacion[2]}")

print(f"\nLa persona que no puede asistir es  {invitacion[0]}")

invitacion.append('Eduardo')

print(f"\nTE INVITO A ALMORZAR QUERID@  {invitacion[1]}")
print(f"TE INVITO A ALMORZAR QUERID@  {invitacion[2]}")
print(f"TE INVITO A ALMORZAR QUERID@  {invitacion[3]}")

print("\nEncontre una mesa mas grande")

invitacion.insert(0,'Leonardo')
invitacion.insert(2,'Juan')
invitacion.append('Cristian')


print(f"\nTE INVITO A ALMORZAR QUERID@  {invitacion[0]}")
print(f"TE INVITO A ALMORZAR QUERID@  {invitacion[1]}")
print(f"TE INVITO A ALMORZAR QUERID@  {invitacion[2]}")
print(f"TE INVITO A ALMORZAR QUERID@  {invitacion[3]}")
print(f"TE INVITO A ALMORZAR QUERID@  {invitacion[4]}")
print(f"TE INVITO A ALMORZAR QUERID@  {invitacion[5]}")

print("\nAhora solo puedes invitar 2 personas de tu lista que cagada :(")

return_value_1 = invitacion.pop()
print(f"\nLAMENTO DECIRTE QUE YA NO QUIERO CENAR CONTIGO {return_value_1}")
return_value_2 = invitacion.pop()
print(f"LAMENTO DECIRTE QUE YA NO QUIERO CENAR CONTIGO {return_value_2}")
return_value_3 = invitacion.pop()
print(f"LAMENTO DECIRTE QUE YA NO QUIERO CENAR CONTIGO {return_value_3}")
return_value_4 = invitacion.pop()
print(f"LAMENTO DECIRTE QUE YA NO QUIERO CENAR CONTIGO {return_value_4}")
return_value_5 = invitacion.pop()
print(f"LAMENTO DECIRTE QUE YA NO QUIERO CENAR CONTIGO {return_value_5}")


print(f"\nCONTIGO SI QUIERO CENAR QUERID@  {invitacion[0]}")
print(f"\nCONTIGO SI QUIERO CENAR QUERID@  {invitacion[1]}")

del invitacion[0]
del invitacion[0]

print(invitacion)