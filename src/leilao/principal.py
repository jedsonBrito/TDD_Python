from src.leilao.dominio import Usuario,Lance,Leilao

jedi = Usuario("Jedi")
sith = Usuario("Sith")

lance_do_sith = Lance(sith,100)
lance_do_jedi = Lance(jedi,150)

leilao_corruscant = Leilao("Celular")

leilao_corruscant.lances.append(lance_do_sith)
leilao_corruscant.lances.append(lance_do_jedi)


for lance in leilao_corruscant.lances:
    print(f'O Usuario {lance.usuario.nome} deu um lance de {lance.valor}')