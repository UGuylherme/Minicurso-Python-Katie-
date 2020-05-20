nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
nota3 = float(input('Nota 3:'))
soma = nota1 + nota2 + nota3 / 3
media = soma // 3
if media >= 7:
    print('O aluno está aprovado')
if media >= 5 <7:
    print('O aluno está em recuperação')
if media < 5:
    print('O aluno está reprovado')