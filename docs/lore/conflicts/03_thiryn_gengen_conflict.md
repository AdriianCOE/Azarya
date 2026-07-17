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

**IMPLEMENTADO NESTA RODADA (lado THK apenas)**: variável real (`set_variable`/`add_to_variable`), inicializada em 10 pelo foco `THK_RevanchistSentiment` e incrementada por `THK_RefugeesFromTheWest` (+5), `THK_VeteransCommittees` (+3), `THK_MapsOfTheLostProvinces` (+10) e pela decisão repetível `THK_PatrolDoiaFrontier` (+2, a cada 30 dias). Nenhum efeito automático de guerra está ligado a essa variável ainda — ela apenas acumula, pronta para um sistema geopolítico futuro que a leia. Não existe hoje nenhum equivalente do lado UPG.

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

**`az_gye_influence_thk` IMPLEMENTADO NESTA RODADA**: definida em 25 pelo foco `THK_AcceptGydianPatronage` (mutuamente exclusivo com `THK_RejectGydianPatronage`, que não altera a variável e em vez disso concede a ideia `THK_Self_Reliance`). Esse é o dilema de Thiryn descrito no "jogo duplo gydiano" — aceitar reduz `political_power_factor` e `drift_defence_factor` (dependência), recusar favorece estabilidade e apoio de guerra (independência), coerente com "Gydian não deve ser retratado como aliado confiável".

`az_gye_influence_upg` continua **AUSENTE** — nenhum arquivo de UPG foi tocado nesta rodada, conforme escopo.

As duas variáveis devem poder crescer simultaneamente quando `az_gye_influence_upg` for implementado.

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

Os estados 86, 400 e 409 coincidem com a formação de Great Thiryn.

**IMPLEMENTADO E VALIDADO NESTA RODADA** — o wiring técnico foi auditado e corrigido:

- a formação é ativada apenas pela decisão `form_Great_Thiryn` (`common/decisions/formable_nation_decisions.txt`), nunca por um foco isoladamente — nenhum foco novo do lado THK duplica esse efeito;
- os estados exigidos continuam sendo exatamente 86, 400 e 409 (`controls_state`), mais `is_subject = no`;
- a decisão agora também exige `has_completed_focus = THK_TowardGreatThiryn` (novo foco final do ramo "The Lost Border" em `common/national_focus/Thiryn.txt`) e `has_stability > 0.4`, amarrando a formação à conclusão de uma rota política (`THK_A_NewThiryn`) e à preparação militar da reivindicação (`THK_PrepareTheClaim`), em vez de ficar disponível desde o primeiro dia;
- o evento disparado é `azarya_formables.1` (namespace próprio `azarya_formables`), sempre depois do efeito (`hidden_effect`);
- `news.59` era de fato um resíduo morto — um evento de notícia completo, nunca chamado, reutilizando o namespace vanilla `news` proibido pelo canon — e foi removido de `events/NewsEvents.txt`;
- Great Thiryn continua representando apenas a reconquista dos três estados perdidos, sem ambição territorial maior.

O novo ramo "The Lost Border" (foco raiz `THK_RevanchistSentiment`, prerequisito = qualquer um dos três caminhos políticos) cobre revanchismo, refugiados, veteranos, o dilema de aceitar ou recusar o patrocínio gydiano, e a preparação de uma reivindicação formal via decisão (`THK_ClaimLostProvinces`, agora usando `retake_core_state` por estado sobre 86/400/409 — os três já são core de THK, então essa é a via preferida sobre `start_justifying_wargoal_against`/`create_wargoal_type`, tentativas anteriores desta mesma rodada de correções). A decisão valida a existência de UPG, ausência de guerra/wargoal já ativos e posse residual de UPG sobre os estados, e usa cooldown (`days_re_enable`) em vez de flag de uso único, para não travar permanentemente caso a justificação seja cancelada — nenhum foco ou decisão declara guerra automaticamente, e nada do lado de UPG ou do sistema geopolítico global (`az_gye_influence_upg`, IA de Gengen) foi implementado nesta rodada.

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
