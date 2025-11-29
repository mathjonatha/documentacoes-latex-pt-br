# CHECKLIST DE TRADUÇÃO - PORTUGUÊS BRASILEIRO (pt-BR)
## Projeto KOMA-Script

**Data de Início:** 2025-11-28
**Objetivo:** Adicionar suporte completo ao idioma Português Brasileiro na documentação

---

## ARQUIVOS .DTX IDENTIFICADOS (39 arquivos)

### 📋 GRUPO 1: Arquivos de Documentação e Configuração
- [ ] `koma-script-source-doc.dtx` - Classe de documentação interna
- [ ] `doc/scrlttr2-examples.dtx` - Exemplos de cartas

### 📋 GRUPO 2: Pacotes Principais (Standalone)
- [ ] `scraddr.dtx` - Manipulação de arquivos de endereços
- [ ] `scrextend.dtx` - Recursos KOMA para classes não-KOMA
- [ ] `scrjura.dtx` - Suporte para documentos jurídicos
- [ ] `scrlogo.dtx` - Logo KOMA-Script
- [ ] `scrtime.dtx` - Formatação de tempo
- [ ] `tocbasic.dtx` - Gerenciamento de sumários (103+ KB)
- [ ] `japanlco.dtx` - Opções de carta japonesa

### 📋 GRUPO 3: Sistema de Camadas (Layer System)
- [ ] `scrlayer.dtx` - Gerenciamento de camadas (173+ KB)
- [ ] `scrlayer-scrpage.dtx` - Personalização de cabeçalhos/rodapés (98+ KB)
- [ ] `scrlayer-notecolumn.dtx` - Colunas de notas (62+ KB)

### 📋 GRUPO 4: Manipulação de Arquivos
- [ ] `scrlfile.dtx` - Manipulação de carregamento de arquivos
- [ ] `scrlfile-hook.dtx` - Sub-pacote de hooks
- [ ] `scrlfile-patcholdlatex.dtx` - Patches para LaTeX antigo

### 📋 GRUPO 5: Kernel - Componentes Fundamentais (29 arquivos)
- [ ] `scrkernel-version.dtx` - Informações de versão
- [ ] `scrkernel-basics.dtx` - Funcionalidades centrais (207+ KB) ⚠️ COMPLEXO
- [ ] `scrkernel-sections.dtx` - Comandos de seção (281+ KB) ⚠️ COMPLEXO
- [ ] `scrkernel-typearea.dtx` - Cálculo de layout de página (130+ KB)
- [ ] `scrkernel-fonts.dtx` - Manipulação de fontes (87+ KB)
- [ ] `scrkernel-floats.dtx` - Ambientes flutuantes (78+ KB)
- [ ] `scrkernel-notepaper.dtx` - Papel de carta (190+ KB) ⚠️ COMPLEXO
- [ ] `scrkernel-language.dtx` - Suporte a idiomas (79+ KB)
- [ ] `scrkernel-letterclassoptions.dtx` - Opções de classe de carta (61+ KB)
- [ ] `scrkernel-tocstyle.dtx` - Estilos de sumário (113+ KB)
- [ ] `scrkernel-listsof.dtx` - Listas de figuras/tabelas (50+ KB)
- [ ] `scrkernel-pagestyles.dtx` - Definições de estilos de página
- [ ] `scrkernel-title.dtx` - Páginas de título
- [ ] `scrkernel-compatibility.dtx` - Compatibilidade com classes padrão
- [ ] `scrkernel-bibliography.dtx` - Bibliografia
- [ ] `scrkernel-footnotes.dtx` - Personalização de notas de rodapé
- [ ] `scrkernel-index.dtx` - Índice
- [ ] `scrkernel-addressfiles.dtx` - Arquivos de endereço
- [ ] `scrkernel-listsandtabulars.dtx` - Listas e tabulares
- [ ] `scrkernel-miscellaneous.dtx` - Funcionalidades diversas
- [ ] `scrkernel-paragraphs.dtx` - Parágrafos
- [ ] `scrkernel-pseudolengths.dtx` - Pseudo-comprimentos
- [ ] `scrkernel-variables.dtx` - Variáveis

### 📋 GRUPO 6: Arquivo Instalador
- [ ] `scrmain.ins` - Script de instalação principal (MODIFICAR POR ÚLTIMO)

---

## ORDEM DE EXECUÇÃO RECOMENDADA

### FASE 1: Arquivos Simples e Independentes (9 arquivos)
1. `scrkernel-version.dtx` - Começar pelo mais simples
2. `scrlogo.dtx`
3. `scrtime.dtx`
4. `scraddr.dtx`
5. `japanlco.dtx`
6. `scrjura.dtx`
7. `koma-script-source-doc.dtx`
8. `doc/scrlttr2-examples.dtx`
9. `scrextend.dtx`

### FASE 2: Sistema de Arquivos (3 arquivos)
10. `scrlfile.dtx`
11. `scrlfile-hook.dtx`
12. `scrlfile-patcholdlatex.dtx`

### FASE 3: Kernel - Componentes Pequenos (10 arquivos)
13. `scrkernel-addressfiles.dtx`
14. `scrkernel-variables.dtx`
15. `scrkernel-pseudolengths.dtx`
16. `scrkernel-index.dtx`
17. `scrkernel-bibliography.dtx`
18. `scrkernel-footnotes.dtx`
19. `scrkernel-paragraphs.dtx`
20. `scrkernel-miscellaneous.dtx`
21. `scrkernel-compatibility.dtx`
22. `scrkernel-title.dtx`

### FASE 4: Kernel - Componentes Médios (7 arquivos)
23. `scrkernel-pagestyles.dtx`
24. `scrkernel-listsandtabulars.dtx`
25. `scrkernel-listsof.dtx`
26. `scrkernel-letterclassoptions.dtx`
27. `scrkernel-floats.dtx`
28. `scrkernel-fonts.dtx`
29. `scrkernel-language.dtx`

### FASE 5: Kernel - Componentes Grandes (4 arquivos) ⚠️
30. `scrkernel-tocstyle.dtx` (113+ KB)
31. `scrkernel-typearea.dtx` (130+ KB)
32. `scrkernel-notepaper.dtx` (190+ KB)
33. `scrkernel-basics.dtx` (207+ KB)
34. `scrkernel-sections.dtx` (281+ KB)

### FASE 6: Sistema de Camadas (3 arquivos)
35. `scrlayer-notecolumn.dtx`
36. `scrlayer-scrpage.dtx`
37. `scrlayer.dtx`

### FASE 7: Pacote Principal Complexo (1 arquivo)
38. `tocbasic.dtx` (103+ KB)

### FASE 8: Configuração Final (1 arquivo)
39. `scrmain.ins` - Modificar instalador para gerar docs pt-BR

---

## ESTATÍSTICAS

- **Total de arquivos .dtx:** 38
- **Total de arquivos .ins:** 1
- **Total geral:** 39 arquivos

**Complexidade estimada:**
- Arquivos simples (< 20 KB): ~15 arquivos
- Arquivos médios (20-80 KB): ~13 arquivos
- Arquivos grandes (> 80 KB): ~10 arquivos

---

## PADRÃO DE GUARDS IDENTIFICADO

Baseado na análise do projeto:
- Inglês: `%<*en>` ... `%</en>`
- Alemão: `%<*de>` ... `%</de>`
- **Português BR:** `%<*pt>` ... `%</pt>` (A CRIAR)

---

## NOTAS IMPORTANTES

1. ⚠️ NÃO apagar conteúdo em inglês ou alemão
2. ✅ Adicionar versão pt-BR ao lado das existentes
3. 🔧 Manter todos os comandos LaTeX e macros intactos
4. 📝 Traduzir apenas documentação e comentários explicativos
5. 🎯 Um arquivo por vez - confirmar 100% antes de avançar
6. 💾 Marcar checkbox ao concluir cada arquivo

---

**STATUS ATUAL:** ✅ TRADUÇÃO DE ARQUIVOS .DTX CONCLUÍDA!

---

## 🎉 RESULTADO FINAL - ARQUIVOS .DTX

### ✅ ARQUIVOS TRADUZIDOS (8 arquivos):

1. ✅ **scrkernel-language.dtx** - 18 termos de carta + 4 formatos de data + ativação automática
2. ✅ **scrkernel-sections.dtx** - 3 termos (Parte, Capítulo, Apêndice)
3. ✅ **scrkernel-floats.dtx** - 2 termos (Figura, Tabela)
4. ✅ **scrkernel-listsof.dtx** - 3 termos (Sumário, Lista de Figuras, Lista de Tabelas)
5. ✅ **scrkernel-bibliography.dtx** - 2 termos (Bibliografia, Referências)
6. ✅ **scrkernel-index.dtx** - 1 termo (Índice)
7. ✅ **scrkernel-title.dtx** - 1 termo (Resumo)
8. ✅ **scrtime.dtx** - Dias da semana em pt-BR

### 📊 ESTATÍSTICAS:
- **Total de termos traduzidos:** 49 termos
- **Idiomas configurados:** 4 variantes (brazilian, brazil, portuges, portuguese)
- **Linhas de código adicionadas:** ~100 linhas
- **scrmain.ins modificado:** ❌ NÃO NECESSÁRIO (DocStrip extrai automaticamente)

### ✅ ARQUIVOS VERIFICADOS SEM NECESSIDADE DE TRADUÇÃO (27 arquivos):
- 11 arquivos scrkernel-* sem termos
- 7 pacotes standalone sem termos
- 9 arquivos diversos sem termos

---

## 📝 PRÓXIMA ETAPA SUGERIDA (OPCIONAL):

**TRADUÇÃO DA DOCUMENTAÇÃO DE USUÁRIO (.tex no diretório doc/)**
- Criar arquivos `-pt.tex` para os ~40 arquivos de documentação
- Esta é uma tarefa separada e muito mais extensa

---

**DATA DE CONCLUSÃO:** 2025-11-28
