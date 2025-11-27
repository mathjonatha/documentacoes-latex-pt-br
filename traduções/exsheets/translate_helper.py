# -*- coding: utf-8 -*-
"""
Helper script to translate exsheets_en.tex to Brazilian Portuguese
This script provides translation mappings for common phrases and sections.
"""

# Translation dictionary for common phrases and section titles
translations = {
    # Section titles
    "General Options": "Opções Gerais",
    "Create Questions/Exercises and their Solutions": "Criar Questões/Exercícios e suas Soluções",
    "The \\env*{question} Environment": "O Ambiente \\env*{question}",
    "Options to the \\env*{question} Environment": "Opções para o Ambiente \\env*{question}",
    "Subtitles to Questions": "Subtítulos para Questões",
    "The \\env*{solution} Environment": "O Ambiente \\env*{solution}",
    "Options to the \\env*{solution} Environment": "Opções para o Ambiente \\env*{solution}",
    "Setting the Counter": "Configurando o Contador",
    "Language Settings": "Configurações de Idioma",
    "Counting Points": "Contando Pontos",
    "The Commands": "Os Comandos",
    "Options": "Opções",
    "Printing Solutions": "Imprimindo Soluções",
    "Print all": "Imprimir todas",
    "Print per chapter/section": "Imprimir por capítulo/seção",
    "Conditional Printing of Questions": "Impressão Condicional de Questões",
    "Using Classes": "Usando Classes",
    "Using Topics": "Usando Tópicos",
    "Own Dividing Concepts": "Conceitos Próprios de Divisão",
    "Retrieving the Class Value in a Question": "Recuperando o Valor da Classe em uma Questão",
    "Tagging Questions": "Marcando Questões",
    "Question Properties -- the Basics": "Propriedades de Questões -- o Básico",
    "Pre-defined Properties": "Propriedades Pré-definidas",
    "Advanced Usage": "Uso Avançado",
    "Variations of an Exam": "Variações de uma Prova",
    "A Grade Distribution": "Uma Distribuição de Notas",
    "Selectively Include Questions from External Files": "Incluir Seletivamente Questões de Arquivos Externos",
    "Caveat": "Advertência",
    "How it works": "Como funciona",
    "Own Question/Solution Pairs": "Pares Questão/Solução Próprios",
    "Filling in the Blanks": "Preenchendo os Espaços em Branco",
    "Cloze": "Lacuna",
    "Vertical Space for answers": "Espaço Vertical para respostas",
    "Styling your Exercise/Exam Sheets": "Estilizando suas Listas de Exercícios/Provas",
    "Background": "Contexto",
    "Available Options": "Opções Disponíveis",
    "Using an \\ExSheets{} Heading in Custom Code": "Usando um Cabeçalho \\ExSheets{} em Código Personalizado",
    "Load Custom Configurations": "Carregar Configurações Personalizadas",
    "The Problem": "O Problema",
    "The Proposed Solution": "A Solução Proposta",
    "Own Environments": "Ambientes Próprios",
    "Appendix": "Apêndice",
    "A List of all Solutions used in this Manual": "Uma Lista de todas as Soluções usadas neste Manual",

    # Common phrases
    "This is our very first very difficult to solve question!": "Esta é nossa primeira questão muito difícil de resolver!",
    "This is our first difficult question that is worth 3 points!": "Esta é nossa primeira questão difícil que vale 3 pontos!",
    "This question is worth 1 point and 1 bonus point.": "Esta questão vale 1 ponto e 1 ponto bônus.",
    "This question is a bonus question. It is worth 3 bonus points.": "Esta questão é uma questão bônus. Ela vale 3 pontos bônus.",
    "This question's points won't be added to the total sum.": "Os pontos desta questão não serão adicionados à soma total.",
    "This question has the type": "Esta questão tem o tipo",
    "The default name has changed from": "O nome padrão mudou de",
    "This question has a custom name.": "Esta questão tem um nome personalizado.",
    "This question is not printed.": "Esta questão não é impressa.",
    "Exercise": "Exercício",
    "Question": "Questão",
    "Solution": "Solução",
    "Fancy name": "Nome elegante",
}

print("Translation dictionary created. Use this to help with manual translations.")
print(f"Total phrases: {len(translations)}")
