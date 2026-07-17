# Sistema: Crônicas e Lore por Estado (`AZ_lore` / `AZ_CHRONICLE`)

*Ver `00_CANON_RULES.md` para os status e a hierarquia das fontes.*

## Função do sistema

O sistema de Crônicas registra o passado consolidado de Azarya e oferece contexto geográfico por estado.

Ele **não deve substituir**:

- eventos nacionais;
- news events;
- decisões;
- focos;
- efeitos que alteram o mundo;
- cadeias diplomáticas jogáveis.

A regra recomendada é:

> **Crônicas explicam o passado; eventos e notícias mostram o presente acontecendo.**

## O que já existe [IMPLEMENTADO]

- `localisation/AZ_lore_l_english.yml`
  - entradas `AZ_LORE_TEXT_<state_id>_<n>`;
  - entradas `AZ_CHRONICLE_TITLE_<n>`;
  - entradas `AZ_CHRONICLE_TEXT_<n>`.
- `common/scripted_guis/AZ_lore_atlas.txt`
- `common/scripted_effects/AZ_lore_effects.txt`
- `common/on_actions/AZ_info_on_actions.txt`
- texturas temporárias:
  - `gfx/interface/AZ_lore_icon_TEMP.dds`;
  - `gfx/interface/AZ_lore_mapicon_TEMP.dds`.

As texturas são placeholders de referência e precisam ser substituídas por arte própria antes de release público.

## Conteúdo histórico já registrado [IMPLEMENTADO]

O sistema já cobre, pelo menos:

- o Grande Terremoto de 1922;
- a devastação de Eldoria;
- a crise da Coroa de Aurum;
- uma derrota militar anterior de Thiryn;
- a ideia de que a Crônica se encerra deliberadamente antes do futuro jogável.

`AZ_CHRONICLE_TEXT_5` estabelece que o registro histórico é incompleto e que, a partir de 1924, o jogador escreve o futuro.

Essa característica deve ser preservada.

## Correção de escopo

A Crônica não deve receber entradas históricas completas sobre acontecimentos que ainda podem variar durante a campanha, como:

- vencedor da Guerra das Três Bandeiras;
- destino de Durnstad;
- adesão de Thiryn ou Gengen a Gydian;
- vitória de Zauern ou Torronese;
- resultado da Grande Guerra.

Esses acontecimentos possuem múltiplos resultados jogáveis.

### Uso permitido para acontecimentos pós-1924

Há duas opções seguras:

1. **não adicioná-los à Crônica estática**;
2. criar entradas dinâmicas desbloqueadas somente depois de o resultado ocorrer.

A segunda opção exige confirmar que o sistema atual suporta:

- condições por flags;
- textos alternativos;
- desbloqueio permanente;
- save/load;
- resultados mutuamente exclusivos.

Até essa auditoria técnica existir, tratar entradas pós-1924 como **PROPOSTA**.

## Atualização recomendada da história pré-1924 [PROPOSTA]

A entrada sobre a derrota de Thiryn pode ser expandida para registrar fatos que já são canon antes do início do cenário:

- Gengen foi o país vencedor;
- Thiryn perdeu Doia (86), Haifa (400) e Mominches (409);
- os três estados contêm aproximadamente 1,7 milhão de habitantes;
- a derrota alimentou o revanchismo thiryniano;
- o terremoto agravou dívida, refugiados e perda de legitimidade.

A Crônica não deve afirmar ainda:

- o nome final da guerra;
- quem realizou o primeiro ataque;
- apoio secreto gydiano;
- nome do tratado de paz;

porque esses pontos ainda precisam de aprovação definitiva.

## Lore por estado

O atlas de estados é adequado para registrar contexto local estável:

### Thiryn e Gengen

- Eldoria (382);
- Doia (86);
- Haifa (400);
- Mominches (409).

### Expansão gydiana

- Karleston (361);
- Celest (462).

### Questão helvariana

Estados e capitais de Durtenbach, Varadnia, Junta Helvariana, Astravern e Marchas Helvarianas, depois que a geografia final for validada.

### Continente oriental

Estados de Orvena, Karyō e Liangor somente depois de a atribuição territorial estar estabilizada.

## Relação com news events

Quando um acontecimento ocorrer em jogo:

1. evento, decisão ou efeito aplica a mudança;
2. flags registram o resultado;
3. news event comunica o acontecimento;
4. opcionalmente, uma entrada dinâmica de Crônica é desbloqueada.

A notícia nunca deve executar sozinha:

- transferência de estado;
- anexação;
- declaração de guerra;
- criação de país;
- mudança de governo.

## Nomenclatura recomendada

Manter as chaves já existentes para o conteúdo legado:

```text
AZ_CHRONICLE_TITLE_<n>
AZ_CHRONICLE_TEXT_<n>
AZ_LORE_TEXT_<state_id>_<n>
```

Para entradas dinâmicas futuras, usar um bloco separado e documentado, por exemplo:

```text
AZ_CHRONICLE_DYNAMIC_TITLE_<n>
AZ_CHRONICLE_DYNAMIC_TEXT_<n>
```

Não implementar esse padrão até confirmar como o scripted localisation e a GUI selecionam as entradas.

## Testes necessários antes de expandir

- validar quantas entradas o sistema suporta;
- confirmar ordenação das Crônicas;
- testar ausência de localisation;
- testar save/load;
- confirmar se uma entrada pode ser condicionada por global flag;
- confirmar se resultados mutuamente exclusivos não aparecem juntos;
- validar que esconder marcadores não apaga progresso;
- substituir ou isolar completamente os assets temporários.

## Decisão recomendada

O sistema deve permanecer **complementar**.

- passado anterior a 1924: Crônicas;
- história local estável: lore por estado;
- acontecimentos jogáveis: eventos, decisões e notícias;
- resultados consolidados da campanha: possível expansão dinâmica futura.
