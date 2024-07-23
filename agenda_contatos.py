class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

    def __str__(self):
        status_favorito = "Favorito" if self.favorito else "Não Favorito"
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, Status: {status_favorito}"


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email, favorito=False):
        contato = Contato(nome, telefone, email, favorito)
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def visualizar_contatos(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for i, contato in enumerate(self.contatos, start=1):
                print(f"{i}. {contato}")

    def editar_contato(self, index, nome=None, telefone=None, email=None, favorito=None):
        if 0 <= index < len(self.contatos):
            contato = self.contatos[index]
            if nome is not None:
                contato.nome = nome
            if telefone is not None:
                contato.telefone = telefone
            if email is not None:
                contato.email = email
            if favorito is not None:
                contato.favorito = favorito
            print("Contato editado com sucesso!")
        else:
            print("Índice inválido.")

    def marcar_desmarcar_favorito(self, index):
        if 0 <= index < len(self.contatos):
            contato = self.contatos[index]
            contato.favorito = not contato.favorito
            status = "marcado" if contato.favorito else "desmarcado"
            print(f"Contato {status} como favorito!")
        else:
            print("Índice inválido.")

    def listar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if not favoritos:
            print("Nenhum contato favorito.")
        else:
            for i, contato in enumerate(favoritos, start=1):
                print(f"{i}. {contato}")

    def apagar_contato(self, index):
        if 0 <= index < len(self.contatos):
            self.contatos.pop(index)
            print("Contato apagado com sucesso!")
        else:
            print("Índice inválido.")


def obter_entrada(mensagem, tipo=str, obrigatorio=True):
    while True:
        try:
            entrada = input(mensagem)
            if not entrada and obrigatorio:
                raise ValueError("Entrada obrigatória")
            return tipo(entrada)
        except ValueError as e:
            print(f"Entrada inválida: {e}")


def menu():
    agenda = Agenda()

    while True:
        print("\nAgenda de Contatos")
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Editar Contato")
        print("4. Marcar/Desmarcar Favorito")
        print("5. Listar Favoritos")
        print("6. Apagar Contato")
        print("7. Sair")
        
        escolha = obter_entrada("Escolha uma opção: ", int)

        if escolha == 1:
            nome = obter_entrada("Nome: ")
            telefone = obter_entrada("Telefone: ")
            email = obter_entrada("Email: ")
            favorito = obter_entrada("Favorito? (s/n): ", str, obrigatorio=False).lower() == 's'
            agenda.adicionar_contato(nome, telefone, email, favorito)
        elif escolha == 2:
            agenda.visualizar_contatos()
        elif escolha == 3:
            agenda.visualizar_contatos()
            index = obter_entrada("Escolha o índice do contato para editar: ", int) - 1
            nome = obter_entrada("Novo Nome (ou deixe em branco para manter): ", str, obrigatorio=False)
            telefone = obter_entrada("Novo Telefone (ou deixe em branco para manter): ", str, obrigatorio=False)
            email = obter_entrada("Novo Email (ou deixe em branco para manter): ", str, obrigatorio=False)
            favorito = obter_entrada("Favorito? (s/n ou deixe em branco para manter): ", str, obrigatorio=False)
            favorito = favorito.lower() == 's' if favorito else None
            agenda.editar_contato(index, nome if nome else None, telefone if telefone else None, email if email else None, favorito)
        elif escolha == 4:
            agenda.visualizar_contatos()
            index = obter_entrada("Escolha o índice do contato para marcar/desmarcar favorito: ", int) - 1
            agenda.marcar_desmarcar_favorito(index)
        elif escolha == 5:
            agenda.listar_favoritos()
        elif escolha == 6:
            agenda.visualizar_contatos()
            index = obter_entrada("Escolha o índice do contato para apagar: ", int) - 1
            agenda.apagar_contato(index)
        elif escolha == 7:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
