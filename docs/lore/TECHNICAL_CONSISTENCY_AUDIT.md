# Auditoria Técnica de Consistência — Azarya

*Rodada de auditoria: 2026-07-17. Somente leitura — nenhum arquivo de jogo foi alterado para produzir este relatório.*

*Ver `00_CANON_RULES.md` para a hierarquia de fontes. Esta auditoria é uma fotografia desta data; não substitui decisões canônicas posteriores nem uma nova inspeção do repositório.*

---

## 1. Resumo executivo

A camada `docs/lore/` está estruturalmente correta e já se autodeclara honesta: 19 fichas de país, 5 fichas de conflito, 2 sistemas e 2 regiões existem exatamente como o `00_CANON_RULES.md` prescreve, e a maioria dos itens sensíveis (Eldoria como epicentro, população de Thiryn/Gengen, desambiguação DUH/DTB) já estava corrigida antes desta rodada. O trabalho útil desta auditoria foi cruzar essa lore com o estado real do repositório de jogo (`common/`, `history/`, `events/`, `localisation/`).

Resultado geral: **a lore é mais confiável do que o código**. Praticamente todo item que a lore já marcava como "a revalidar" se confirmou problemático quando checado contra os arquivos reais, e um item não documentado foi descoberto (HEL tem a mesma inconsistência de ideologia que a lore só atribuía a VRD).

Achados mais graves, em ordem de severidade:

1. **`news.59` é código morto que viola a própria regra de namespace do mod.** Existe em `events/NewsEvents.txt:125`, comentado "# Formation of Great Thiryn", mas não é chamado por nenhum foco, decisão ou evento ativo — a formação real usa `azarya_formables.1`.
2. **A cessão de Karleston (361) a Gydian não existe em lugar nenhum do código.** Só a guerra KOZ→TOL existe (`declare_war_on` incondicional no boot, com `type = annex_everything` — narrativamente incompatível com "ceder apenas 1 estado").
3. **Não existe nenhum mecanismo técnico para a Guerra das Três Bandeiras.** DTB, VRD e HEL simplesmente coexistem; nenhum `declare_war_on`, evento, decisão ou on_action liga os três países entre si.
4. **Três das quatro tags orientais e helvarianas usam ideologias de líder que não existem** em `common/ideologies/00_ideologies.txt` (`Federalist`, `Divine_Throne`, `Nationalist`).
5. **Sithius tem zero navios e zero divisões terrestres reais no OOB**, apesar de 16 níveis de base naval, 6 estaleiros e uma ideia nacional inteira celebrando seu poderio naval.

Nada disso é urgente de corrigir nesta rodada — o escopo pedido foi só auditar. Mas todos esses pontos bloqueiam qualquer tentativa de iniciar a Guerra das Três Bandeiras ou a expansão gydiana como sistemas jogáveis.

**Correção canônica registrada nesta rodada:** a ausência de estados pertencentes a `KAR` — apontada como achado crítico na versão anterior deste relatório — não é uma inconsistência. O autor confirmou que é intencional: Karyō será localizado em um arquipélago oriental ainda não criado no mapa. Tag, arquivo de país, história, personagens, ideias e localisation foram preparados antecipadamente; território, capital e OOB dependem da criação futura dessa massa terrestre. Ver a nota dedicada na seção 2.

---

## 2. Inconsistências críticas

| # | Achado | Evidência | Impacto |
|---|---|---|---|
| C1 | **`news.59` é evento órfão no namespace vanilla proibido.** | `events/NewsEvents.txt:122-155`, comentário `# Formation of Great Thiryn`, opções `news.59.a/.b/.c` com `trigger = { original_tag = THK ... }`. Nenhum `news_event = { id = news.59 ... }` é chamado por foco/decisão/evento algum no repositório. | Viola `00_CANON_RULES.md` regra 10 e `05_ID_AND_FLAG_REGISTRY.md` ("não reutilizar namespace `news`"). Código morto que confunde qualquer auditoria futura sobre "qual é a notícia real de Great Thiryn". |
| C2 | **Cessão de Karleston (361) a Gydian é 100% inexistente em script.** | `history/states/361-*.txt`: `owner = KOZ`, `add_core_of = GYE` (apenas um core, não uma transferência). Nenhuma ocorrência de "361"/"Karleston" em `common/decisions/`, `common/scripted_effects/`, `events/`. | O elo central da doutrina de expansão gydiana ("Zauern recebe apoio, cede Karleston") não tem nenhum wiring técnico — é puramente conceitual em `docs/`. |
| C3 | **Guerra KOZ→TOL dispara incondicionalmente no boot com wargoal excessivo.** | `history/countries/KOZ - Kingdom of Zauern.txt:86-89`: `declare_war_on = { target = TOL type = annex_everything }`, fora de qualquer `if`/bloco de data, entre `army_experience` e `set_politics`. | Sem gatilho narrativo, sem condição de aceite do acordo. `annex_everything` anexaria TOL inteira, não só Karleston — contradiz a própria lore (`02_zauern_torronese_war.md`, linha 91: "a cessão deve ser apresentada como acordo legal, não anexação aberta"). |
| C4 | **Nenhum mecanismo liga DTB, VRD e HEL em guerra.** | Busca por `declare_war_on` envolvendo essas 3 tags em `events/`, `common/on_actions/`, `common/decisions/`, `common/scripted_effects/`, `common/scripted_triggers/`, `history/countries/`: zero resultados. `az_three_banners` só existe em `docs/`. | A Guerra das Três Bandeiras — CANON segundo `00_CANON_RULES.md` — não tem absolutamente nenhuma implementação técnica hoje. Ver seção 9. |
| C5 | **Ideologias de líder inválidas em ORV, KAR e LIA.** | `create_country_leader = { ideology = Federalist }` (ORV), `= Divine_Throne` (KAR), `= Nationalist` (LIA) — nenhuma dessas três chaves existe em `common/ideologies/00_ideologies.txt`. | Ideologia customizada inexistente tende a gerar erro/aviso no `error.log` e pode quebrar a exibição do líder no jogo. O caso de KAR (`Divine_Throne`) é um problema real independente da questão territorial tratada na nota abaixo. |
| C6 | **Sithius tem zero unidades reais no OOB.** | `history/countries/SIT - Sithius.txt:3`: `set_oob = "standard_templates"`; `history/units/standard_templates.txt` contém só um `division_template` de milícia nunca instanciado — nenhum `division = {}` nem `navy = {}` real. Esse OOB é compartilhado por 31 países do mod. | Contradiz e piora a suspeita da própria lore ("zero navios no OOB"): não há zero navios apenas, não há nenhuma unidade terrestre ou naval implantada, apesar de 16 níveis de base naval, 6 estaleiros e tecnologia naval avançada pesquisada no history. |

### Nota canônica — Karyō (KAR) não é uma inconsistência

Correção recebida do autor nesta rodada: a ausência de estados pertencentes a `KAR` é **intencional**, não um bug nem uma regressão. Karyō será localizado em um novo arquipélago que ainda será criado manualmente no mapa. A tag, o arquivo de país, a história, os personagens, as ideias e a localisation foram preparados antecipadamente, antes da criação da massa terrestre correspondente.

> **Arquipélago de Karyō ainda não implementado. A estrutura nacional já existe, mas a atribuição territorial depende da criação de nova massa terrestre, províncias, estados, regiões estratégicas e conexões marítimas.**

Classificação correta:

| Elemento | Status |
|---|---|
| Conceito nacional | CANON |
| Estrutura de país (tag, história, ideias, personagens, localisation) | IMPLEMENTAÇÃO EM ANDAMENTO |
| Território, capital, estados, portos e OOB | BLOQUEADOS PELA EXPANSÃO DO MAPA |
| Ausência atual de owner em `history/states/` | INTENCIONAL |

Não recomendar: atribuir território provisório a KAR, usar estados já existentes de Orvena, Liangor ou do continente principal como solução temporária, ou tratar capital/OOB ausentes como erros independentes nesta fase — todos dependem da criação do arquipélago definitivo. O arquipélago oriental **não bloqueia** a Guerra das Três Bandeiras nem nenhum outro conflito hesperiano (ver seção 9).

Permanecem como problemas reais e separados, não relacionados à questão territorial: a ideologia de líder `Divine_Throne` (inexistente em `common/ideologies/00_ideologies.txt`, ver C5); a necessidade futura de definir capital; a necessidade futura de um OOB dedicado; e a necessidade de validar recursos, portos e infraestrutura somente depois que o arquipélago for criado.

---

## 3. Inconsistências médias

| # | Achado | Evidência |
|---|---|---|
| M1 | **VRD: `ruling_party = communism`, mas o líder tem ideologia `conservatism`.** Confirma literalmente o que a lore já sinalizava como "a corrigir". | `history/countries/VRD - Varadnia.txt:115-120` (`ruling_party = communism`) e `:129-132` (`create_country_leader = { ideology = conservatism }`). `conservatism` está definido sob o grupo `democratic` em `common/ideologies/00_ideologies.txt:7`. |
| M2 | **HEL tem a mesma inconsistência que VRD, mas isso NÃO estava documentado na lore.** `ruling_party = neutrality`, líder com ideologia `conservatism` (grupo `democratic`). | `history/countries/HEL - Helvaria.txt:70-75` e `:84-87`. Achado novo desta auditoria — `docs/lore/countries/HEL.md` só menciona dados quantitativos como TEMPORÁRIO, não esta inconsistência de ideologia. |
| M3 | **ATV: possível divergência de capitalização entre `Rexism` (usado no history) e `rexism` (definido em `00_ideologies.txt:150`).** Não confirmado como bug em runtime, mas HoI4 costuma ser case-sensitive para chaves de ideologia. | `history/countries/ATV - Astravern.txt:101-103`; `common/ideologies/00_ideologies.txt:150`. |
| M4 | **`annex_everything` é sintaticamente válido** (usado também em `common/operations/00_operations.txt:1718` e `common/scripted_effects/00_scripted_effects.txt:116,122`), mas narrativamente incompatível com a rota histórica de Zauern-Torronese. Ver C3. | — |
| M5 | **`form_Great_Thiryn` usa `controls_state`, não `owns_state`/`is_owned_by`.** A lore não especifica qual verbo técnico deveria ser usado; `controls_state` permite formar Great Thiryn por ocupação militar, sem anexação formal via paz — uma diferença narrativa relevante (revanchismo "pacífico" via paz vs. conquista militar). | `common/decisions/formable_nation_decisions.txt`, bloco `form_Great_Thiryn.available`. |
| M6 | **Estados 507/508/509 não pertencem majoritariamente às tags orientais**, contrariando a hipótese de `01_WORLD_OVERVIEW.md`/`eastern_continent.md` de que estariam ligados à expansão oriental. | `history/states/507-*.txt`: `owner = DRM`. `508-*.txt`: `owner = EDR`. `509-*.txt`: `owner = ORV` (único dos três de fato oriental). |
| M7 | **Referências cruzadas em `docs/lore/` usam nomes de arquivo sem caminho relativo.** Ex.: `docs/lore/countries/BOM.md` referencia `` `01_three_banners_war.md` `` sem indicar que o arquivo está em `../conflicts/`. Todos os arquivos-alvo existem (nenhum link quebrado de fato), mas a navegação por caminho literal falharia. `CZL.md` referencia vagamente "a auditoria histórica" em vez de nomear `AZARYA_WORLD_CONTEXT_AUDIT.md`. | Ver lista completa na seção 8 (links) abaixo. |
| M8 | **Localisation de conselheiros genéricos ausente em ORV/KAR/LIA.** Os 20 tokens de conselheiro por país (`ORV_ar`, `KAR_acr`, `LIA_stc`, etc., definidos em `common/characters/<TAG>.txt`) não têm nenhuma chave de nome em `localisation/`. | `common/characters/ORV.txt`, `KAR.txt`, `LIA.txt` vs. busca em `localisation/*.yml`. |
| M9 | **Karleston (361) tem `add_core_of = GYE`**, ou seja, já existe um core histórico de Gydian sobre o estado, mesmo sem qualquer transferência ativa. Isso é coerente com "pretensão histórica" mas pode confundir uma futura implementação de scripted_trigger de elegibilidade de transferência (que normalmente checa ausência de core do destinatário como sinal de "ainda não transferido"). | `history/states/361-State_361.txt`. |

---

## 4. Placeholders confirmados

| Item | Status confirmado | Fonte |
|---|---|---|
| HEL — manpower total | **Exatamente 3** (3 estados, 1 manpower cada, nomes `STATE_35`, `STATE_198`, `STATE_205`) | `history/states/35,198,205-*.txt` |
| ATV — manpower total | **Exatamente 5** (5 estados, 1 manpower cada) | `history/states/238,241,242,248,259-*.txt` |
| DTB — manpower total | 12.757.620, estados nomeados de verdade — **não é placeholder**, bate com a lore | `history/states/` (15 estados com owner=DTB) |
| VRD — manpower total | 7.501.964, 5/6 estados com nome real; 1 estado (187) é placeholder puro (`manpower=1`, `name="STATE_187"`) | `history/states/` (6 estados com owner=VRD) |
| SIT — OOB | `standard_templates` genérico, 0 navios, 0 divisões reais, compartilhado por 31 países | `history/units/standard_templates.txt` |
| DTB/VRD/HEL/ATV — OOB | Todos usam o mesmo `standard_templates` genérico | `history/countries/*.txt: set_oob` |
| ORV/LIA — capital e OOB | Comentados/ausentes nos dois (`# capital = <state_id>`, `# oob = "..."`), com TODO explícito no arquivo — território já existe, é pendência de atribuição real, não bloqueio de mapa | `history/countries/ORV - Orvena.txt`, `LIA - Liangor.txt` |
| KAR — capital e OOB | Também comentados/ausentes, mas **não são placeholders a preencher agora** — dependem da criação do arquipélago oriental (correção canônica, ver seção 2) | `history/countries/KAR - Karyo.txt` |
| SIT — estados brutos vs. desenvolvidos | 13 arquivos de estado com owner=SIT, mas 2 (`STATE_52`, `STATE_255`) são placeholders vazios sem nome/prédios — a lore conta "11 estados", que bate se excluídos os 2 placeholders | `history/states/52,255-*.txt` |
| ATV/HEL/DTB/VRD — personagens | `create_country_leader` sem `Name =` em VRD, HEL e ATV (só DTB tem nome, "Cleitinho do Durten") | `history/countries/*.txt` |

---

## 5. Conteúdo legado

- **`news.59`** (`events/NewsEvents.txt:122-155`) é o item de conteúdo legado mais concreto encontrado: um evento de notícia completo, com 3 opções condicionadas a `original_tag = THK`, comentado explicitamente como "Formation of Great Thiryn", mas hoje desconectado de qualquer chamador. É quase certamente uma implementação anterior de Great Thiryn, substituída pela decisão atual (`form_Great_Thiryn` → `azarya_formables.1`), mas nunca removida. Ver C1.
- **`docs/AZARYA_WORLD_CONTEXT_AUDIT.md`** é uma auditoria antiga (camada 4 na hierarquia de fontes do `00_CANON_RULES.md`) com números de população para países não relacionados a Thiryn/Gengen (RFB: 1.892.940; EYD: 1.777.764) — não é uma contradição sobre o total de 1,7 milhão de Doia/Haifa/Mominches (que já está correto e consistente em todos os arquivos de `docs/lore/`), apenas dados de outros países que não foram auditados nesta rodada.
- **`standard_templates` genérico** compartilhado por 31 países (incluindo os 4 beligerantes helvarianos e Sithius) é, na prática, um placeholder técnico herdado de um estágio inicial de desenvolvimento — nenhum desses países tem um OOB narrativamente dedicado ainda.
- **Nenhuma mistura DUH/DTB** foi encontrada em nenhum arquivo de jogo (`common/characters/DUH.txt`, `common/names/DUH_names.txt`, `history/units/DUH.txt`, localisation) — a separação determinada pela regra 9 do `00_CANON_RULES.md` está sendo respeitada tecnicamente.
- **Nenhuma guerra, anexação ou wargoal pré-configurado** foi encontrado para DUH no boot — consistente com a premissa de que a crise de Durnstad ainda não começou em 1924.1.1.

---

## 6. Tabela por país (elementos auditados nesta rodada)

| País | Tag+arquivos | História/país | Estados/owner | OOB | Ideias | Personagens | Localisation | Foco/Decisões/Eventos |
|---|---|---|---|---|---|---|---|---|
| Orvena | IMPLEMENTADO | IMPLEMENTAÇÃO INCOMPLETA (capital ausente; ideologia `Federalist` inválida) | IMPLEMENTAÇÃO INCOMPLETA (29 estados, nomes majoritariamente placeholder) | AUSENTE | IMPLEMENTADO | IMPLEMENTAÇÃO INCOMPLETA (sem loc. de conselheiros) | IMPLEMENTAÇÃO INCOMPLETA | AUSENTE |
| Karyō | IMPLEMENTAÇÃO EM ANDAMENTO | CONTRADITÓRIO quanto à ideologia (`Divine_Throne` inválida, problema real); capital BLOQUEADA PELA EXPANSÃO DO MAPA (intencional, não é erro) | BLOQUEADO PELA EXPANSÃO DO MAPA (arquipélago ainda não criado — ausência de owner é intencional, ver nota canônica na seção 2) | BLOQUEADO PELA EXPANSÃO DO MAPA | IMPLEMENTADO | IMPLEMENTAÇÃO INCOMPLETA | IMPLEMENTAÇÃO INCOMPLETA | AUSENTE (não bloqueia a Guerra das Três Bandeiras) |
| Liangor | IMPLEMENTADO | IMPLEMENTAÇÃO INCOMPLETA (capital ausente; ideologia `Nationalist` inválida) | IMPLEMENTAÇÃO INCOMPLETA (17 estados, nomes majoritariamente placeholder) | AUSENTE | IMPLEMENTADO | IMPLEMENTAÇÃO INCOMPLETA | IMPLEMENTAÇÃO INCOMPLETA | AUSENTE |
| Durtenbach (DTB) | IMPLEMENTADO | IMPLEMENTADO (ideologia `oligarchism` válida e coerente) | IMPLEMENTADO (15 estados, manpower bate com a lore) | PLACEHOLDER (genérico) | AUSENTE | IMPLEMENTADO (20 conselheiros + líder nomeado) | IMPLEMENTADO | AUSENTE |
| Varadnia (VRD) | IMPLEMENTADO | CONTRADITÓRIO (`communism`/`conservatism`) | IMPLEMENTAÇÃO INCOMPLETA (manpower bate, 1 estado placeholder) | PLACEHOLDER (genérico) | AUSENTE | IMPLEMENTADO (sem nome de líder) | IMPLEMENTADO | AUSENTE |
| Junta Helvariana (HEL) | IMPLEMENTADO | CONTRADITÓRIO (`neutrality`/`conservatism`, achado novo) | PLACEHOLDER (manpower=3, confirmado) | PLACEHOLDER (genérico) | AUSENTE | IMPLEMENTADO (sem nome de líder) | IMPLEMENTADO | AUSENTE |
| Astravern (ATV) | IMPLEMENTADO | IMPLEMENTAÇÃO INCOMPLETA (possível typo `Rexism`/`rexism`) | PLACEHOLDER (manpower=5, confirmado) | PLACEHOLDER (genérico) | AUSENTE | IMPLEMENTADO (sem nome de líder) | IMPLEMENTADO | AUSENTE |
| Durnstad (DUH) | IMPLEMENTADO | IMPLEMENTADO (garantia GYE→DUH correta) | IMPLEMENTADO (2 estados) | Não auditado nesta rodada | Não auditado | IMPLEMENTADO (líder nomeado) | IMPLEMENTADO | AUSENTE (esperado — crise ainda não implementada) |
| Sithius (SIT) | IMPLEMENTADO | IMPLEMENTADO (dados batem com a lore) | IMPLEMENTADO (16 níveis de base naval e 6 estaleiros conferem exatamente) | **CONTRADITÓRIO (zero navios e zero divisões reais)** | IMPLEMENTADO (3 ideias, incl. legado "Victorium") | Não auditado a fundo | IMPLEMENTADO (descrição nacional presente) | AUSENTE |

---

## 7. Tabela por conflito

| Conflito | Mecanismo de início | Estado técnico | Bloqueadores principais |
|---|---|---|---|
| Zauern–Torronese | `declare_war_on` incondicional no boot (`history/countries/KOZ - Kingdom of Zauern.txt:86-89`) | IMPLEMENTAÇÃO PARCIAL — a guerra existe tecnicamente, mas sem gatilho narrativo nem condição de aceite | `type = annex_everything` é excessivo; cessão de Karleston 100% ausente do código (ver C2, C3) |
| Great Thiryn | Decisão `form_Great_Thiryn` em `common/decisions/formable_nation_decisions.txt`, sempre disponível para `original_tag = THK` que controle os estados 86/400/409 | IMPLEMENTADO (decisão + evento próprio `azarya_formables.1`), mas com código morto coexistente (`news.59`) | Remover/decidir o destino de `news.59` (ver C1); nenhum foco na árvore de THK está de fato ligado à formação |
| Guerra das Três Bandeiras | **Nenhum** | **AUSENTE — 100% conceitual**, existe apenas em `docs/lore/conflicts/01_three_banners_war.md` | Ver seção 9 (bloqueadores dedicados) |
| Crise de Durnstad | **Nenhum** (esperado nesta fase) | AUSENTE — apenas a garantia inicial GYE→DUH está implementada, coerente com a lore de que a crise ainda não começou | Cadeia completa (proteção→dependência→ruptura→intervenção→ocupação) precisa ser construída do zero; nenhuma flag conceitual (`az_duh_*`) existe em código |
| Grande Guerra Continental | **Nenhum** (esperado nesta fase; depende da Crise de Astravern, que depende da Guerra das Três Bandeiras) | AUSENTE — puramente conceitual | Depende de C4/seção 9 estarem resolvidos primeiro |

---

## 8. IDs e namespaces disponíveis

### Links relativos em `docs/lore/` (validação de estrutura)

Todos os arquivos referenciados por nome nas fichas existem em algum lugar da árvore `docs/lore/` — **nenhum link quebrado de fato** — mas nenhuma referência usa caminho relativo (`../conflicts/...`), apenas o nome do arquivo. Isso funciona em busca textual, mas não é clicável/navegável como link real. Lista completa de referências cruzadas verificadas:

- `01_WORLD_OVERVIEW.md` → `00_CANON_RULES.md`, `02_MASTER_TIMELINE.md`, `03_GEOPOLITICAL_BLOCKS.md`, `04_CONTENT_IMPLEMENTATION_MATRIX.md`, `05_ID_AND_FLAG_REGISTRY.md` — todos existem no mesmo diretório (`docs/lore/`), referência correta.
- `countries/BOM.md`, `DTB.md`, `HEL.md`, `NSA.md`, `VRD.md` → `01_three_banners_war.md` — arquivo real está em `conflicts/01_three_banners_war.md` (caminho omitido).
- `countries/KOZ.md`, `TOL.md` → `02_zauern_torronese_war.md` — real em `conflicts/`.
- `countries/THK.md`, `UPG.md` → `03_thiryn_gengen_conflict.md` — real em `conflicts/`.
- `countries/DUH.md` → `04_durnstad_crisis.md` — real em `conflicts/`.
- `countries/ATV.md`, `SIT.md`, `NSA.md` → `05_great_continental_war.md` — real em `conflicts/`.
- `countries/KAR.md`, `LIA.md`, `ORV.md` → `eastern_continent.md` — real em `regions/`.
- `countries/FVI.md`, `GYE.md`, `NIR.md` → `gydian_expansion_doctrine.md` — real em `systems/`.
- `conflicts/02_zauern_torronese_war.md` → `gydian_expansion_doctrine.md` — real em `systems/`.
- `countries/CZL.md` → "a auditoria histórica" (referência vaga, sem nome de arquivo) — deveria apontar para `AZARYA_WORLD_CONTEXT_AUDIT.md` (que fica em `docs/`, um nível acima de `docs/lore/`).
- `PACK1_REVIEW.md` → `AZARYA_WORLD_CONTEXT_AUDIT.md` — este também está em `docs/`, não em `docs/lore/`; referência correta quanto ao nome, mas fora da árvore `docs/lore/`.

**Contagem estrutural confirmada:** 19 fichas em `countries/` ✓, 5 fichas em `conflicts/` ✓, 2 arquivos em `systems/` ✓, 2 arquivos em `regions/` ✓.

### Namespaces `az_*` propostos em `05_ID_AND_FLAG_REGISTRY.md`

Todos os 10 namespaces propostos (`az_gye`, `az_three_banners`, `az_koz_tol`, `az_nir`, `az_duh`, `az_thk_upg`, `az_sit`, `az_great_war`, `az_east`, `az_news`) foram buscados em todo o repositório fora de `docs/`, incluindo eventos, flags, variáveis, nomes de arquivo e localisation.

**Resultado: os 10 namespaces são 100% propostas. Nenhum existe hoje em nenhuma forma no código do mod.** Não há, portanto, nenhuma colisão a resolver — mas há infraestrutura relacionada já ativa que os novos sistemas devem considerar antes de criar algo do zero:

| Já existe | Onde | Relevância |
|---|---|---|
| Namespace de evento `az_info` (minúsculo, já usa o padrão `az_`) | `events/AZ_info_events.txt:1` | Precedente direto de convenção — um namespace `az_` minúsculo já está em produção para um sistema diferente (info/lore). Os novos namespaces (`az_gye` etc.) devem seguir o mesmo padrão sem colidir com este. |
| Namespace de evento `azarya_formables` | `events/AZ_formables.txt` | Usado pela decisão `form_Great_Thiryn`; não colide com `az_east`/`az_great_war` mas é outro precedente de nomenclatura a considerar. |
| Namespace vanilla `news` (não `az_news`) | `events/NewsEvents.txt:5` | Contém o evento órfão `news.59` (ver C1). É exatamente o namespace que `05_ID_AND_FLAG_REGISTRY.md` já pede para não reutilizar — a regra está correta e é ativamente violada por conteúdo legado, não por conteúdo novo. |
| Categoria de decisão `foreign_influence` | `common/decisions/foreign_influence.txt` | Arquivo-stub, conteúdo integral é `foreign_influence = {}` — candidato natural para hospedar decisões de `az_gye` (influência/dependência) sem precisar criar uma categoria nova. |
| Padrão de decisão de formação de nação | `common/decisions/formable_nation_decisions.txt` (`form_Great_Thiryn`) | Modelo pronto e reutilizável para qualquer formação futura (ex.: Helvaria reunificada), incluindo o padrão de flags `set_global_flag`/`set_country_flag` de conclusão única. |
| Triggers genéricos de subject/dependência | `common/scripted_triggers/00_scripted_triggers.txt`: `is_controlled_by_ROOT_or_subject`, `is_free_or_subject_of_root`, `owns_or_subject_of`, `controls_or_subject_of`, `state_is_fully_controlled_by_ROOT_or_subject`, `country_can_be_reasonable_target_of_wargoal`, `FROM_is_stronger`/`_weaker` | Diretamente aplicáveis à doutrina de expansão gydiana (influência, transferência segura de estado, elegibilidade de wargoal) sem reimplementar do zero. |
| Efeitos genéricos relacionados | `common/scripted_effects/00_scripted_effects.txt`: `instantiate_collaboration_government`, `abandon_colony_tag`, `get_best_alliance_match_<ideologia>_effect`, `civil_war_anti_exploiter_punitive_action` | Candidatos a reuso para fantoches/aliados/anexações da doutrina gydiana. |
| Prefixo `AZ_` (maiúsculo) já em uso ativo | `common/scripted_effects/AZ_info_effects.txt`, `AZ_lore_effects.txt`; `common/on_actions/AZ_info_on_actions.txt`; `common/ideas/AZ_*.txt` (7 arquivos); `common/scripted_guis/AZ_*`; `common/scripted_localisation/AZ_*`; múltiplos `localisation/AZ_*.yml` | Não colide com os 10 namespaces minúsculos propostos, mas confirma que o mod já mistura `AZ_` (arquivo, sistema de lore/info) com `az_` (namespace de evento) — o padrão do `05_ID_AND_FLAG_REGISTRY.md` (arquivo=`AZ_`, script=`az_`) já é seguido na prática pelo sistema de info/lore existente. |

### Estado numérico dos IDs de estado mencionados na lore

Confirmado diretamente em `history/states/`:

| Estado | Nome | Owner confirmado | Bate com a lore? |
|---|---|---|---|
| 86 | Doia | UPG | Sim |
| 400 | Haifa | UPG | Sim |
| 409 | Mominches | UPG | Sim |
| 361 | Karleston | KOZ (+ `add_core_of = GYE`) | Sim, owner bate; core de GYE é informação nova não coberta pela lore |
| 462 | Celest | Não auditado nesta rodada | — |
| 507 | (STATE_507) | DRM | **Não** — lore hipotetizava relação com expansão oriental |
| 508 | (STATE_508) | EDR | **Não** — idem |
| 509 | (STATE_509, "Net") | ORV | Parcialmente — é oriental, mas pertence a ORV, não a KAR ou LIA especificamente |

---

## 9. Bloqueadores para começar a Guerra das Três Bandeiras

Nenhum destes é uma correção pedida nesta rodada — são registrados como pré-requisitos técnicos para a próxima etapa de implementação:

1. **Nenhum mecanismo de início de guerra existe.** É preciso criar o efeito/evento que declara a guerra entre DTB, VRD e HEL (a lore já propõe fazer isso via evento com incidente ainda não nomeado, não via `declare_war_on` direto no history, ao contrário do padrão problemático usado em KOZ→TOL).
2. **HEL e ATV têm dados totalmente placeholder** (manpower=3 e 5, estados sem nome, sem capital narrativa definida). Nenhuma implementação militar séria deveria começar antes de resolver isso, conforme a própria ficha de HEL já recomenda.
3. **VRD e HEL têm ideologia de líder incoerente com o partido governante** (`communism`/`conservatism` e `neutrality`/`conservatism` respectivamente) — isso deveria ser corrigido antes de qualquer foco ou evento que dependa da ideologia do líder para lógica condicional.
4. **Nenhum dos quatro países (DTB/VRD/HEL/ATV) tem árvore de foco, decisões, eventos ou ideias nacionais próprias.** Toda a "Fase 1 — cadeia vertical mínima" descrita em `01_three_banners_war.md` está por construir do zero.
5. **Nenhuma tag ou mecanismo existe para "Helvaria reunificada".** Não há tag dinâmica, `form_Helvaria`, `change_tag` ou `set_cosmetic_tag` associado — apenas o padrão já usado por `form_Great_Thiryn` pode servir de modelo técnico.
6. **OOB de todos os quatro países é o placeholder genérico `standard_templates`**, compartilhado com outros 27 países — nenhuma divisão real está posicionada; uma guerra entre eles hoje resultaria em combate entre exércitos de milícia idênticos e sem frota.
7. **O padrão problemático de `declare_war_on` incondicional no boot (usado em KOZ→TOL) não deveria ser copiado** para a Guerra das Três Bandeiras — a lore já pede explicitamente um evento com escalada (janeiro–abril, maio–junho, estopim em junho–setembro), não uma declaração direta no history.
8. **Os patrocinadores externos (Novasovia→VRD, Gydian→HEL, Montia→DTB) não têm nenhuma variável de apoio implementada** (`az_three_banners_support_dtb/vrd/hel` são só flags conceituais em `docs/`).

---

## 10. Recomendações para a próxima rodada

*(Recomendações de auditoria, não implementação — nenhuma delas foi executada nesta rodada.)*

1. Decidir explicitamente o destino de `news.59`: remover (recomendado, é código morto que viola a regra 10 do canon) ou documentar formalmente por que permanece.
2. Revalidar as três ideologias inválidas (`Federalist`, `Divine_Throne`, `Nationalist`) contra `common/ideologies/00_ideologies.txt` — decidir se serão registradas como ideologias customizadas novas ou trocadas por uma já existente.
3. KAR não precisa de investigação sobre a ausência de estados — é intencional, conforme correção canônica registrada na seção 2 (arquipélago de Karyō ainda não criado). Quando o arquipélago for modelado no mapa, revalidar nesta ordem: recursos, portos e infraestrutura da nova massa terrestre; depois capital; depois OOB dedicado. Não usar território provisório nem estados de Orvena, Liangor ou do continente principal como solução temporária.
4. Corrigir a dupla inconsistência de ideologia em VRD e HEL (`communism`/`conservatism`, `neutrality`/`conservatism`) antes de qualquer trabalho de foco/evento que dependa disso.
5. Atualizar as fichas de país em `docs/lore/countries/` que referenciam arquivos de conflito/sistema/região por nome sem caminho, adicionando o diretório relativo correto (`../conflicts/...`, `../systems/...`, `../regions/...`) para tornar as referências navegáveis.
6. Ajustar `CZL.md` para citar `AZARYA_WORLD_CONTEXT_AUDIT.md` explicitamente em vez de "a auditoria histórica".
7. Antes de implementar a cadeia de cessão de Karleston, decidir formalmente se o `declare_war_on`/`annex_everything` em KOZ será mantido, substituído por um wargoal mais limitado, ou envolto por uma condição de disparo posterior ao boot.
8. Ao iniciar a implementação da Guerra das Três Bandeiras, seguir a ordem já recomendada em `04_CONTENT_IMPLEMENTATION_MATRIX.md` (padronizar IDs primeiro, depois cadeia vertical mínima) e reutilizar os triggers/efeitos genéricos listados na seção 8 deste relatório em vez de recriá-los.
9. Confirmar a identidade dos "Estados-bandidos" de Nirisia (candidatos ASV/RES/BLA/SHT) e a situação do estado 462 (Celest) — não cobertos nesta rodada.
10. Investigar a relação entre Sithius e Gydian mencionada na doutrina de expansão (dívida, concessões, arrendamento de portos) — hoje é puramente textual em `docs/lore/systems/gydian_expansion_doctrine.md`, sem nenhum reflexo em `history/states/`, decisões ou eventos.
