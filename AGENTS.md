# Azarya — Contexto e Lore do Mod

> Documento de referência permanente sobre o mundo, a linha do tempo e as intenções por trás do mod. Manter atualizado conforme a lore for sendo definida.

## O que é o mod

Total conversion para Hearts of Iron IV. Ambientação **realista** (não é fantasia), mas se passa em uma **linha do tempo alternativa** à nossa.

- **Nome atual do projeto/repositório: `Azarya`.** Historicamente o projeto principal se chamava `Azaryafantasia`, e existia uma pasta separada `Azarya` com um rascunho simples gerado por um gerador automático de mundos fantasiosos. O rascunho antigo foi apagado, e a pasta principal `Azaryafantasia` foi renomeada para `Azarya`, virando também um repositório Git (`github.com/AdriianCOE/Azarya`, branch `Main1`). Daqui pra frente, `Azarya` é a única fonte de verdade do projeto; `Azaryafantasia` só aparece em contexto histórico.
- Data de início da campanha: **1924** (em vez de 1936 como no HOI4 vanilla).

## Divergência histórica

- **Não houve** uma Primeira Guerra Mundial comparável à nossa.
- Ocorreu, sim, uma guerra comparável à nossa Segunda Guerra Mundial.

## O Grande Terremoto

Alguns anos antes do início do jogo (1924), um **terremoto de proporções catastróficas** devastou uma grande parte do mundo. Isso obrigou várias nações a entrarem em um processo de **reconstrução** — o que molda o estado econômico, político e territorial do mundo no ponto em que a campanha começa.

- Ano exato do terremoto: *a definir*
- Regiões/países mais afetados: *a definir*
- Efeitos de jogo previstos (ex: infraestrutura destruída, deslocamento de população, focos de reconstrução, recursos escassos): *a definir*
- Se o terremoto tem relação causal com a guerra tipo-Segunda-Guerra-Mundial (ex: disputas por recursos pós-desastre) ou é um evento independente: *a definir*

## Nações principais

*A definir — quais tags/países são os protagonistas da narrativa (até agora THK - Thiryn Kingdom e CZL - Czariado de Lesc são os mais desenvolvidos em termos de conteúdo, mas isso é estado de desenvolvimento do mod, não necessariamente definição de lore).*

## Ideologias e tensões geopolíticas

*A definir.*

## Tecnologia da época

*A definir — nível tecnológico equivalente a que década/momento histórico real.*

## Plano atual

**Objetivo imediato: estabilizar os logs (error.log) antes de partir para criação de conteúdo.**

A ideia é resolver os problemas técnicos que geram erros/avisos no log do jogo primeiro, para ter uma base limpa antes de expandir focus trees, eventos, tecnologia, etc. Candidatos prioritários a causar erro de log (ver diagnóstico abaixo, seção 5):

- `map/default.map` referencia `positions.txt`, que não existe.
- Evento `THK_azarya.txt` referencia GFX inexistente (`GFX_THK_marcha_militar_anual_de_thiryn`).
- `common/country_tags/01_countries.txt` com 0 bytes (pode ou não gerar erro, checar).
- 25 arquivos órfãos `D51–D75.txt` em `common/countries` sem tag correspondente.
- Tag de teste `TST.txt` esquecida em `common/characters`.
- `common/doctrines.disabled` e `common/focus_inlay_windows.disabled` — decidir se ativam (e adaptam) ou removem de vez.
- `common/scripted_guis/` vazia mas declarada no `.mod`.
- Nomes de arquivo com espaços/erros de digitação em `history/countries` (cosmético, mas vale padronizar).

Depois de rodar o jogo e confirmar o que efetivamente aparece no `error.log`, os itens acima serão repriorizados por impacto real (em vez de só suposição).

---

## Diagnóstico completo do estado atual (levantamento de 2026-07-13)

*Este é o relatório técnico de estado do mod, gerado por auditoria completa dos arquivos. Não é lore — é o estado de desenvolvimento/código. Mantido aqui para referência rápida sem precisar re-auditar tudo de novo.*

### Resumo executivo

| Área | Status | Observação principal |
|---|---|---|
| Mapa (map/) | ✅ Pronto/robusto | Mapa 100% customizado (bmp/csv próprios, ~34MB provinces.bmp), 506 estados |
| history/countries | ✅ Pronto/robusto | 57/57 países com conteúdo real (tech, personagens, política) |
| history/states | ✅ Pronto/robusto | 506 arquivos, todos preenchidos, 1 arquivo "cópia" perdido |
| common/countries + country_tags | ✅ Pronto/robusto | Todas as 57 tags mapeadas corretamente, sem tag órfã |
| common/characters | ✅ Pronto/robusto | 1 arquivo por tag, todos existem |
| common/national_focus | 🟡 Pela metade | Só 2 de 57 países têm árvore própria (THK e CZL); resto usa genérica |
| localisation/ | 🟡 Pela metade | Núcleo (países, estados, VPs) bem escrito; foco de CZL sem tradução alguma |
| events/ | 🔴 Vazio/não iniciado | ~100 arquivos-stub vazios (herdados da vanilla); só 1 evento próprio existe |
| history/general | 🔴 Vazio/não iniciado | 2 de 3 arquivos com 0 bytes |
| common/technologies | 🔴 Vazio/não iniciado (conceitualmente) | Conteúdo é a árvore tecnológica vanilla, sem adaptação |
| common/doctrines.disabled | ⚠️ Tem problema | 225KB de conteúdo real, mas desativado (extensão .disabled) |
| common/focus_inlay_windows.disabled | ⚠️ Tem problema | Arquivos ainda com nomes vanilla (cze/ger/jap), nunca adaptados |
| common/scripted_guis | 🔴 Vazio/não iniciado | Pasta com 0 arquivos, mas declarada no .mod |
| interface/AZ_texticons.gfx.disabled | ⚠️ Tem problema | Feature desativada, possivelmente esquecida |
| gfx/, music/, portraits/ | ✅ Pronto/robusto | Assets reais e volumosos (flags, loadingscreens, música) |
| tutorial/ | 🔴 Vazio/não iniciado | 1 arquivo de 1KB, não customizado (baixa prioridade) |

### 1. Levantamento por pasta

**common/ (visão geral).** Das ~80 subpastas, a maioria tem conteúdo real. Destaques:

- `common/units/`: 265 arquivos, 2.0MB — maior pasta, parece robusta.
- `common/country_leader/`: 4 arquivos, 416KB — denso.
- `common/dynamic_modifiers/`: 10 arquivos, 376KB.
- `common/technologies/`: 14 arquivos, 472KB, **literalmente os arquivos vanilla sem renomear** (`armor.txt`, `naval.txt`, `infantry.txt`, `MTG_naval.txt` etc.) — árvore de tecnologia não adaptada.
- `common/characters/`: 60 arquivos — 1 por tag (57) + `generic.txt` + `_documentation.txt` + `TST.txt` (tag órfã de teste).
- `common/national_focus/`: apenas 4 arquivos (ver seção 3).
- `common/country_tags/`: 3 arquivos — `00_countries.txt` (59 tags estáticas), `01_countries.txt` (0 bytes, vazio), `zz_dynamic_countries.txt` (tags dinâmicas D01-D50 para guerras civis).
- `common/scripted_guis/`: 0 arquivos — pasta completamente vazia, mesmo declarada no `.mod`.
- `common/doctrines.disabled/`: 25 arquivos, 225KB, estrutura completa (grand_doctrines, subdoctrines, tracks, folders, _documentation.md) — conteúdo substancial mas inativo.
- `common/focus_inlay_windows.disabled/`: 5 arquivos, nomes vanilla (`cze_industry_focus_inlay_window.txt`, `ger_inner_circle_inlay_window.txt`, `jap_imperial_influence_inlay_window.txt`) — nunca adaptados, desativado.
- `common/ideologies/`: 1 arquivo (`00_ideologies.txt`), 4 ideologias vanilla + 1 tipo customizado (`Merchant_Republic` dentro de democratic).
- `common/bookmarks/`: `1924.txt` e `1925.txt` reais e customizados (THK como país padrão); `blitzkrieg.txt` e `the_gathering_storm.txt` com 0 bytes (nomes vanilla esvaziados).
- `common/defines/`: `01_mod_defines.lua` define `MAX_PROVINCES = 25000`; `02_blankmod.lua` é template padrão Paradox.
- `common/ai_strategy/`, `common/ai_navy/`: nomes genéricos vanilla, não customizados por país.

**history/countries (57 arquivos).** Área robusta — todos com conteúdo substantivo (1,3KB–8KB): tecnologia inicial, `recruit_character`, popularidade de ideologias, líder/marechal/comandantes. Maiores: `THK - ThirynKingdom.txt` (8021B) e `CZL - Czariado de Lesc.txt` (6910B). Atenção: blocos `create_country_leader` (ex. em `ARK - Auralis.txt`) sem campo `name =` — checar se gera líder sem nome no log.

**history/states (506 arquivos).** Todos preenchidos (151–967 bytes). Nomeação inconsistente (`N-State_N.txt`, exceto `500-STATE_500.txt` em maiúscula); a maioria usa nome genérico "STATE_N" em vez de nome próprio.

**history/general.** Praticamente vazio: `china_shared_advisors.txt` e `generic_advisors.txt` com 0 bytes; `spain_shared_advisors.txt` com 3 bytes (só BOM UTF-8).

**map/.** 100% customizado: `provinces.bmp` (34,6MB), `heightmap.bmp`, `terrain.bmp`, `rivers.bmp`, `trees.bmp`, `world_normal.bmp`, `cities.bmp` (~11,5MB cada). `definition.csv`: 566KB. `adjacencies.csv`: 1,5KB. `map/strategicregions/`: 92 arquivos. `map/supplyareas/`: 358 arquivos. `map/terrain/`: 4 arquivos, 15MB. **`default.map` referencia `positions.txt`, que não existe** (há `unitstacks.txt` de 13,7MB como possível substituto moderno).

**localisation/ (15 arquivos .yml, só inglês).** Conteúdo real: `AZ_countries_l_english.yml` (1170 linhas/54KB, nomes por ideologia); `AZ_focus_l_english.yml` (239 linhas, **só focos de THK** — os 8 focos de CZL não têm nenhuma entrada); `AZ_state_names`, `AZ_victory_points`, `AZ_strategic_region_names`, `AZ_parties` — todos com conteúdo real.

**events/ (~100 arquivos).** Área mais fraca. Maioria são stubs vanilla vazios (0 ou 3 bytes): `Britain.txt`, `Germany.txt`, `Japan.txt`, `WTT_*`, `MTG_*`, `NSB_*`, `LaR_*`, `BFTB_*`, `DOD_*`, `TOA_*`, `TFV_*`, `BBA_*`, `AAT_*`. Únicos com conteúdo real: `Decisions_Events.txt` (10,5KB, mas referencia arte vanilla `GFX_report_event_hitler_handshake`), `THK_azarya.txt` (481B, único evento próprio do mod, ligado ao foco `THK_queensSpeech`), mais alguns pequenos (`debug_events.txt`, `GOE_Raj.txt`, `SEA_Japan.txt`, `LowCountries.txt`, `NewsEvents.txt`, `ss_recruitment_event.txt`, `stability_events.txt`, `treaty_orgs.txt`).

**gfx/, interface/, music/, portraits/, tutorial/.** `gfx/flags/`: 827 arquivos, 8MB. `gfx/loadingscreens/`: 27 arquivos, 116MB. `gfx/leaders/`: 72 arquivos, 3,9MB. `gfx/texticons/`: 8 arquivos, 6,9MB. `interface/`: 12 arquivos, 132KB, mas `AZ_texticons.gfx.disabled` desativado. `music/`: 13 arquivos, 33MB. `portraits/`: 58 arquivos (1 por tag + índices vanilla reaproveitados). `tutorial/`: 1 arquivo, 1KB, não customizado.

### 2. Tags de países × common/country_tags × common/countries

57 tags em `history/countries`: AEI, ARD, ARK, ASV, ATI, ATV, BKG, BLA, BOA, BOK, BOM, CBS, CMR, CZL, DKG, DKM, DRM, DTB, DUH, EDR, ELD, EYD, FVI, GET, GYE, HEL, INV, KES, KOZ, KRT, LUA, LUQ, LVD, MEK, MER, MOR, NIR, NSA, RES, RFB, RFO, SAH, SDB, SHT, SIT, SLU, SLV, SVD, THK, TOL, TRB, TRD, UPG, VAL, VAN, VRD, WIH.

Todas as 57 têm entrada correspondente em `common/country_tags/00_countries.txt` e resolvem para arquivo real em `common/countries/`. Nenhuma tag ausente ou quebrada.

`zz_dynamic_countries.txt` define 50 tags dinâmicas (D01–D50) reciclando 15 arquivos base (D01–D15). Mas `common/countries/` tem 75 arquivos D01–D75.txt — **D51 a D75 (25 arquivos) estão órfãos**.

### 3. common/national_focus (árvores de foco)

Apenas 4 arquivos:
1. `00_titlebar_styles.txt` (397B) — config visual, não é árvore.
2. `Lesc.txt` (CZL, 2,8KB) — **8 focos**, ramo de revolução comunista. Estágio inicial/esqueleto.
3. `Thiryn.txt` (THK, 26,8KB) — **~75 focos**, o mais desenvolvido: sucessão política, infraestrutura, educação, indústria, exército, aeronáutica, marinha.
4. `generic.txt` (49,7KB) — árvore genérica padrão, usada pelos outros 55 países, sem adaptação.

**Só 2 de 57 nações (3,5%) têm árvore de foco própria.**

### 4. Mapa e estados — detalhe

`default.map` aponta corretamente para `definition.csv`, `provinces.bmp`, `terrain.bmp`, `rivers.bmp`, `heightmap.bmp`, `trees.bmp`, `adjacency_rules.txt`, `adjacencies.csv`, `ambient_object.txt`, `seasons.txt` — todos existem, **exceto `positions.txt`**. `history/states/482-NO copy.txt` é um arquivo remanescente de cópia manual (funciona, mas nome desleixado).

### 5. Inconsistências concretas

1. `map/default.map` referencia `positions.txt`, que não existe.
2. Nomes divergentes: tag `ARK` = "Aurelia" (`common/countries`) vs "Auralis" (`history/countries`); tag `LUA` = "Luradia" vs "Lurandia".
3. `482-NO copy.txt` em `history/states/` — nome de cópia esquecida.
4. 25 arquivos órfãos `D51.txt`–`D75.txt` em `common/countries/`.
5. `common/characters/TST.txt` — tag de teste sem entrada em `country_tags` nem `history/countries`.
6. `common/country_tags/01_countries.txt` — 0 bytes.
7. `common/doctrines.disabled/` — 225KB de conteúdo estruturado, totalmente inativo.
8. `common/focus_inlay_windows.disabled/` — nomes vanilla não adaptados, nunca trabalhados.
9. `interface/AZ_texticons.gfx.disabled` — feature desativada/abandonada.
10. `common/scripted_guis/` — vazia mas declarada em `replace_path` no `.mod`.
11. Focos de CZL sem localização nenhuma (`CZL_Unfinished_Revolution`, `CZL_Shadow_Council` etc. — 0 ocorrências em `AZ_focus_l_english.yml`).
12. Evento `THK_azarya.txt` referencia `GFX_THK_marcha_militar_anual_de_thiryn`, não encontrado em nenhum `.gfx`.
13. `events/Decisions_Events.txt` usa arte vanilla real-histórica (`GFX_report_event_hitler_handshake`), destoando do mundo fantasioso.
14. `history/general/china_shared_advisors.txt` e `generic_advisors.txt`: 0 bytes; `spain_shared_advisors.txt`: só BOM.
15. `common/bookmarks/blitzkrieg.txt` e `the_gathering_storm.txt`: 0 bytes.
16. Erros de digitação em nomes de arquivo `history/countries/`: `"ATI- Attica.txt"`, `"SLV- Sylvan.txt"`, `"LUQ -  Luquitos.txt"` (cosmético).
17. Azarya e Azaryafantasia compartilham exatamente as mesmas 57 tags — colisão garantida se ativados juntos (não é bug, mas atenção).
18. Várias subpastas de `common/` com conteúdo real (`ai_strategy`, `ai_navy`, `ai_peace`, `ai_faction_theaters`, `ideologies`, `game_rules`, `idea_tags`, `technology_tags`, `terrain`, `organizations`, `special_projects`, `state_category` etc.) não aparecem na lista de `replace_path` do `.mod` — normalmente ok se os nomes de arquivo coincidem com os vanilla, mas não confirmado pasta a pasta.

### 6. Arquivos .mod

- `Azaryafantasia.mod` (launcher) e `Azaryafantasia/descriptor.mod` (workshop) consistentes entre si: ~55 `replace_path`, `version="0.1"`, `supported_version="1.19.*"`, tags Alternative History / Map / Total Conversion.
- `Azarya.mod`: mais enxuto, `name="Fantasy World"`, mesma `supported_version`, só ~24 `replace_path` (sem national_focus, doctrines, focus_inlay_windows, events) — confirma que é o rascunho/gerado automaticamente.

### 7. localisation/ — quantitativo

15 arquivos .yml, todos `l_english` (nenhum outro idioma): `AZ_countries` (1170L/54,2KB), `AZ_focus` (239L/20,7KB), `AZ_victory_points` (339L/12,1KB), `AZ_state_names` (451L/11,5KB), `AZ_strategic_region_names` (232L/9,0KB), `AZ_parties` (84L/8,3KB), `AZ_bop` (63L/3,4KB), `AZ_characters` (33L/3,4KB), `AZ_ideas` (33L/3,1KB), `AZ_bookmarks` (26L/4,3KB), `AZ_adjacency_rules` (44L/2,9KB), `AZ_loading_tips` (11L/1,0KB), `AZ_events_THK_azarya` (5L/471B), `AZ_music_station` (7L/255B), `AZ_version` (4L/130B). Conteúdo real e bem escrito (ex.: `KRT_communism: "People's Republic of Kareth"`), exceto a lacuna de localização dos focos de CZL (item 11 acima).

### Conclusão do diagnóstico

O mod tem fundação de mapa e países muito mais sólida do que a árvore de pastas sugere à primeira vista — mapa 100% autoral, 57 países com history real, 506 estados preenchidos. O gargalo está em conteúdo de jogabilidade específico: só 2 árvores de foco customizadas (de 57), quase nenhum evento próprio, tecnologia 100% vanilla, e dois sistemas inteiros (doutrinas, focus inlay windows) construídos mas desligados via `.disabled`. Sugere investimento pesado em worldbuilding/mapa/lore inicial (THK e CZL na frente) que ainda não escalou para o restante das 55 nações nem para eventos.

> **Nota:** por pedido do usuário, states e provinces (`history/states/`, `map/definition.csv` etc.) não precisam ser relidos em diagnósticos futuros — já confirmados como preenchidos/robustos nesta auditoria.

---

## Investigação de crash real (2026-07-13) — pós-reorganização `Azaryafantasia` → `Azarya`

*Esta seção documenta a investigação do crash determinístico ao iniciar a campanha de THK em 1924, incluindo a reorganização do projeto (rascunho antigo apagado, pasta principal renomeada para `Azarya`, virou repositório Git). Mantida como registro histórico da investigação — não é lore.*

### Contexto da reorganização

- O projeto principal (antes `Azaryafantasia`) foi renomeado para `Azarya` e virou o repositório Git atual (`github.com/AdriianCOE/Azarya`, branch `Main1`). O rascunho antigo (`Azarya` gerado automaticamente) foi apagado.
- O `error.log`/`game.log`/`crashes/` analisados foram gerados jogando este mesmo projeto, antes da renomeação — são evidência válida da linhagem atual, mas podem ser anteriores a correções já presentes no HEAD.

### Classificação dos problemas conhecidos (log antigo × HEAD atual)

| Problema | Estava no log antigo? | Status no HEAD atual |
|---|---|---|
| `START_DATE`/`END_DATE` = 1984/1999 em `common/defines/02_blankmod.lua` (arquivo-molde nunca editado, sobrescrevia a data por ordem alfabética de carregamento) | Sim | **JÁ CORRIGIDO** — linhas removidas |
| Construção duplicada (naval_base da província 1159) no `history/states/506-STATE_506.txt` — 1159 pertence de verdade ao state 212, que já tem a atribuição legítima | Sim | **JÁ CORRIGIDO** — bloco duplicado removido |
| Chave faltante em `history/units/ASV.txt` (2ª divisão nunca fechava antes da 3ª abrir, aninhamento inválido) | Sim | **JÁ CORRIGIDO** — estrutura igual ao `ARD.txt` |
| `map/positions.txt` ausente (referenciado em `default.map`, vanilla também usa um arquivo vazio) | Sim (sem erro explícito) | **JÁ CORRIGIDO** — arquivo vazio criado |
| `GUI_TYPE` `change_background`/`country_filter` indefinidos — `interface/frontendmainview.gui` e `frontendgamesetupview.gui` do mod são cópias desatualizadas (faltam elementos que o vanilla 1.19.2 atual define) | Sim | Overrides renomeados para `.gui.disabled_test` (frontend vanilla deve assumir) — **hipótese principal do crash, ainda não comprovada, depende do próximo teste** |
| `gfx/loadingscreens/load_ncns_jap.dds` — "Unexpected token: DDS" | Sim | **JÁ CORRIGIDO por ausência** — arquivo não existe mais, sem referência em lugar nenhum |
| `gfx/loadingscreens/load_2.dds`/`load_5.dds`/`load_6.dds` — na verdade JPEGs com extensão `.dds` | Não (achado nesta reauditoria) | **AINDA PRESENTE** — sem referência explícita encontrada em `.gfx`/`.gui`/`.asset`/`.txt`, carregamento pelo engine não determinado — candidato do Round 2, não mexido ainda |
| Manifesto externo `mod/Azarya.mod` desatualizado (`name="Fantasy World"`, ~24 `replace_path`, sobra do rascunho antigo nunca sincronizada) | Não é erro de log, consequência da renomeação | **CORRIGIDO nesta rodada** — reescrito espelhando `descriptor.mod` |
| `replace_path="common/collections"` / `"common/focus_inlay_windows"` removidos numa rodada anterior por engano (o vanilla tem conteúdo real nas duas pastas — removê-los deixaria vazar CZE/GER/JAP focus inlay windows e o sistema de collections vanilla) | Não é erro de log | **CORRIGIDO nesta rodada** — restaurados em `descriptor.mod` e no manifesto externo |
| `interface/_backup_original/*.gui` — cópias com extensão carregável dentro de `interface/`, redundantes com o Git e arriscando duplicar definição de GUI_TYPE | Não existia no log antigo | **CORRIGIDO nesta rodada** — pasta removida (`git rm -r`), backup fica só no histórico do Git e no `.gui.disabled_test` |

### Achado crítico: dessincronia entre o launcher e a pasta renomeada

O banco do Paradox Launcher (`launcher-v2.sqlite`) tinha o playset ativo apontando para `mod/Azaryafantasia.mod` / `dirPath=...\mod\Azaryafantasia` — **caminho que não existe mais** depois da renomeação. Isso não foi editado (é estado de outro aplicativo, fora do repositório) — **o usuário precisa, no Paradox Launcher: remover a entrada antiga quebrada e adicionar/ativar a entrada atual apontando para a pasta `Azarya`** antes do próximo teste.

### `tools/validate_mod.py`

Reescrito com 10 checagens (manifesto externo × `descriptor.mod`, `replace_path` órfão, `.gui`/`.gfx` em pastas de backup, header DDS, building fora do state / província duplicada entre states via parsing por profundidade de chaves, balanceamento de chaves, tags/country files/history sem correspondência, focus/event IDs duplicados), classificadas em `ERROR`/`WARNING`/`INFO`, saída não-zero só com `ERROR`. Resultado após o Round 1: **3 ERROR** (os 3 DDS já conhecidos, reservados para o Round 2), **72 WARNING** (a maioria são os 25 arquivos órfãos `D51`–`D75.txt` já documentados antes, mais `common/collections`, `country_metadata` e `gfx/interface/equipmentdesigner/graphic_db` sem pasta ativa nem `.disabled` — não investigados a fundo ainda, não bloqueiam o teste desta rodada).

### Próximo passo (Round 1)

Checklist de teste manual (ver conversa/plano para o passo a passo completo): reconfigurar o mod no Paradox Launcher apontando para `Azarya`, desativar os demais mods, iniciar THK → 1924, e confirmar se a campanha chega ao mapa jogável. Se sim, o conjunto de correções acima resolveu o crash (sem isolar uma causa única, já que várias mudaram juntas). Se ainda fechar, o próximo passo isola só os 3 DDS corrompidos, sem mexer em mais nada.

---

## Rodada 2 (2026-07-13) — state 506 (capacidade de buildings) + sprites de frontend

*O usuário testou de novo depois da Round 1: o launcher já reconhece `Azarya` corretamente (`system.log`: "Active Mod: Azarya"), a data cai em 1936 (fallback vanilla, não mais 1984). Mas **o jogo ainda fechou** — novo crash `crashes/hoi4_20260713_025250/`, `EXCEPTION_ACCESS_VIOLATION`, com a pilha de chamadas **idêntica offset a offset** à do crash da Round 1 (mesma rota determinística, ainda não eliminada). Confirmado no novo `error.log`: sem `Undefined GUI_TYPE`, sem erro em `ASV.txt`, sem `Province #1159`, sem `1984.01.01.12`, sem `load_ncns_jap.dds` — a Round 1 funcionou parcialmente, mas restam problemas.*

### P0 — state 506, segundo bug independente (corrigido)

O log ainda terminava em `506 - Net has too many buildings : -1`. A remoção do bloco duplicado da província 1159 (Round 1 anterior a esta reorganização) resolveu só um dos dois bugs desse state — este é outro, novo.

Diagnóstico: `state_category=town` fornece `local_building_slots=4` (`common/state_category/town.txt`). Somando os níveis dos 4 tipos de building de state em `history/states/506-STATE_506.txt` (`infrastructure=2, arms_factory=2, industrial_complex=3, air_base=1`) dá **8** — o valor mais alto entre **todos os 242 states com `state_category=town` do mod** (o segundo mais alto, state 410, soma 7 e não gera erro; a maioria fica entre 0 e 5). `naval_base` é building **provincial** (`level_cap.province_max`), não conta contra `local_building_slots`. Não achei nenhuma segunda ocorrência do erro "too many buildings" em nenhum outro state do mod.

Não há acesso ao código-fonte do engine para confirmar a fórmula exata, mas a evidência empírica (soma=8 sendo o único outlier claro, teto seguro observado = 7) é forte o suficiente para uma correção mínima: **`industrial_complex` reduzido de `3` para `2`** em `history/states/506-STATE_506.txt`, trazendo a soma para 7. Não mexeu em `provinces`, `owner`, `victory_points`, `naval_base` nem em nenhum arquivo de mapa.

### P1 — sprites ausentes no frontend (diagnosticado, correção reservada)

Novo no log: `GFX_subscription_widget_chinese`, `GFX_country_filter_entry`, `GFX_unplayed_content_notification` ausentes. Causa: a Round 1 desativou só os `.gui` de frontend (`frontendmainview.gui.disabled_test`, `frontendgamesetupview.gui.disabled_test`), mas os `.gfx` companheiros (`interface/frontendmainview.gfx`, `interface/frontendgamesetupview.gfx`) continuam **ativos e são cópias antigas** (mesmo nome do vanilla, sobrescrevem por completo): faltam 9 e 4 sprites respectivamente que o vanilla atual (1.19.2) define, incluindo os 3 do log. `frontendgamesetupview.gfx` não tem nenhum sprite próprio do mod; `frontendmainview.gfx` tem só um (`GFX_frontend_az_dev_logo`), hoje órfão (só era referenciado pelo `.gui` já desativado). **Não corrigido ainda** — reservado para depois do teste do state 506, conforme pedido.

### `radio_station_cover.dds` — classificado

`Couldn't find texture file: 'gfx/radio_station_cover.dds'` é referência do **próprio mod** (`interface/AZ_music.gfx` → `GFX_radio_station_cover`, usado em `interface/AZ_music.gui`, o player de música customizado). Não é vanilla, DLC nem outro mod Workshop — é um asset de textura que nunca foi adicionado ao mod. Cosmético (capa do widget de música), não tratado como bloqueador. Não corrigido nesta rodada.

### DDS conhecidos

`load_2.dds`, `load_5.dds`, `load_6.dds` continuam intocados — ainda não aparecem no `error.log`.

### Próximo passo (Round 2)

Testar THK → 1924 de novo. Se chegar ao mapa: a correção do state 506 era suficiente (P1 pode nem precisar ser corrigido se não estiver gerando problema real). Se ainda fechar: comparar a pilha de chamadas do novo crash com `hoi4_20260713_025250` — se mudar, o state 506 era parte do problema e a próxima camada (P1, sprites) deve ser corrigida; se ficar idêntica, o state 506 não era a causa principal e é preciso investigar mais fundo antes de mexer nos `.gfx`.

---

## Rodada 3 (2026-07-13) — teste A/B completo do frontend (`.gfx`)

*Novo teste confirmou, de forma independente (reli o log fresco `errornovo.log` e o novo `crashes/hoi4_20260713_032139/`): `506 - Net has too many buildings` **não aparece mais** — o fix do state 506 (Round 2) funcionou e foi preservado. O crash continua, com a mesma pilha de chamadas idêntica (offset a offset) às rodadas anteriores — mesma rota determinística ainda não eliminada. O log trouxe exatamente as contagens esperadas: `GFX_subscription_widget_chinese` (1x), `GFX_country_filter_entry` (9x), `GFX_unplayed_content_notification` (8x) ausentes — confirmando o diagnóstico do P1 da Rodada 2.*

### Ação: desativados os `.gfx` companheiros

`interface/frontendmainview.gfx` → `frontendmainview.gfx.disabled_test`, `interface/frontendgamesetupview.gfx` → `frontendgamesetupview.gfx.disabled_test`. Os `.gui` continuam desativados de antes. **Os 4 arquivos de frontend do mod (2 `.gui` + 2 `.gfx`) estão todos desativados agora** — o jogo deve usar o `frontendmainview`/`frontendgamesetupview` (`.gui` + `.gfx`) 100% vanilla. Nenhuma cópia com extensão carregável ficou em subpasta (`_backup_original` já tinha sido removida na Round 1).

### `radio_station_cover.dds` — reclassificado com o log novo (mesma conclusão)

Investigação somente-leitura repetida com o log atual: sem `common/radio` no mod nem no vanilla; a única referência em todo o mod/vanilla/mods Workshop carregados continua sendo `interface/AZ_music.gfx:4` (`textureFile = "gfx/radio_station_cover.dds"`) e `interface/AZ_music.gui:120`. Os 3 mods Workshop ativos (`3707251866` HOI4 Fantasy World Map Maker, `3711359350` Focus Tree Editor, `3716626471` HOI4 ContentMaker) são ferramentas de desenvolvimento, não têm conteúdo de rádio, e não referenciam esse nome. **Confirmado: é asset do próprio mod, nunca adicionado.** Não corrigido — aguardando resultado deste teste, conforme pedido.

### Próximo passo (Round 3)

Testar THK → 1924. Se chegar ao mapa: os `.gfx` antigos eram a causa restante. Se ainda fechar: comparar a pilha de chamadas do novo crash com `hoi4_20260713_032139` (se mudar, avançamos mais uma camada; se ficar idêntica, o frontend não era a causa principal e a investigação precisa mudar de direção — possivelmente `radio_station_cover.dds` ou algo ainda não identificado).

---

## Rodada 4 (2026-07-13) — redução estrutural do error.log

*O teste da Round 3 confirmou `506 - Net has too many buildings` ausente (fix preservado) mas o crash persistiu. Em vez de investigar mais o crash em si, esta rodada limpa as famílias de erro mais repetitivas do `error.log` (`errornovo.log`, 4437 linhas brutas / 3821 entradas lógicas), priorizadas por impacto real, não por sistema.*

### `tools/summarize_error_log.py` (novo)

Script read-only que lê o log, mescla continuações multilinha, e agrupa por assinatura detalhada (preserva IDs específicos: tech, idea, tag, sprite, specialization, trigger) e por família ampla (`invalid_technology_reference`, `invalid_idea_reference`, `invalid_specialization`, `missing_country_tag`, etc.). Gera `tools/reports/error_log_summary_baseline.md`. Rodar: `python tools/summarize_error_log.py <log> [--markdown <arquivo>]`.

### Achados e correções (investigação a fundo antes de qualquer edição, git log checado antes de copiar do vanilla)

- **`common/ai_strategy/doctrines.txt` (1596 linhas do log, ~42%)**: eram só **14 linhas distintas** usando sintaxe antiga de doutrinas (`has_tech = mobile_warfare` etc., de antes do rework de doutrinas do HOI4). Mapeadas contra o vanilla atual (`common/doctrines/grand_doctrines/`, `subdoctrines/`) e migradas para `has_doctrine =`/`has_completed_subdoctrine =`. 9 de 14 com correspondência direta confirmada; 5 (`large_front_operations`, `air_superiority`, `day_bombing`, `formation_flying`, `force_rotation`) sem subdoctrine exata identificável — usei o doctrine pai como aproximação razoável (só afeta peso de decisão de IA, não corretude de jogo).
- **`BUL_army_restrictions_aat` (593 linhas, ~15%)**: os 6 arquivos de equipment (`tank_chassis.txt`, `plane_airframes.txt`, `ship_hull_{submarine,light,heavy,cruiser}.txt`) eram **100% idênticos ao vanilla** (0 diff). O bloco `can_be_produced` checava uma idea da Bulgária vanilla que não existe no Azarya (`common/ideas` é 100% autoral). Removidos os 15 blocos (mecânico, script com preview antes de aplicar). **Achado à parte, não corrigido**: outros ~10 arquivos de equipment (`ballistic_missiles.txt`, `nuclear_missiles.txt`, `ship_hull_carrier.txt` etc.) têm o mesmo padrão mas não apareceram no log atual — fica para uma rodada futura se aparecerem.
- **Specializations/special projects (~979 linhas)**: **checei `git log --all` antes de copiar do vanilla**, como pedido. Achado importante: `common/special_projects/projects/air_projects.txt` tinha **customização real do Azarya** (troca de `original_tag = GER`→`CZL`, remoção de efeitos da Alemanha, renome de tech de motor a jato) no commit `e8bbf9d3`, perdida no commit seguinte `6124b77d` ("voltamos la v1", aparente squash/revert acidental). Recuperado desse commit, não do vanilla — copiar do vanilla teria apagado essa customização. Os outros 6 arquivos vazios (`specializations.txt` + 5 `prototype_rewards/generic_*.txt`) eram idênticos ao vanilla no commit `56511bd5`, recuperados de lá.
- **`common/ai_navy` sem `replace_path`**: única pasta `ai_*` sem essa entrada; `fleet/`/`taskforce/` só tinham placeholder, então os 8 arquivos vanilla continuavam carregando (~117 linhas do spam de tags). Adicionado `replace_path="common/ai_navy"` nos dois manifestos.
- **`common/factions/templates` e `common/factions/rules`**: `replace_path="common/factions"` só cobre o nível do pai (confirmado, não cascade pra subpastas — mesmo comportamento non-recursivo já visto em `map/`). Essas duas subpastas não existem no mod, então o vanilla (10+9 arquivos, `USA.txt`, `axis.txt`, `joining_rules.txt` etc.) carregava inteiro. Em vez de criar 19 stubs vazios (padrão já usado em `factions/goals/`), adicionei `replace_path="common/factions/templates"` e `="common/factions/rules"` diretamente — mesmo efeito, menos manutenção, precedente idêntico já existe em `common/scripted_guis` (replace_path + pasta vazia).
- **`common/characters/DKM.txt`**: typo `original_tag = DMK` → `DKM` (40 ocorrências, incluindo os prefixos de ID dos personagens `DMK_ar`→`DKM_ar` etc.). Achado bônus: isso também é a causa dos 20 erros `recruit_character: Unknown character` — `history/countries/DKM - Duskmoor.txt` já chamava `recruit_character = DKM_ar` (certo), mas os personagens estavam definidos como `DMK_ar` (errado). Uma correção resolveu as duas famílias.

### Não corrigido nesta rodada (adiado, confirmado sem bloquear o próximo teste)

`common/raids/*` (is_literally_china, bathe_in_hellfire, the_great_wall), `common/technology_sharing/12_wuw_tech_sharing_groups.txt` (grupo Habsburg + trigger órfão `BEL`), `common/country_leader/00_traits.txt` (blocos residuais tipo `imperial_sanction`, 18k linhas, precisa de sub-rodada dedicada), `common/units` (`fire_support.txt`/`hq_support.txt` ausentes + seções cortadas em `sp_anti-air_brigade.txt`/`tank_destroyer_brigade.txt`, causa das 63 linhas de "Unexpected token" em doutrinas), `common/ai_equipment` (blocked_for de país vanilla, ~234 linhas), `coal` (recurso removido mas `industry.txt` ainda referencia, decisão de design pendente), ~10 arquivos de equipment com `BUL_army_restrictions` não vistos no log atual.

### Validador e redução esperada

`tools/validate_mod.py`: 3 ERROR (os 3 DDS já conhecidos, intocados), 74 WARNING (72 de antes + 2 novos, esperados, dos `replace_path` de `factions/templates`/`rules`), 0 divergência entre manifestos.

Famílias tratadas nesta rodada somam **~3285 das 3821 entradas lógicas da baseline (~86%)**: `has_tech: Invalid tech` (1596), `BUL_army_restrictions_aat` (593), specialization/special projects (~979), parte do spam de tags via `ai_navy` (~117).

### Próximo passo (Round 4)

Testar THK → 1924 de novo. O próximo `error.log` deve ficar bem menor — aí dá pra ver com clareza se o crash ainda tem uma causa própria não relacionada a esse ruído, ou se alguma das correções desta rodada also mexeu nele (não há garantia, o objetivo aqui era limpeza de log, não o crash em si). Comparar `crashes/` de novo pela pilha de chamadas.

---

## Rodada 5A (fora desta sessão) — resultado

Teste runtime mais longo até agora: **THK/Thiryn iniciou em 1924, avançou até 3 de fevereiro sem crash, save criado com sucesso.** OOB, variantes aéreas e texticons foram corrigidos nessa rodada (detalhes não documentados aqui, aconteceram fora desta conversa) — **não foram tocados na Rodada 5B**, confirmado via `git status` (nenhum arquivo em `common/units` ou `interface/AZ_texticons*` no diff).

## Rodada 5B (2026-07-13) — traits soviéticos residuais + fallback de portraits

*O novo `error.log` (96KB, 666 linhas) veio bem menor graças às rodadas anteriores. 443 das 666 linhas eram só duas ideias soviéticas inexistentes; o resto eram problemas pontuais de portrait/personagem.*

### P0 — `SOV_purged_junior_army_officers_3` / `SOV_purged_junior_navy_officers_3` (443 linhas → 0)

As duas ideias existem no vanilla (`common/ideas/SOV.txt`, expurgos de Stalin) mas não no Azarya (sem URSS). Apareciam em 24 blocos `new_commander_weight` (11 army + 13 navy) de traits **genéricas** (`old_guard`, `brilliant_strategist`, `inflexible_strategist` etc. — não são traits soviéticas, são traits de personalidade comuns), como mais um `modifier = { FROM = { has_idea = X } factor = 0 }` entre vários (ao lado de `best_of_the_best_spirit`/`academy_scholarships_spirit`, que existem no mod e foram preservados). Removidos os 24 blocos de 4 linhas (96 linhas no total), nada mais tocado em `common/unit_leader/00_traits.txt` (747 chaves antes e depois — balanceado).

### P1-A/B — fallback de portrait e 4 portraits de THK (causa real: formato, não nome de arquivo)

Comparei o DDS real (não só existência) do fallback `gfx/leaders/leader_unknown.dds` (herdado do vanilla, sem `replace_path` em `gfx/leaders`) e dos 4 portraits problemáticos (`Thaddeus_Ironwood.dds`, `Adric_Von_Drachen.dds`, `Lysandra_Ardent.dds`, `Magnus_Goldcrest.dds`, criados via `create_field_marshal`/`create_corps_commander`/`create_navy_leader` com `picture=` legado em `history/countries/THK - ThirynKingdom.txt`) contra um portrait confirmado funcional na mesma pasta (`Portrait_Germany_Kurt_Student.dds`, cópia do vanilla, 0 erro): todos têm as mesmas dimensões (156×210), mas os problemáticos são **RGBA 32-bit não comprimido** enquanto o funcional é **DXT1 comprimido**. `character_manager.cpp` não consegue derivar o portrait pequeno a partir do formato RGBA não comprimido.

Reconvertidos para DXT1 via Pillow (12.2.0, disponível no ambiente): `gfx/leaders/leader_unknown.dds` (novo, gerado a partir do original vanilla — mesma imagem, só reformatada) e os 4 arquivos de THK, in-place, mesmo conteúdo visual e dimensões. **Nota**: esses arquivos são `.dds`, cobertos pelo `.gitignore` (`*.dds`) — não aparecem em `git status`, mas estão no disco.

### P1-C — personagem "sumido" em Ironvale

Não estava sumido — `common/characters/INV.txt` tinha `INV_democrINVc_guy` em vez de `INV_democratic_guy` (find-replace malfeito trocou "ati" por "INV" dentro de "democr**ati**c_guy"). Único caso desse tipo no arquivo (conferido contra os outros 19 personagens). Corrigido (2 ocorrências).

### P2 — placeholder AEI (melhor esforço, a confirmar)

`history/countries/AEI - Aelosia.txt` referenciava `Portrait_PLACEHOLDER_2_large.dds`, que nunca existiu (nome já indica arte não finalizada). Trocado para `picture = "gfx/leaders/leader_unknown.dds"` (o fallback central recém-corrigido). **Sem precedente no mod** de `picture=` com caminho completo apontando pra fora da pasta da própria tag — não é 100% certo que o engine aceita esse override de caminho; confirmar no próximo teste se Aelosia mostra o silhouette genérico em vez de erro.

### Validador

3 ERROR (os mesmos 3 DDS conhecidos de sempre, intocados), 76 WARNING (nenhum novo relacionado a esta rodada), 0 divergência de manifesto. Nenhum dos 5 `.dds` recodificados apareceu na checagem de header DDS (confirma que a conversão pra DXT1 produziu headers válidos).

### Próximo passo (Round 5B)

Carregar o save de 3 de fevereiro de 1924, avançar ≥7 dias, abrir Officer Corps e conferir os portraits (THK principalmente + Aelosia), salvar de novo, e checar se `SOV_purged_junior_*_officers_3` sumiu do novo `error.log`.

---

## Rodada 5C (2026-07-13) — reconstrução segura do frontend Azarya

*Existiam 4 overrides antigos de frontend desativados (`interface/frontend{mainview,gamesetupview}.{gui,gfx}.disabled_test`) — cópias antigas e quebradas do frontend vanilla. Objetivo: recuperar o branding real do Azarya sem reativá-los.*

### Achado principal: a maior parte do branding já estava ativa, silenciosamente

`gfx/interface` não é `replace_path`'d. O mod tem vários arquivos de textura com o **mesmo nome relativo** que sprites já definidos no `.gfx` vanilla ATIVO referenciam — mesmo mecanismo de sobreposição por nome de arquivo já visto na Rodada 5B (portraits). Confirmado sprite a sprite: `GFX_frontend_game_logo` (→ `logo_game.dds`, autoral), `GFX_play_button_ready`, `GFX_tiled_frontend_upper_bar`, `GFX_tiled_frontend_lower_bar`, `GFX_mini_country_selector` (todos na tela de seleção de cenário) e o bookmark de 1924 (`GFX_select_date_1924`, definido em `AZ_Bookmark.gfx`, ativo) **já estavam mostrando arte própria do Azarya, sem eu editar nada**. `GFX_frontend_dev_logo` (logo "dev") tinha um arquivo do mod com o mesmo nome, mas era cópia byte-a-byte do vanilla (SHA1 igual) — sem efeito visual.

Único sprite genuinamente órfão: **`GFX_frontend_az_dev_logo`** (`gfx/interface/az_dev_logo.dds`, 128×192 DXT5, válido) — sem nome vanilla equivalente pra sobrepor por acidente, só definido no `.gfx` antigo desativado.

### Bugs do `frontendmainview.gui.disabled_test` confirmados (não reproduzidos)

Chave final ausente (`social_view_interface_window` nunca fechada antes de `first_row` abrir, cascateando até faltar o fechamento de `guiTypes`), background duplicado em `mainmenu_single_player`, `career_profile_button`/`credits_button` sobrepostos em y=138 (deveria ser y=218), painel de 20 faixas fixas assumindo 1920×1080 (fundo animado sem responsividade), `privacy_policy_button` com coordenadas de um container diferente do seu pai real (estourando a área), e 4 dos 6 links hardcoded (`forum`/`facebook`/`twitter`/e o workshop) confirmados como institucionais do HOI4 vanilla, não do Azarya.

`frontendgamesetupview.gui.disabled_test`: os 4 hacks (`y=2200`, `y=-3300`, `width=2000%%`) confirmados — só escondiam elementos (retrato de líder, grid médio, segundo bookmark), não devem voltar. Sem nenhum branding autoral hardcoded. Vanilla atual ganhou `country_filter`/`filters`/`more_countries`, que não existiam no arquivo antigo.

### Ação tomada (bem menor que uma reconstrução completa, por causa dos achados acima)

1. **`interface/AZ_frontend_brand.gfx`** (novo) — só define `GFX_frontend_az_dev_logo`. Sem colisão com nenhum `.gfx` ativo.
2. **`interface/frontendmainview.gui`** (novo — cópia exata do vanilla atual, 732→756 linhas, + 3 edições pontuais): (a) o ícone `frontend_dev_logo` passa a usar `GFX_frontend_az_dev_logo` em vez de `GFX_frontend_dev_logo` (mesma posição/slot do vanilla, sem apagar a definição vanilla original); (b) 2 `instantTextBoxType` novos perto do logo do jogo, reaproveitando as chaves de localisation já existentes (`AZ_MOD_VERSION`, `compatible_game`) que antes só ficavam penduradas no arquivo desativado; (c) nada mais — todos os widgets essenciais (DLC, subscription, achievements, change_background, friends_button etc.) ficam idênticos ao vanilla atual.
3. **`localisation/AZ_version_l_english.yml`**: `compatible_game` atualizado de "v1.16.9" (desatualizado) para "v1.19.*" (versão instalada).
4. **`frontendgamesetupview.gui`/`.gfx`**: **não criados**. A tela já mostra 100% do branding autoral real (via sobreposição de textura já ativa) e já tem mais funcionalidade que o arquivo antigo — reconstruí-la seria regressivo.
5. **Não incluído**: selo Alpha (sem asset próprio, nunca existiu — a referência já estava comentada no arquivo antigo), fundo animado de 20 faixas (é o próprio bug a não reproduzir), links sociais (reddit/discord podem estar desatualizados/expirados, sem forma de confirmar — fica pendente até o usuário confirmar links atuais).
6. Os 4 arquivos `.disabled_test` continuam intocados.

### Validador e verificação

3 ERROR (mesmos DDS conhecidos), 76 WARNING (nenhum novo desta rodada), 0 divergência de manifesto. Chaves balanceadas nos 2 arquivos novos (204/204 e 2/2, excluindo comentários). Nenhuma colisão de sprite ID. Confirmado por `git status` que `AZ_texticons.gfx`, `history/countries/THK`, `history/units/THK.txt`, `gfx/leaders` não foram tocados nesta rodada.

### Próximo passo (Round 5C)

Testar: menu principal (logo, texto de versão, logo de dev trocado) → Continue → Singleplayer → THK → bookmark 1924 → Game Rules → campanha → Load Game → Options → sair. Testar em 1366×768 e 1920×1080. Preservar logs e `crashes/` mais recente.

---

## Rodada 5D (2026-07-14) — correção direta dos erros restantes

*Mod já estável (menu animado ok, THK inicia, campanha avança, save funciona, sem crash). Objetivo: reduzir o `error.log` restante (`countrytag.cpp:135`, `INS_underground_revolution`, colisões de `text.log`, comandos navais descartados), sem tocar em assets nem nos itens explicitamente ignorados pelo usuário (portraits/flags ausentes, discrepância bitmap/província).*

### Task 1 — `countrytag.cpp:135` (139 ocorrências, 114 tags distintas)

**Achado arquitetural**: `common/doctrines` está inteiramente desativado (`common/doctrines.disabled/`, sem `replace_path`) — o jogo carrega `common/doctrines` 100% vanilla, explicando boa parte da cauda longa de tags (`SOV`, `USA`, `JAP`, `ITA`, `GER`, `ENG`, `FRA`, `FIN`, `SAF`, `NZL`, `INS`, `CAN`, `AST`, `SWE`, `PRC`, `POL`, `NOR`, `CHI`, `BEL`, `SIA`, `RAJ`, `BRM`). Existe uma versão autoral já pronta do Azarya para `infantry_subdoctrines.txt` dentro de `common/doctrines.disabled/`, mas desatualizada frente ao vanilla atual (796 vs 898 linhas — faltam blocos de balanceamento de patches posteriores). **Decisão**: não reativar `common/doctrines.disabled` inteiro nesta rodada (mudança grande demais, desatualizada) — fica documentado como pendência de decisão do usuário para uma rodada futura dedicada.

Removidos ~110 linhas/blocos de resíduo vanilla puro (sem uso autoral, confirmado por 3 agentes de investigação independentes com cruzamento de achados) em 14 arquivos: `common/country_leader/00_traits.txt` (traits `defier_of_the_sun_god`, `PRC_zhang_guotao_in_kmt`, `austrian_exile` + 6 linhas em `imperial_sanction`), `common/technology_sharing/{00,01_dod,09_aat,14_tsr}_tech_sharing_groups.txt` (18 grupos inteiros: TUR, BUL, FIN, DEN, RAJ, CZE, HUN, SWE, ICE, MAN+PRC), `common/peace_conference/ai_peace/00_misc.txt` (GER em `puppet_their_puppets`), `common/scorers/country/operative_mission_scorer.txt` (GER em scorer dummy/exemplo), `common/ai_equipment/generic_naval.txt` (ENG/USA/JAP), `common/special_projects/projects/{land,naval,rocket}_projects.txt` (blocos GER "Dora"/fortificação, ITA "CB Class", JAP×5, GER/USA/SOV em recompensas), `common/technologies/{artillery,infantry}.txt` (PRC/XSM/SIK/GXC/SHX/YUN, mantendo `tag = UPG`), `common/technologies/industry.txt` (bloco `on_research_complete` órfão referenciando FIN/Nokia).

Em todos os casos: preservado tudo que tinha uso autoral genuíno (tags reais do Azarya como UPG/THK/GYE/SLU/LUQ/NSA/SIT nunca tocadas); removido só o vanilla puro sem função no universo Azarya. **Casos documentados, não removidos** (incerteza real ou fora de escopo): `technologies/infantry.txt` linha ~890 `tag = BRA` misturado em bloco autoral (pode ser resíduo vanilla ou erro de digitação de outra tag Azarya iniciada com B — não dá pra saber sem confirmação); `country_leader/00_traits.txt` `tag = SOU` (nem é tag vanilla válida hoje, não gera erro atualmente); `common/dynamic_modifiers/HABSBURG_dynamic_modifiers.txt` (idêntico ao vanilla, mas sem referência literal de tag, nunca usado — resíduo morto fora do escopo desta limpeza específica); pasta duplicada `common/organizations/` (não é um caminho reconhecido pelo motor, nunca carregada, lixo de repo inofensivo); `common/scripted_diplomatic_actions/` e `common/scripted_triggers/diplomacy_scripted_triggers.txt` (referências de tag 100% dentro de comentários, inertes); `common/scripted_effects/SP_scripted_effects.txt:486-490` (stub `original_tag = USA` deliberado e documentado pelo próprio autor como no-op de compatibilidade — gera 1 linha de log mas é intencional).

**Achado extra durante a verificação de chaves**: `common/technologies/infantry.txt` tinha um bug estrutural pré-existente (não relacionado a esta rodada, confirmado via bisseção de profundidade de chaves) — um bloco de tecnologia perdeu sua linha de cabeçalho em algum momento anterior (só sobrou um comentário órfão citando `HUN_light_infantry_divisions_doctrine_effect`, sem nenhuma outra referência no mod), deixando `research_cost`/`allow`/`infantry` soltos com uma chave de fechamento sem abertura correspondente. Isso fechava o `technologies = {` do arquivo prematuramente na linha 1370, desalinhando ~48 tecnologias subsequentes (support_weapons, tech_trucks, motorised_infantry, armored_car*, mechanised_infantry etc.) para fora do bloco esperado — sem gerar erro no log (o parser do HOI4 não acusa), mas potencialmente quebrando o registro dessas tecnologias silenciosamente. Como o bloco órfão não tinha ID (portanto já era inacessível/inútil independente do bug de chaves), removido para restaurar o aninhamento correto. Vale testar a árvore de tecnologia de infantaria em jogo para confirmar que essas techs agora aparecem corretamente.

### Task 2 — `INS_underground_revolution`

`common/doctrines/subdoctrines/land/infantry_subdoctrines.txt` não tinha override ativo (100% vanilla, 898 linhas). O `if/else` de `peoples_war.available` sempre cai no `if` (`NOT = { original_tag = INS }` sempre verdadeiro no universo Azarya), tornando o `else` (com `INS_underground_revolution`) logicamente inatingível — mas o HOI4 valida os dois ramos no load mesmo assim. **Fix**: criado override do mod (vanilla atual + `available = { has_government = communism }`, sem `if/else`) — texto idêntico ao que o próprio autor já usava na versão desativada do arquivo, confirmando que é a correção pretendida. Também removida uma referência residual a `original_tag = PRC` num `ai_will_do.modifier` da mesma subdoctrine (achado ao copiar o vanilla atual, não estava na versão desativada do autor porque ela é mais antiga). `descriptor.mod`/`Azarya.mod` ganharam `replace_path="common/doctrines/subdoctrines/land"` (mínimo necessário).

### Task 3 — Colisões internas de localisation

Analisado `logs/text.log` (1744 linhas "Duplicate localization found"). 872 das colisões são overrides intencionais vanilla-vs-Azarya (não mexidas). Só 2 colisões genuínas — mesma chave duplicada dentro do mesmo arquivo Azarya —, ambas em `localisation/AZ_victory_points_l_english.yml`: `VICTORY_POINTS_759` (`"Fuembellope"` órfã vs `"Vorraketh"` com lastro real em `history/states/465-Kence.txt`) e `VICTORY_POINTS_7806` (`"Noviomagus"` órfã vs `"Steinwacht"` com lastro real em `history/states/363-State_363.txt`). Removidas as 2 entradas órfãs (sem correspondência a nenhuma província real no mod); não foi tentado realocar os nomes para outros IDs sem dono (3185/4677/2494 em GYE) por falta de confirmação.

### Task 4 — `naval_mission_move_command` descartado

5 ocorrências, todas nos primeiros dias de campanha, `tick: 65535` (sentinela de tick inválido, mensagem genérica de engine sem referência a arquivo/linha de mod). Base naval do THK verificada e correta (província 4744, nível 5, estado 382 "Eldoria", owner THK). Sem causa concreta encontrada — documentado como aviso de baixo risco, sem alteração de código.

### Task 5 — Ocultar "Change Background"

Já satisfeito: o container `change_background` em `interface/frontendmainview.gui` já tinha `hide = yes` (adicionado junto da implementação do fundo animado responsivo de 20 faixas, fora desta sessão) — diferente do vanilla atual, que não oculta esse botão. Nenhuma edição necessária.

### Validação final

`tools/validate_mod.py`: 3 ERROR (os 3 DDS conhecidos, inalterados), 76 WARNING (mesma baseline, nenhum novo), 0 divergência de manifesto, 0 desbalanceamento de chaves, 0 building fora de state / província duplicada, 0 foco/evento duplicado. Confirmado manualmente que todos os arquivos tocados têm chaves `{`/`}` balanceadas (contagem exata, incluindo o fix do bug estrutural pré-existente em `infantry.txt`). Nenhum `*.dds/png/tga`, `gfx/flags/`, `gfx/leaders/`, `map/` tocado. `AZ_animated_frontendmainviewbg.gfx` e `AZ_frontend_brand.gfx` confirmados intactos (timestamps anteriores a esta sessão). Sem commit/push.

### Pendências para rodadas futuras

- Decidir se vale a pena atualizar e reativar `common/doctrines.disabled` por completo (reduziria bastante o restante de `countrytag.cpp:135`, mas precisa antes reconciliar com os blocos de balanceamento adicionados pelo vanilla em patches posteriores).
- Confirmar `tag = BRA` em `technologies/infantry.txt` (resíduo vanilla ou erro de digitação de outra tag Azarya com B).
- Testar em jogo a árvore de tecnologia de infantaria (o fix do bug estrutural pode ter "destravado" tecnologias que antes podiam não estar registrando corretamente).
- `common/organizations/` (pasta duplicada não carregada pelo motor) pode ser removida como limpeza de repositório, sem urgência.

---

## Diagnóstico e correção — oceano chapado/branco no fundo do menu (2026-07-14)

*Usuário reportou oceanos renderizando como cor chapada (teal) e uma "bolha branca" no meio do mapa de fundo do menu.*

**Causa confirmada**: `replace_path="map"` no manifesto bloqueava fallback pro vanilla, e `map/terrain/` do mod só tinha 5 dos ~64 arquivos vanilla (faltavam `atlas*`/`atlas_normal*` — detalhe de textura —, `fow_noise_*`/`fow_rgb_waterspec_a` — fog-of-war/nuvem/especular —, `underwater_terrain_*`, bordas, neve, lama etc.). Sem essas camadas o shader cai pra cor lisa da `colormap_water_*` (única camada presente) — exatamente o oceano chapado — e a falta de `fow_noise_*` explica a bolha branca. Segunda causa, independente, confirmada via dica de outro modder no Discord: `common/terrain/00_terrain.txt` (arquivo próprio do Azarya) tinha o bloco `ocean` e outras categorias de água (`water_fjords`, `water_shallow_sea`, `water_deep_ocean`) sem `minimum_seazone_dominance` (e `ocean` também sem `naval_terrain`/`naval_mine_hit_chance`) — chaves presentes no vanilla, relevantes pra dominância naval/zona de mar.

**Fix aplicado**:
1. Copiadas as 59 texturas `.dds`/`.bmp` que faltavam em `map/terrain/` a partir do vanilla instalado (confirmado byte-a-byte idênticas ao original, nenhuma nova arte criada — só restauração de assets genéricos do motor).
2. Adicionadas as chaves faltantes em `common/terrain/00_terrain.txt`: `minimum_seazone_dominance` (250/100/100/250 em `ocean`/`water_fjords`/`water_shallow_sea`/`water_deep_ocean`) e `naval_terrain`/`naval_mine_hit_chance` em `ocean`, todos com os valores do vanilla. Não mexido o `naval_mine_hit_chance = -0.5` que `water_deep_ocean` já tinha (vanilla usa -0.95, mas isso parece ajuste de balanceamento autoral do Azarya, não bug).

Testar visualmente o mapa de fundo do menu pra confirmar que o oceano voltou a ter profundidade/sombreamento normal.

---

## Rodada 5E (2026-07-14) — menu principal e Select Scenario mais autorais

*Menu principal funcionando mas parecendo "vanilla com overlay"; tela de Select Scenario sem override, rodando 100% vanilla, mostrando 2 bookmarks quase idênticos (1924 principal + 1925 rascunho de teste). Objetivo: dar identidade visual própria a essas 2 telas sem tocar em imagem nenhuma.*

### `common/bookmarks/1925.txt` → `1925.txt.disabled`

Bookmark de teste desativado (mesmo padrão `.disabled` do resto do mod, 100% reversível). Tinha nome/descrição idênticos ao 1924 e só 2 países-placeholder — resolvia a "duplicidade de cenários" na raiz, sem precisar de lógica de GUI pra filtrar cards (HOI4 não tem flag nativa de visibilidade por bookmark).

### `interface/frontendmainview.gui` (editado)

- `azarya_version_label`/`azarya_compatible_game_label` aproximadas do logo (de y=220/240 pra y=170/192).
- Nova `azarya_tagline_label` (chave `AZ_MENU_TAGLINE`, nova, em `AZ_version_l_english.yml`): *"A world scarred by disaster, now marching toward war."*
- Removido `version_label` hardcoded "ALPHA" (duplicava/conflitava com a label de versão real).
- Removido `mainmenu_achievement_button` — um segundo botão de achievements órfão, marcado pelo próprio autor com `## This position needs updated` e posicionado em x=-500 (fora dos limites do próprio container pai), duplicando o `achievements_button` que já funciona.
- `exit_button` ajustado de y=300 pra y=298 (ritmo de 40px exato com os outros botões).
- `nudge_button` mantido (a pedido do usuário — botão de debug/teste), só confirmado no ritmo correto.
- `pdx_int_logo` (topo-direita) afastado 15px do `frontend_dev_logo` (x=135→150) pra dar mais respiro.
- Fundo animado e `change_background` (`hide=yes`) não tocados.

### `interface/frontendgamesetupview.gui` (criado, override novo)

Base = cópia integral do vanilla atual (2318 linhas). Único container editado: `gamesetup_scenario_window` (o popup "Select Scenario"). Janela de 579×512 pra 760×580, fundo trocado de `GFX_select_date_bg` (spriteType simples, distorceria ao esticar) pra `GFX_tiled_window2_1b_border` (corneredTileSpriteType do vanilla `core.gfx`, escalável, já usado em outras telas do próprio Azarya). O card do bookmark (`bookmarks_grid`/`bookmark_entry`, 232×211) mantido no tamanho nativo, só reposicionado pra coluna esquerda — como só sobrou 1 bookmark ativo, a grid já mostra 1 card só, sem precisar de filtro manual.

Coluna esquerda: card do cenário + nova seção "Recommended Nations" (texto puro, sem bandeira — não existe mecanismo confirmado de bandeira estática fora do binding dinâmico de grid): `THK — Thiryn Kingdom`, `CZL — Czar of Lesc`, `TOL — Torronese`, `ARD — Aeridor` (tags confirmadas válidas, nomes de `AZ_countries_l_english.yml` + os 2 primeiros conforme o próprio texto do pedido do usuário).

Coluna direita: `bookmark_title`/`bookmark_desc` com `maxWidth`/`maxHeight` bem maiores (reaproveita `NEW_AZARYA_DESC`, que agora cabe inteiro sem cortar) + nova seção "resumo do cenário" (`AZ_SCENARIO_SUMMARY_TITLE` + 5 tags: Fractured Alliances, Militarizing Nations, Regional Conflicts, 57 Countries, 506 States — contagens conferidas diretamente em `history/countries/`=57 e `history/states/`=506, batem com o pedido). `back_button`/`select_button` mantidos com os mesmos nomes internos, sons e atalhos (`ESCAPE`/`RETURN`), só reposicionados.

Novas chaves de loc em `localisation/AZ_bookmarks_l_english.yml`: `AZ_SCENARIO_SUMMARY_TITLE`, `AZ_SCENARIO_TAG_1..5`, `AZ_RECOMMENDED_NATIONS_TITLE`, `AZ_RECOMMENDED_NATION_1..4`.

`gamesetup_interesting_countries_window` (seletor de país) não foi tocado — já tinha branding correto confirmado na Rodada 5C.

### Validação

`tools/validate_mod.py`: 3 ERROR (mesmos DDS conhecidos), 76 WARNING (baseline inalterada), 0 divergência de manifesto, 0 desbalanceamento de chaves. Chaves balanceadas conferidas manualmente nos 2 `.gui` (287/287 no `frontendmainview.gui`, 681/681 no `frontendgamesetupview.gui` novo). Nenhum `*.dds/png/tga` criado ou editado nesta rodada, `map/` não tocado. `AZ_animated_frontendmainviewbg.gfx`, `AZ_frontend_brand.gfx`, `AZ_Bookmark.gfx` confirmados intactos (timestamps anteriores à sessão). Sem commit/push.

### Correção pós-teste: `version_label` e fonte inválida (mesmo dia)

Testando em jogo, o `error.log` mostrou 2912 ocorrências (92% do log) de `[containerwindow.cpp:787] Could not find "version_label" in window mainmenu_panel_bottom` — o motor consulta esse elemento pelo nome continuamente (provavelmente alguma rotina de subscription/versão), mesmo que ele não precisasse ser exibido. Remover o elemento inteiro (em vez de só ocultá-lo) foi o erro. **Fix**: `version_label` restaurado em `frontendmainview.gui`, agora com `hide = yes` — existe pro motor encontrar, mas não mostra mais o texto "ALPHA" que conflitava com a label de versão real.

Também apareceu `[graphics.cpp:1280] No font with name hoi_14b` — a fonte usada na nova `azarya_tagline_label` não existe no HOI4 (fontes válidas seguem o padrão `hoi_16`/`hoi_18`/`hoi_16mbs`/`hoi_18mbs` etc., confirmado em `core.gfx` do vanilla). **Fix**: trocada para `hoi_16mbs` (mesma família das outras labels do canto superior esquerdo).

Conferido também: as novas chaves de localisation desta rodada (`AZ_MENU_TAGLINE`, `AZ_SCENARIO_*`, `AZ_RECOMMENDED_NATION*`) não aparecem em nenhuma linha de `text.log` — zero colisão introduzida por elas. A única remoção órfã que não gerou o mesmo tipo de erro foi o `mainmenu_achievement_button` (confirmado — nenhum "Could not find" relacionado a ele no log).

---

## Fechamento de `countrytag.cpp:135` — `common/script_constants` e resto de `common/doctrines` (2026-07-14)

*Pedido do usuário: corrigir tudo no `error.log` que ele não pediu explicitamente pra ignorar. Log inicial testado veio contaminado por outro mod instalado (`Code Geass: Black Requiem`, `ugc_3759973824.mod`) — 91,8% dos erros eram desse mod (arquivos `imperial_*`/`empire_ideas.txt`/etc. que nem existem na pasta do Azarya). Usuário desativou o Code Geass e reenviou log limpo.*

### Log limpo: só 2 categorias acionáveis

`missing_country_tag` (137 ocorrências, 112 tags únicos, 54,8% do log) e o resto já coberto pela lista de itens ignorados (portraits/flags ausentes). Nenhuma outra categoria de erro real sobrou.

### Causa raiz principal: `common/script_constants/country_groups.txt`

Pasta **não é `replace_path`'d** — carregava 100% vanilla. Esse arquivo define grupos nomeados de tags (`nordics`, `continental_europe_1936`, `literally_china`, `chinese_warlords`, `islamic_world`) usados por `country_groups.X` em triggers/efeitos — mas nenhum arquivo do Azarya referencia `country_groups.*` em lugar nenhum (confirmado por grep). Sozinho, esse arquivo explicava **110 das 112 tags únicas** do log (praticamente todo o Oriente Médio, Ásia Central, Bálcãs, senhores da guerra chineses, países nórdicos e a Europa continental de 1936 vanilla). **Fix**: criado override do mod com o mesmo schema e nomes de grupo, mas arrays vazios (sem inventar conteúdo, já que nada usa esses grupos).

### Causa secundária: resto de `common/doctrines` não coberto na Rodada 5D

As 2 tags restantes (`JAP`, `SOV`) vinham dos 8 arquivos de subdoctrine aéreas/navais que a Rodada 5D não tinha coberto (só `subdoctrines/land` tinha sido tratado): `subdoctrines/air/{air_fighter,air_heavy,air_medium,air_strike}_aircraft_subdoctrines.txt` e `subdoctrines/sea/navy_{capital,carrier,screen,submarine}_subdoctrines.txt`. Removidas ~25 referências a ENG/USA/JAP/ITA/SOV/FRA/GER/AST/CAN/NZL/SAF (todas vanilla puro, sem uso autoral, mesmo padrão de "modifier de peso de IA isolado" das rodadas anteriores) em todos os 8 arquivos, preservando o resto de cada subdoctrine. `grand_doctrines`, `tracks` e `folders` de doctrines foram checados e não têm nenhuma referência de tag — não precisaram de override.

**Achado extra**: `common/doctrines/subdoctrines/sea/navy_submarine_doctrines.txt` **vanilla** tem um bug estrutural próprio da Paradox — o último subdoctrine (`long_range_submarines`) nunca fecha (falta 1 `}` no final do arquivo original, 110 abre vs 109 fecha). Corrigido ao criar o override (chave de fechamento adicionada no final).

`descriptor.mod`/`Azarya.mod` ganharam `replace_path="common/doctrines/subdoctrines/air"` e `="common/doctrines/subdoctrines/sea"`.

### Validação

`tools/validate_mod.py`: 3 ERROR (DDS conhecidos), 76 WARNING (baseline inalterada), 0 divergência de manifesto, 0 desbalanceamento de chaves. Conferido manualmente: as 112 tags únicas do log batem exatamente com 110 (country_groups.txt) + 2 (JAP/SOV nos 8 arquivos de doctrine) — cobertura total confirmada por diff de conjuntos, não achismo.

### Pendência restante

`common/doctrines.disabled` (grand_doctrines, tracks, folders — versão autoral completa) continua sem decisão de reativação (mesma pendência da Rodada 5D). `common/script_constants/state_groups.txt` (vanilla, não sobrescrito) referencia IDs de estado que provavelmente não existem no mapa do Azarya, mas não gerou nenhum erro no log atual — não mexido, documentado como possível ponto de atenção futuro se aparecer algum erro relacionado a estados.

---

## Fechamento de `countrytag.cpp:135` (parte 2) e regressões críticas do frontend (2026-07-15)

*Log novo enviado pelo usuário: só 3 tags restantes (JAP, SOV, CZE), mas também revelou 2 problemas graves ("Undefined GUI_TYPE... This will most likely crash the game") introduzidos por edições feitas fora desta conversa em `frontendmainview.gui` e `frontendgamesetupview.gui` — ambos os arquivos foram reescritos externamente (mesmo timestamp nos dois), com estrutura bem diferente da Rodada 5E. Tratado como nova base real, sem tentar reverter — só corrigidos os bugs estruturais pontuais.*

### `interface/frontendmainview.gui` — `change_background` removido por completo

O container `change_background` (e seus filhos `background_selection`/`background_selection_list`/`available_backgrounds`/`select_all_checkbox`/`change_background_button`) tinha sumido inteiramente do arquivo entre `owned_dlc_item` e `unowned_dlc_item`. Mesmo padrão do bug do `version_label` (Rodada 5E): o motor procura esse elemento por nome internamente mesmo quando oculto — sem ele, "Undefined GUI_TYPE: change_background - This will most likely crash the game" e uma cascata de "Could not find X in window" pros filhos. **Fix**: bloco restaurado (texto verificado, lido diretamente do arquivo numa investigação anterior desta mesma sessão), com `hide = yes` mantido. Nenhuma outra parte do arquivo foi tocada — o resto claramente tem edições novas e deliberadas de fora desta conversa (ex.: posição do `frontend_game_logo` mudou pra x=750 y=25) que não me cabe reverter.

### `interface/frontendgamesetupview.gui` — `filters` removido, comentário explicava o motivo errado

O elemento `filters` (`OverlappingElementsBoxType`) tinha sido removido de `gamesetup_interesting_countries_window`, com um comentário explicando que dependia de um template `country_filter` "que a gente não tem" (referência a outro mod, "Youjo Senki", usado como base externa de comparação). Na verdade `country_filter` é um template que o próprio motor cria dinamicamente ao redor do `filters` — nem o vanilla define esse template em nenhum arquivo. **Fix**: `filters` restaurado com os valores exatos do vanilla atual (posição/tamanho/spacing), resolvendo tanto o "Could not find 'filters'" quanto o "Undefined GUI_TYPE: country_filter" repetido.

### `countrytag.cpp:135` — os 3 últimos: JAP, SOV, CZE

Repeti a metodologia da rodada anterior (buscar um arquivo só que contenha as 3 tags juntas, cruzando com as pastas ainda não cobertas por `replace_path`). Dois arquivos, ambos 100% vanilla puro sem uso autoral:

- **`common/profile_pictures/00_profile_picture.txt`** (pasta nunca tocada) — sistema de fotos de perfil de carreira multiplayer, quase todas as 59 entradas numeradas (exceto 4 genéricas) travadas atrás de `tag = <país vanilla>` ligado a focus histórico específico (CZE, JAP, SOV, GER, ENG, USA, FRA, ITA, POL, GRE, BUL, CHI, YUG, POR, MEX, HOL, LIT, RAJ, SPR, SWI, ETH etc.) — nenhuma dessas tags existe no Azarya, então nenhuma dessas entradas pode disparar de verdade. **Fix**: override novo mantendo só as 4 entradas genéricas (sem `tag =`), removendo as ~55 travadas atrás de país vanilla.
- **`common/doctrines/subdoctrines/special_forces/special_forces_subdoctrines.txt`** — 9º arquivo de doctrine que tinha ficado de fora das Rodadas 5D/5D-parte-2 (só descoberto agora porque nenhuma das suas ~28 referências de tag tinha aparecido nos logs testados até então). Removidos 7 blocos `modifier = { OR = { original_tag = ... } }` (SWE/FIN/NOR, GER/SOV/POL/ITA/BEL, ENG/CAN/AST/NZL/SAF, JAP/USA, SOV/JAP/ITA, GER/ENG/POL/USA, FIN/SWE/NOR/BEL, SIA/RAJ/BRM), preservando o resto de cada subdoctrine. `descriptor.mod`/`Azarya.mod` ganharam `replace_path="common/doctrines/subdoctrines/special_forces"`.

### `AZ_lore_icon_TEMP.dds`/`AZ_lore_mapicon_TEMP.dds` — placeholder temporário carregado a pedido do usuário

Confirmado como Equestria at War (Steam Workshop, appid 394360, item 1826643372) — `gfx/interface/state_lore_button.dds` (47×50) e `gfx/interface/state_lore_mapicon.dds` (47×76), dimensões batendo exatamente com o que o comentário do próprio `AZ_lore_atlas.gfx` já documentava. Copiados para `gfx/interface/AZ_lore_icon_TEMP.dds`/`AZ_lore_mapicon_TEMP.dds` a pedido explícito do usuário, como placeholder temporário — headers DDS válidos confirmados via `validate_mod.py` (338 arquivos verificados, só os 3 ERROR de sempre). Ainda precisam ser trocados por arte própria do Azarya antes de qualquer release pública (mesmo aviso já presente no comentário do `.gfx`).

### Validação

`tools/validate_mod.py`: 3 ERROR (DDS conhecidos), 76 WARNING (baseline inalterada), 0 divergência de manifesto, 0 desbalanceamento de chaves. Chaves balanceadas conferidas manualmente em `frontendmainview.gui` (259/259), `frontendgamesetupview.gui` (642/642) e `special_forces_subdoctrines.txt` (195/195). Sem commit/push.
