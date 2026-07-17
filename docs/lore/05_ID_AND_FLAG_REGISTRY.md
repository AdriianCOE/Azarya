# Azarya — Registro de IDs e Convenções Técnicas

**Status: PROPOSTA TÉCNICA. Nada neste arquivo está automaticamente implementado.**

## Decisão de padronização

O repositório mistura `AZ_` e `az_`. Para conteúdo novo:

- **nomes de arquivo:** `AZ_` em maiúsculo;
- **identificadores de script:** `az_` em minúsculo;
- **tags de países dentro de efeitos e triggers:** forma oficial em maiúsculo (`GYE`, `THK`, `UPG`);
- **localisation:** seguir exatamente o ID que será exibido, sem duplicar chaves equivalentes.

Não criar um terceiro padrão.

## Arquivos propostos

```text
common/scripted_effects/AZ_geopolitics_effects.txt
common/scripted_triggers/AZ_geopolitics_triggers.txt
common/on_actions/AZ_geopolitics_on_actions.txt
common/decisions/AZ_geopolitics_decisions.txt
events/AZ_geopolitics_events.txt
events/AZ_news_events.txt
localisation/english/AZ_geopolitics_l_english.yml
localisation/english/AZ_news_l_english.yml
```

Os caminhos de localisation devem ser adaptados ao padrão real do repositório antes da criação.

## Namespaces

| Sistema | Namespace |
|---|---|
| Expansão gydiana | `az_gye` |
| Guerra Zauern–Torronese | `az_koz_tol` |
| Nirisia/Celest | `az_nir` |
| Durnstad | `az_duh` |
| Guerra das Três Bandeiras | `az_three_banners` |
| Thiryn–Gengen | `az_thk_upg` |
| Sithius | `az_sit` |
| Grande Guerra Continental | `az_great_war` |
| Continente oriental | `az_east` |
| Notícias mundiais | `az_news` |

### Regra

Não reutilizar o namespace genérico vanilla `news`. Isso reduz colisões e impede repetição do problema de `news.59`.

## Organização numérica dentro de cada namespace

Faixas não são tecnicamente obrigatórias, mas ajudam a leitura:

| Faixa | Uso |
|---:|---|
| 1–49 | inicialização e eventos ocultos |
| 50–99 | preparação e escalada |
| 100–199 | escolhas nacionais |
| 200–299 | crises diplomáticas |
| 300–399 | guerras e capitulações |
| 400–499 | pós-guerra e integração |
| 900–999 | debug e migração temporária |

Nenhuma faixa deve ser reservada sem verificar os IDs já existentes no momento da implementação.

## IDs já implementados (não apenas propostos)

Diferente do restante deste arquivo, os itens abaixo já existem em código real, criados durante a auditoria e expansão da árvore de foco de Thiryn:

| ID | Tipo | Onde | Efeito |
|---|---|---|---|
| `az_thk_upg_border_tension` | variável de país, clampada 0–100 via `clamp_variable` (não mais inline em `add_to_variable`) | `common/national_focus/Thiryn.txt`, `common/decisions/THK.txt` | acumula tensão fronteiriça com UPG; sem leitor automático ainda |
| `az_gye_influence_thk` | variável de país, clampada 0–100 via `clamp_variable` | `common/national_focus/Thiryn.txt` (`THK_AcceptGydianPatronage` +25, `THK_RejectGydianPatronage` -10) | reflete a influência gydiana sobre Thiryn |
| `az_thk_gye_patronage_accepted` | flag de país | `common/national_focus/Thiryn.txt` (`THK_AcceptGydianPatronage`) | registra que Thiryn aceitou o patrocínio gydiano |
| `az_thk_gye_patronage_rejected` | flag de país | `common/national_focus/Thiryn.txt` (`THK_RejectGydianPatronage`) | registra que Thiryn recusou o patrocínio gydiano e reduz `az_gye_influence_thk` |
| `az_thk_great_thiryn_formed` | flag global | `common/decisions/formable_nation_decisions.txt` | substitui o antigo `form_test_flag`; impede nova formação |
| `az_thk_great_thiryn_completed` | flag de país | `common/decisions/formable_nation_decisions.txt` | substitui o antigo `created_country` |

Namespaces de evento realmente em uso: `THK_azarya` (eventos nacionais, `THK_azarya.1` e `THK_azarya.2`), `azarya_formables` (notícia de formação, `azarya_formables.1`). Nenhum desses reutiliza o namespace vanilla `news`; `news.59` foi removido por ser código morto.

## Flags globais

| Flag proposta | Finalidade |
|---|---|
| `az_three_banners_started` | guerra já iniciada |
| `az_three_banners_ended` | guerra encerrada |
| `az_helvaria_reunified` | existe um vencedor reunificador |
| `az_great_war_started` | Grande Guerra Continental iniciada |
| `az_durnstad_truth_exposed` | crimes de Durnstad revelados internacionalmente |

## Flags nacionais

Formato:

```text
az_<tag_minúscula>_<descrição>
```

Exemplos:

```text
az_gye_fvi_offer_sent
az_gye_fvi_integration_completed
az_gye_atv_puppet_stage
az_koz_karleston_promised
az_koz_karleston_ceded
az_nir_celest_offer_received
az_duh_break_with_gydian
az_duh_occupation_active
az_thk_revanchism_active
az_upg_gydian_alignment
az_sit_debt_crisis_active
```

## Variáveis

Formato:

```text
az_<sistema>_<objeto>
```

Exemplos:

```text
az_gye_influence_fvi
az_gye_influence_atv
az_gye_influence_upg
az_thk_upg_border_tension
az_three_banners_support_dtb
az_three_banners_support_vrd
az_three_banners_support_hel
az_sit_debt_level
az_lia_central_authority
az_orv_intervention_support
```

### Regra de intervalo

Quando possível, documentar:

- mínimo;
- máximo;
- valor inicial;
- efeitos de cada faixa;
- comportamento ao anexar ou trocar de tag.

Não depender de valores ilimitados sem clamp.

## Decisões e categorias

| Elemento | Padrão |
|---|---|
| Categoria | `az_<tag>_<sistema>_category` |
| Decisão | `az_<tag>_<ação>` |
| Missão | `az_<tag>_<objetivo>_mission` |

Exemplos:

```text
az_gye_expansion_category
az_gye_pressure_fervonia
az_nir_negotiate_celest
az_thk_support_border_committees
az_upg_request_gydian_guarantee
az_nsa_arm_varadnia
```

## Scripted effects

Formato:

```text
az_<sistema>_<ação>_effect
```

Exemplos:

```text
az_geopolitics_safe_state_transfer_effect
az_three_banners_start_war_effect
az_helvaria_reunification_effect
az_gye_complete_integration_effect
```

Todo efeito permanente deve:

1. validar que o alvo existe;
2. validar owner/controlador quando relevante;
3. impedir execução duplicada;
4. definir flag de conclusão;
5. disparar notícia somente depois do efeito;
6. possuir fallback documentado.

## Scripted triggers

Formato:

```text
az_<sistema>_<condição>_trigger
```

Exemplos:

```text
az_three_banners_can_start_trigger
az_gye_can_integrate_fvi_trigger
az_duh_can_break_protection_trigger
az_great_war_can_start_trigger
```

## Eventos e localisation

Evento:

```text
az_three_banners.100
```

Localisation:

```text
az_three_banners.100.t
az_three_banners.100.d
az_three_banners.100.a
az_three_banners.100.b
```

News event:

```text
az_news.10
az_news.10.t
az_news.10.d
az_news.10.a
```

Não criar duas chaves para a mesma opção, como `THK_azarya.1.a` e `thiryn.1.a`.

## Estado das regiões importantes

| Nome | Estado |
|---|---:|
| Doia | 86 |
| Karleston | 361 |
| Haifa | 400 |
| Mominches | 409 |
| Celest | 462 |

O ID deve ser validado novamente antes de cada implementação, pois o mapa está sendo alterado em paralelo.

## Idempotência

Cada cadeia deve ter:

- flag `started`;
- flag `completed` ou resultado exclusivo;
- trigger que bloqueia nova execução;
- fallback caso uma tag tenha sido anexada;
- teste após save/load.

Exemplo conceitual:

```text
az_three_banners_started
az_three_banners_winner_dtb
az_three_banners_winner_vrd
az_three_banners_winner_hel
az_three_banners_ended
```

Somente uma flag de vencedor pode existir.

## IA

Pesos históricos devem ser centralizados em `ai_chance`/`ai_will_do`, condicionados por game rule histórica quando existir.

Não usar evento oculto para forçar escolha histórica ignorando o jogador.

## Regra final

Antes de criar qualquer identificador:

1. pesquisar o namespace no repositório;
2. validar tags e IDs de estado;
3. registrar o novo ID neste arquivo;
4. implementar um sistema por vez;
5. executar validação estática;
6. testar no cenário;
7. testar save/load;
8. revisar `error.log`, `game.log` e `setup.log`.
