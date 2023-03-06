#Nomes: Jefferson Messias da Silva, Rafael Nascimento Oliveira

from abc import ABC, abstractmethod

class Portaria(ABC):
    @abstractmethod
    def entrar(self, nome):
        pass
class Aluno(Portaria):
    def entrar(self, nome):
        return f"{nome} tem relação com a instituição como Aluno"
class Professor(Portaria):
    def entrar(self, nome): 
        return f"{nome} tem relação com a instituição como Professor"
class Coordenador(Portaria):
    def entrar(self, nome): 
        return f"{nome} tem relação com a instituição como Coordenador"
class Diretor(Portaria): 
    def entrar(self, nome): 
        return f"{nome} tem relação com a instituição como Diretor"
class Administrativo(Portaria): 
    def entrar(self, nome): 
        return f"{nome} tem relação com a instituição como Administrativo"

class FabricaRelacao: 
    def criar_relacao(self,relacao,nome): 
        if(relacao == "1"): 
            return Aluno() 
        elif(relacao == "2"): 
            return Professor() 
        elif(relacao=="3"): 
            return Coordenador() 
        elif(relacao=="4"): 
            return Diretor() 
        elif(relacao=="5"): 
            return Administrativo() 

sair="a"
while(sair!="q"):
    
    cria_entrada=FabricaRelacao()
    nome=input("Entre com o seu nome: ")
    valor=input("Qual a sua relação com a FATEC: \n1-Aluno\n2-Professor\n3-Coordenador\n4-Diretor\n5-Coordenador\n6-Sem relação\n ")
   
    relacao=cria_entrada.criar_relacao(valor,nome)
    if(valor=="6"):
        print(nome, " não tem nenhuma relação com a instituição, acompanhar até a secretaria")
    elif(valor=="1" or valor=="2" or valor=="3" or valor=="4" or valor=="5"):    
        print(relacao.entrar(nome))
    else:
        print("Entrada invalida!")    
    sair=input("digite q para sair ou outra tecla para continuar: ")
