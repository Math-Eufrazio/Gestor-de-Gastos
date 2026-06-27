# 💰 App de Finanças Pessoais

Sistema de gestão financeira que permite cadastrar despesas e ganhos, fazer relatórios, extrato e exportar o extrato para ser usado em outra máquina se necessário.

---

## 👤 Informações Relevantes
- **Aluno:** Matheus O. Eufrazio
- **Professor:** Jean Matias

---

## ⚙️ Como rodar

Pré-requisitos: Python 3 instalado, terminal aberto na pasta do projeto.

```bash
python financas.py
```

---

## 🗂️ Funcionalidades

- **[1] Registrar** — pede tipo, valor, categoria e descrição, valida as entradas e salva automaticamente
- **[2] Extrato** — lista todos os lançamentos com data, tipo, categoria e valor formatado
- **[3] Relatório** — exibe saldo total, total de receitas, total de despesas e total por categoria
- **[4] Exportar** — gera o arquivo `relatorio.txt` com o conteúdo do relatório
- **[5] Sair** — encerra o programa sem perda de dados

---

## 🔧 Funções implementadas

| Função | Responsabilidade |
|--------|-----------------|
| `carregar()` | Lê o `lancamentos.json` e retorna a lista. Se o arquivo não existir, retorna lista vazia |
| `salvar()` | Recebe a lista de lançamentos e grava no `lancamentos.json` |
| `registrar_lancamento()` | Pede tipo, valor, categoria e descrição ao usuário, valida cada entrada com `try/except` e salva após cada registro |
| `extrato()` | Carrega os lançamentos e exibe cada um formatado com data, tipo, categoria e valor |
| `relatorio()` | Calcula e exibe saldo total, total de receitas, total de despesas e totais agrupados por categoria |
| `exportar_relatorio()` | Gera o arquivo `relatorio.txt` com o mesmo conteúdo do relatório e a data de geração |

---

## 🛠️ Tecnologias usadas

| Tecnologia | Uso |
|------------|-----|
| `Python 3` | linguagem principal do projeto |
| `json` | salvar e carregar os lançamentos |
| `os` | verificar se o arquivo existe |
| `datetime` | registrar a data e hora de cada lançamento |

---

## 📁 Estrutura do repositório

| Arquivo | Descrição |
|---------|-----------|
| `financas.py` | programa principal |
| `lancamentos.json` | dados gerados pelo programa |
| `relatorio.txt` | exportado pelo programa |
| `README.md` | documentação do projeto |

---

## 📝 O que aprendi

Sobre dificuldades no projeto, minha principal foi definir as funções que interagiam com o dicionário de lançamentos, principalmente porque ainda não entendo por completo o uso de variáveis dentro de funções. Sobre o que ficou mais claro foi o uso do `try/except` para validar entradas do usuário. Se eu recomeçasse esse projeto, me empenharia em fazer um sistema de validação de usuário melhor do que o que tenho agora.