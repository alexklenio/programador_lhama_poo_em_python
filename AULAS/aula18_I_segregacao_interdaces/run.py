from abc import ABC,abstractmethod

class Trabalhador(ABC): #Interface

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

    @abstractmethod
    def consultar_beneficios(self) -> None: pass

class TrabalhadorTemporario(ABC): #Interface

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

   

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print(f"O professor está dando aula.")

    def ir_para_casa(self) -> None:
        print(f"O professor está indo para casa.")

    def consultar_beneficios(self) -> None:
        print(f"Consultando benefícios da CLT.")

class ProfessorSubstituto(TrabalhadorTemporario):
    def trabalhar(self) -> None:
        print(f"O professor substituto está dando aula.")

    def ir_para_casa(self) -> None:
        print(f"O professor substituto está indo para casa.")
        
  
    
p2 = ProfessorSubstituto()
