# Azarya — Matriz de Implementação de Conteúdo

*Esta matriz descreve dependências e ordem de construção. Não significa que os sistemas já estejam implementados.*

## Princípios técnicos

1. eventos e scripted effects controlam mudanças permanentes;
2. decisões e focos iniciam ou modificam cadeias;
3. notícias apenas comunicam resultados;
4. cada cadeia precisa de flags de início e conclusão;
5. toda guerra, anexação ou transferência deve ser segura contra repetição;
6. a IA histórica deve usar pesos, não efeitos forçados sem alternativa;
7. nenhum sistema novo deve depender de resíduos vanilla.

## Ordem recomendada

1. padronizar IDs, flags e namespaces;
2. implementar uma cadeia vertical mínima da Guerra das Três Bandeiras;
3. validar início único da guerra;
4. implementar condições de vitória e reunificação;
5. construir expansão gydiana por subcadeias independentes;
6. construir Thiryn–Gengen;
7. construir Sithius;
8. conectar tudo à Crise de Astravern em 1927;
9. implementar o teatro oriental;
10. adicionar focos completos, IA e balanceamento.

---

## Sistema A — Infraestrutura geopolítica compartilhada

| Campo | Definição |
|---|---|
| Status | PROPOSTA TÉCNICA |
| Objetivo | fornecer flags, variáveis, efeitos reutilizáveis e validação de estado |
| Arquivos prováveis | `AZ_geopolitics_effects.txt`, `AZ_geopolitics_triggers.txt`, `AZ_geopolitics_on_actions.txt` |
| Regras | nenhuma transferência ou guerra sem guard de idempotência |
| Testes | carga inicial, save/load, evento duplicado, país inexistente, alvo anexado por terceiro |

---

## Sistema B — Guerra das Três Bandeiras

| Campo | Definição |
|---|---|
| Status | CANON; não implementado |
| Beligerantes | DTB, VRD, HEL |
| Patrocinadores | BOM→DTB, NSA→VRD, GYE→HEL |
| Janela de início | junho–setembro de 1924 |
| Preparação | apoio externo cresce por eventos/decisões antes da guerra |
| Estopim | nome e incidente exatos TBD |
| Resultado histórico | DTB vence e forma Helvaria reunificada |
| Alternativas | vitória VRD; vitória HEL |
| Dependências | definição dos estados de reunificação, capitais, OOB e regra de paz |
| Eventos mínimos | início do apoio NSA; oferta GYE; apoio secreto BOM; escalada; início da guerra; notícia |
| Eventos finais | capitulação de cada concorrente; reunificação por vencedor; integração de unidades/personagens |
| IA | rota histórica favorece DTB, sem tornar vitória inevitável |
| Testes | guerra inicia uma vez; três lados corretos; sem paz vanilla prematura; vencedor único; reunificação funciona após save/load |

---

## Sistema C — Expansão gydiana

| Campo | Definição |
|---|---|
| Status | CANON; arquitetura TBD |
| Mecânica central | influência e dependência por país, sem uma variável global única obrigatória |
| Alvos | FVI, DUH, ATV, KOZ, NIR, UPG, THK, SIT, HEL |
| Resultado histórico | esfera formada por integrações, fantoches, aliados e concessões; não anexação automática de todos |
| Alternativas | recusa, renegociação, golpe fracassado, mudança de lado |
| Testes | cada subcadeia pode falhar sem bloquear a Crise de 1927 |

### C1 — Zauern–Torronese

| Campo | Definição |
|---|---|
| Status | CANON; `declare_war_on` encontrado em KOZ, runtime ainda precisa ser validado |
| Apoio | armas, crédito, trabalhadores, assessores e logística gydianos |
| Preço | Karleston (361) |
| Pós-guerra | Zauern entra na esfera e pode aderir sob pressão |
| Alternativas | vitória/defesa de TOL; KOZ recusa cessão; GYE retira apoio |
| Testes | guerra inicial real; transferência apenas se condição atendida; estado não transferido duas vezes |

### C2 — Nirisia e Celest

| Campo | Definição |
|---|---|
| Status | CANON |
| Oferta | eliminação dos Estados-bandidos próximos |
| Preço | Celest (462) |
| Opções | aceitar, recusar, renegociar |
| Dependência | confirmar tags/estados dos bandidos |
| Testes | bandidos já derrotados; Celest ocupada por terceiro; NIR deixa de existir |

### C3 — Fervonia

| Campo | Definição |
|---|---|
| Status | CANON |
| Ponto inicial | garantia gydiana já implementada |
| Progressão | proteção → dependência → associação/fantoche/integração |
| Rota histórica | integração ou submissão sem guerra ampla |
| Alternativas | resistência, golpe, proteção de outra potência |
| Testes | garantia removida corretamente; anexação sem unidades órfãs; autonomia válida |

### C4 — Astravern

| Campo | Definição |
|---|---|
| Status | CANON |
| Progressão | suborno, empréstimo, repressão da oposição, presença militar |
| Rota histórica | fantoche ou aliado subordinado |
| Função em 1927 | plataforma e estopim da crise com Helvaria |
| Testes | governo pró-Gydian pode cair; GYE pode intervir; crise funciona mesmo com rota alternativa |

### C5 — Durnstad

| Campo | Definição |
|---|---|
| Status | CANON |
| Ponto inicial | garantia gydiana |
| Progressão | proteção → dependência → tentativa de ruptura → intervenção |
| Rota histórica | guerra real, ocupação e anexação/submissão |
| Atrocidades | censura, deportações, desaparecimentos e falsificação de relatórios; sem descrição gráfica |
| Informação pública | primeiro propaganda gydiana; depois rumores, refugiados e documentos |
| Alternativas | Durnstad aceita tutela; intervenção fracassa; potência externa garante sobrevivência |
| Testes | garantia retirada antes da guerra; war goal válido; ocupação não dispara duas vezes; revelação não ocorre antes do encobrimento |

---

## Sistema D — Crise Thiryn–Gengen

| Campo | Definição |
|---|---|
| Status | CANON |
| Estados | Doia 86, Haifa 400, Mominches 409 |
| Ponto inicial | UPG controla os três; THK possui interesse nacional/core conforme implementação |
| Mecânica | tensão de fronteira + influência gydiana separada nos dois países |
| Eventos | patrulhas, escolas, refugiados, sabotagem, contrabando, mobilização |
| Rota histórica | Gengen inclina-se a Gydian |
| Alternativas | aliança THK–GYE; reconciliação THK–UPG; neutralidade; guerra regional |
| Great Thiryn | relação forte com reconquista dos três estados, mas ligação técnica exata deve ser revalidada |
| Testes | tensão limitada não inicia guerra automaticamente; eventos não repetem; Great Thiryn não usa notícia vanilla |

---

## Sistema E — Sithius

| Campo | Definição |
|---|---|
| Status | CANON |
| Mecânicas | dívida, concessões, prestígio naval, influência gydiana |
| Rota histórica | aliado menor de Gydian |
| Alternativas | anexação; resistência; restauração independente |
| Conteúdo | venda de porto, arrendamento, crise da frota, reivindicações em Serenvioled |
| Testes | concessões não transferem capital acidentalmente; rotas continuam se país-alvo não existe |

---

## Sistema F — Grande Guerra Continental

| Campo | Definição |
|---|---|
| Status | CANON |
| Ano | aproximadamente 1927 |
| Estopim histórico | intervenção gydiana em Astravern e ultimato recusado por Helvaria |
| Ator central anti-GYE | Helvaria reunificada |
| Dilemas | THK/UPG; SIT; NSA; BOM; CZL; Estados-tampão |
| Novasovia | entra depois e amplia a escala |
| Requisitos | Helvaria existente ou fallback para vencedor alternativo; Astravern sob influência ou crise alternativa |
| Testes | guerra pode iniciar com vencedor VRD/HEL; não exige tags mortas; blocos formados dinamicamente; nenhuma declaração duplicada |

---

## Sistema G — Continente oriental

### Orvena

| Campo | Definição |
|---|---|
| Status | CANON; implementação em andamento |
| Mecânica | federalismo, isolacionismo, mobilização estadual |
| Papel | fornecedor, arsenal e participante tardio |
| Entrada histórica | ameaça a rotas, ilhas ou base orveniana |
| Testes | mobilização gradual; neutralidade possível; entrada não depende de data fixa apenas |

### Karyō

| Campo | Definição |
|---|---|
| Status | CANON; implementação em andamento |
| Mecânica | disputa Exército–Marinha, falta de recursos, expansão |
| Papel | agressor oriental |
| Relação GYE | cooperação inicial, interesses próprios |
| Testes | expansão limitada ou total; guerra não quebra se LIA fragmentar |

### Liangor

| Campo | Definição |
|---|---|
| Status | CANON; implementação em andamento |
| Mecânica | autoridade central e lealdade dos governadores |
| Papel | grande potência potencial sob invasão |
| Caminhos | centralização republicana, confederação, revolução, restauração |
| Testes | perda de capital não encerra cadeia; governadores reagem à invasão |

---

## Sistema H — News events

| Regra | Implementação |
|---|---|
| Namespace | `az_news` |
| Função | comunicar fatos já aplicados |
| Proibido | transferir estados, iniciar guerra ou anexar países apenas dentro da notícia |
| Visibilidade | notícia pública pode conter propaganda ou informação incompleta |
| Testes | notícia dispara uma vez; não aparece para evento oculto abortado |

## Dependência resumida

```text
Três Bandeiras ──> Helvaria reunificada ──┐
                                          ├─> Crise de Astravern ──> Guerra Continental
Expansão gydiana ──> Astravern/FVI/DUH ───┘
THK–UPG + Sithius + Novasovia ────────────> escala e composição da guerra
Karyō–Liangor + Orvena ───────────────────> transformação em guerra mundial
```
