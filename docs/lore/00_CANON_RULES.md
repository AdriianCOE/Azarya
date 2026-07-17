# Azarya — Regras de Canon e Documentação

*Revisão: 2026-07-17.*

Este arquivo define como a bíblia de lore em `docs/lore/` deve ser lida, atualizada e utilizada durante a implementação do mod.

## Hierarquia das fontes

Quando duas informações entrarem em conflito, use esta ordem:

1. decisão explícita mais recente do autor;
2. inspeção atual do repositório;
3. documentação técnica mais recente;
4. auditorias antigas;
5. propostas ainda não aprovadas.

Uma auditoria é uma fotografia de uma data específica. Ela não substitui decisões canônicas posteriores nem uma nova inspeção do repositório.

## Status permitidos

| Status | Significado |
|---|---|
| **CANON** | Decisão narrativa aprovada explicitamente pelo autor. |
| **IMPLEMENTADO** | Fato confirmado no estado atual do repositório. Deve citar o arquivo correspondente. |
| **PROPOSTA** | Ideia ainda não aprovada definitivamente. |
| **TBD** | Informação em aberto. Não deve ser preenchida por suposição. |
| **LEGADO** | Conteúdo antigo, vanilla ou herdado de outro mod que ainda precisa ser revisado. |
| **TEMPORÁRIO** | Placeholder técnico, visual ou textual que será substituído. |

Um item pode carregar mais de um status. Exemplo: uma guerra pode ser **CANON**, mas ainda não estar **IMPLEMENTADA**.

## Regras obrigatórias

1. **CANON não significa IMPLEMENTADO.**  
   A Guerra das Três Bandeiras é canônica, mas sua cadeia de eventos ainda precisa ser construída.

2. **IMPLEMENTADO não significa CANON.**  
   Um arquivo vanilla residual ou uma declaração de guerra antiga não se torna lore apenas porque está carregado.

3. **Notícias não controlam a lógica.**  
   Eventos, decisões ou efeitos alteram o mundo. News events apenas comunicam a consequência.

4. **Uma única fonte de verdade por efeito.**  
   Transferência de estado, início de guerra, anexação, mudança de governo ou formação de país não deve ser duplicada em foco, decisão e evento ao mesmo tempo.

5. **Toda cadeia precisa ser idempotente.**  
   O mesmo evento não pode iniciar duas guerras, transferir o mesmo estado duas vezes ou repetir uma anexação após save/load.

6. **Todo caminho histórico precisa de alternativas jogáveis.**  
   A IA pode ter uma rota histórica preferida, mas as opções do jogador não devem ser falsas.

7. **Nenhum dado placeholder vira lore.**  
   População 1–5, ausência de indústria, retrato genérico e texto legado são dados temporários.

8. **Temas de atrocidades devem ser tratados sem descrição gráfica.**  
   A ocupação de Durnstad deve ser apresentada por censura, deportação, desaparecimentos, refugiados, documentos, responsabilidade política e consequências internacionais.

9. **Não misturar Durnstad e Durtenbach.**

   - `DUH` — **Durnstad**: pequeno reino inicialmente garantido por Gydian; futura intervenção armada e ocupação.
   - `DTB` — **Durtenbach**: competidor da Guerra das Três Bandeiras e possível núcleo da Helvaria reunificada.

10. **Nenhuma implementação nova deve reutilizar IDs genéricos vanilla.**  
    Em especial, não criar notícias novas no namespace `news`. Usar namespace próprio de Azarya.

## Decisões canônicas já consolidadas

### Cenário

- Início em **1º de janeiro de 1924**.
- Apenas um cenário ativo.
- Guerra das Três Bandeiras começa entre **junho e setembro de 1924**.
- Grande Guerra Continental começa aproximadamente em **1927**.

### Expansão gydiana

- Gydian busca hegemonia por influência, dívida, tratados, golpes, garantias e anexações negociadas.
- Durnstad é a principal exceção anterior à Grande Guerra: a anexação exige guerra real.
- A garantia gydiana a Durnstad é parte do mecanismo de dependência e traição, não uma contradição.
- Astravern tende a virar aliado subordinado ou fantoche.
- Fervonia tende a ser integrada ou submetida sem guerra ampla.
- Zauern recebe apoio contra Torronese em troca de Karleston, estado 361.
- Nirisia recebe uma oferta de pacificação dos Estados-bandidos em troca de Celest, estado 462.
- Gydian tenta usar simultaneamente Thiryn e Gengen.

### Guerra das Três Bandeiras

- Beligerantes: Durtenbach, Varadnia e Junta Helvariana.
- Novasovia começa a armar Varadnia aproximadamente cinco meses após o início do cenário.
- Gydian apoia a Junta.
- Montia apoia Durtenbach secretamente e atua por redes religiosas extremistas.
- Rota histórica: vitória de Durtenbach e formação de uma Helvaria reunificada.
- A Helvaria reunificada torna-se o principal rival continental de Gydian.
- Varadnia e a Junta permanecem vencedores alternativos válidos.

### Thiryn e Gengen

- Thiryn perdeu Mominches (409), Doia (86) e Haifa (400) para Gengen.
- População técnica atual combinada: **1.657.762**, arredondada na lore para **aproximadamente 1,7 milhão**.
- Gengen tende inicialmente ao bloco gydiano.
- Gydian pode prometer os territórios a Thiryn enquanto oferece proteção a Gengen.
- Os conflitos de fronteira devem escalar sem obrigatoriamente iniciar guerra imediata.

### Sithius

- Foi um grande império marítimo baseado em ilhas, portos, estreitos e possessões distantes.
- Perdeu territórios longínquos para populações locais e potências próximas.
- Vendeu ou concedeu territórios próximos para pagar dívidas, sobretudo a Gydian.
- Pode ser anexado, resistir ou tornar-se aliado menor de Gydian.
- Na rota histórica, tende a cumprir papel de aliado oportunista do bloco gydiano.

### Continente oriental

Os conceitos e nomes atuais foram aprovados como base canônica:

- **ORV — Federação de Orvena**
- **KAR — Império de Karyō**
- **LIA — República de Liangor**

Tags, fronteiras e arquivos em andamento são **IMPLEMENTAÇÃO EM ANDAMENTO**; capitais, líderes, população, OOB e detalhes ainda podem permanecer **TBD** até confirmação no repositório.

## Estrutura recomendada

```text
docs/lore/
├── README.md
├── 00_CANON_RULES.md
├── 01_WORLD_OVERVIEW.md
├── 02_MASTER_TIMELINE.md
├── 03_GEOPOLITICAL_BLOCKS.md
├── 04_CONTENT_IMPLEMENTATION_MATRIX.md
├── 05_ID_AND_FLAG_REGISTRY.md
├── countries/
├── conflicts/
├── systems/
└── regions/
```

## Regra de manutenção

Toda alteração narrativa relevante deve atualizar, no mínimo:

- a ficha do país;
- a ficha do conflito ou sistema;
- a timeline, se houver impacto cronológico;
- a matriz de implementação;
- o registro de IDs, quando houver criação técnica.

Metadados efêmeros de worktree não pertencem às regras de canon. Devem ficar em relatórios de auditoria ou no resumo da rodada.
