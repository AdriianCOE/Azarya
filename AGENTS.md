# Azaryafantasia — Contexto e Lore do Mod

> Documento de referência permanente sobre o mundo, a linha do tempo e as intenções por trás do mod. Manter atualizado conforme a lore for sendo definida.

## O que é o mod

Total conversion para Hearts of Iron IV. Ambientação **realista** (não é fantasia), mas se passa em uma **linha do tempo alternativa** à nossa.

- Existe também uma pasta `Azarya` (mais simples, gerada por um gerador automático de mundos fantasiosos). Ela é só rascunho/referência — o projeto principal é o **Azaryafantasia**.
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
