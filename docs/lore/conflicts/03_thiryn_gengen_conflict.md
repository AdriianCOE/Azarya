# Crise Thiryn–Gengen

*Ver `00_CANON_RULES.md`, `02_MASTER_TIMELINE.md` e `04_CONTENT_IMPLEMENTATION_MATRIX.md`.*

## Origem [CANON]

Thiryn (`THK`) perdeu uma guerra humilhante contra a recém-formada República de Gengen (`UPG`).

Perdeu:

| Região | Estado | Owner técnico atual |
|---|---:|---|
| Doia | 86 | UPG |
| Haifa | 400 | UPG |
| Mominches | 409 | UPG |

A população técnica combinada é **1.657.762**, descrita na lore como **aproximadamente 1,7 milhão de habitantes**.

Essas regiões são consideradas parte nacional de Thiryn.

## Consequências em Thiryn

- revanchismo;
- protestos;
- descrédito do Exército;
- perda de confiança na monarquia;
- crise de veteranos;
- refugiados;
- propaganda nacionalista;
- pressão pela reconstrução e reconquista.

O Grande Terremoto agrava a crise econômica e política.

## Situação de Gengen

Gengen é uma república jovem que precisa consolidar:

- fronteiras;
- Exército;
- legitimidade;
- administração dos territórios conquistados;
- relações com populações thirynianas;
- proteção contra revanche.

## Inclinação histórica [CANON]

Gengen tende inicialmente a aproximar-se de Gydian.

Motivos:

- medo de uma nova invasão thiryniana;
- dependência de armas e assessores;
- ajuda recebida anteriormente;
- crescimento de Zauern sob apoio gydiano;
- percepção de que a proteção imperial é necessária.

A natureza exata da ajuda gydiana durante a guerra anterior ainda pode ser detalhada, mas a aproximação política é canon.

## O jogo duplo gydiano [CANON]

Gydian tenta controlar os dois países.

### Para Gengen

Oferece:

- garantia;
- armas;
- assessores;
- crédito;
- bases;
- proteção diplomática.

Depois exige:

- presença militar em Haifa;
- acesso ferroviário em Doia;
- união econômica;
- alinhamento externo;
- redução de autonomia.

### Para Thiryn

Sugere que Mominches, Doia e Haifa podem ser devolvidas em troca de:

- adesão ao bloco gydiano;
- acesso militar;
- submissão econômica;
- apoio na Grande Guerra.

Gydian não pretende necessariamente cumprir integralmente nenhuma promessa.

## Conflitos de fronteira

A crise deve escalar por eventos recorrentes, sem iniciar guerra automaticamente.

### Incidentes possíveis

- patrulha capturada em Mominches;
- escolas thirynianas fechadas;
- marcha de refugiados em Doia;
- explosão ferroviária;
- contrabando de armas;
- confronto alfandegário em Haifa;
- exercícios militares;
- prisões de líderes comunitários;
- ataques de milícias;
- agentes gydianos provocando os dois lados.

Os nomes finais dos incidentes permanecem TBD.

## Mecânica recomendada

### Tensão fronteiriça

```text
az_thk_upg_border_tension
```

Faixa sugerida: `0–100`.

A tensão pode alterar:

- opinião;
- estabilidade;
- apoio de guerra;
- custo de decisões;
- risco de incidente grave;
- influência gydiana.

Ela não deve, sozinha, declarar guerra.

### Influência gydiana

```text
az_gye_influence_thk
az_gye_influence_upg
```

As duas variáveis devem poder crescer simultaneamente.

## Rota histórica provável [CANON]

Gengen entra ou aproxima-se fortemente do bloco gydiano antes da Grande Guerra.

Isso não determina automaticamente a escolha final de Thiryn.

## Caminhos possíveis [CANON]

### 1. Gengen com Gydian

Rota histórica provável.

Gengen aceita proteção e concessões, preservando temporariamente os territórios.

### 2. Thiryn com Gydian

Thiryn recebe promessa de reconquista e pode atacar Gengen ou exigir partilha.

### 3. Resistência conjunta

Thiryn e Gengen reconhecem que Gydian está usando os dois.

Podem suspender a disputa sem resolver definitivamente a soberania dos estados.

### 4. Neutralidade

Ambos evitam adesão direta, mantendo fronteira militarizada.

### 5. Nova guerra regional

A tensão ou a interferência externa causa nova guerra antes ou durante a Grande Guerra Continental.

## Relação com Great Thiryn

Os estados 86, 400 e 409 coincidem com a formação de Great Thiryn registrada em auditorias anteriores.

A ligação narrativa é forte, mas o wiring técnico precisa ser revalidado:

- quais focos realmente ativam a formação;
- quais estados são exigidos;
- qual evento ou notícia é disparado;
- se ainda existe uso indevido de `news.59`;
- se Great Thiryn representa apenas reconquista ou ambição maior.

Até essa inspeção, registrar como **CANON narrativo provável / IMPLEMENTAÇÃO A VALIDAR**.

## Testes obrigatórios

- população e IDs corretos;
- eventos não repetem;
- tensão não ultrapassa limites;
- guerra não inicia por acidente;
- influência cresce separadamente;
- Gengen histórico tende a Gydian;
- resistência conjunta funciona mesmo com claims ativos;
- Great Thiryn não dispara notícia vanilla;
- save/load preserva a crise.
