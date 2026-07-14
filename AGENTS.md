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
