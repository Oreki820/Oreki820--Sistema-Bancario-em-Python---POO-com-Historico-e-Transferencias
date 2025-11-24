# 💳 Sistema Bancário em Python - POO

Este é um **sistema bancário completo em Python**, desenvolvido como projeto de portfólio.  
Ele foi implementado utilizando **Programação Orientada a Objetos (POO)**, permitindo gerenciar usuários, contas, depósitos, saques, transferências e extratos detalhados com histórico de movimentações.

---

## ⚡ Funcionalidades

- Criação de **usuários** com CPF, nome, data de nascimento e endereço.
- Criação de **contas bancárias** vinculadas a usuários.
- Realização de **depósitos** com registro no extrato.
- Realização de **saques** com limite diário e validações.
- **Transferências** entre contas com registro no extrato de ambas.
- **Extrato detalhado**, incluindo todas as movimentações com data e hora.
- **Validação** de CPF e número da conta para todas as operações.
- Mensagens de erro e sucesso claras para o usuário.
- Sistema modular e preparado para futuras melhorias.

---

## 📂 Estrutura do Repositório

```

├── main.py        # Código principal do sistema bancário
└── README.md      # Este arquivo explicativo

````

> Observação: todo o sistema roda via terminal, interativo, não requer instalação de bibliotecas externas além do Python 3.x.

---

## 🛠 Como utilizar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
````

2. Entre na pasta do projeto:

```bash
cd nome-do-repositorio
```

3. Execute o sistema:

```bash
python main.py
```

4. Siga o menu interativo:

* `[nu]` - Criar novo usuário
* `[nc]` - Criar nova conta
* `[d]` - Depositar
* `[s]` - Sacar
* `[t]` - Transferir entre contas
* `[e]` - Extrato detalhado
* `[lc]` - Listar contas
* `[q]` - Sair do sistema

---

## 📈 Exemplo de Uso

```
================ MENU ================
[d] Depositar
[s] Sacar
[t] Transferir
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
=> nu
Informe o CPF (somente números): 12345678900
Informe o nome completo: João Silva
Informe a data de nascimento (dd-mm-aaaa): 01-01-1990
Informe o endereço (logradouro, nro - bairro - cidade/UF): Rua A, 123 - Centro - Cidade/UF
=== Usuário criado com sucesso! ===
```

---

## 💡 Tecnologias utilizadas

* **Python 3.x**
* Programação Orientada a Objetos (POO)
* Manipulação de listas e objetos
* Estruturas de decisão e loops

---

## 🚀 Próximos passos

* Adicionar **tipos de conta** (Corrente, Poupança, Premium)
* Persistência de dados usando **JSON ou SQLite**
* Interface gráfica com **Tkinter ou PySimpleGUI**
* Relatórios avançados e estatísticas de movimentações

---

## 📌 Autor

Lucas Gabriel Ferreira Gomes
[LinkedIn](www.linkedin.com/in/lucas-gabriel-dados) | [GitHub](https://github.com/Oreki820)

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações
