# Kingdom of Thiryn (`THK`)

*Ver `00_CANON_RULES.md` e `03_thiryn_gengen_conflict.md`.*

## Status

- monarquia e Rainha Elara: **IMPLEMENTADO/CANON**;
- caminho `THK_MenOfPride`: **CANON**; identidade confirmada tecnicamente como facção de oficiais/nobres ("Adric's path"), ligada ao lado "Royal Army" do sistema de Balance of Power;
- caminho `THK_RoyalAlternative`: **IMPLEMENTADO**; confirmado tecnicamente como consolidação da Coroa/Casa de Aurum (decisão de BOP `THK_high_decrease_effect`, visível apenas após este foco, recruta divisões leais à Coroa);
- caminho `THK_ThirdOption`: **IMPLEMENTADO**; identidade confirmada como movimento popular/operário de esquerda (ganho de popularidade `communism`, ícone de inspiração revolucionária), distinto dos outros dois;
- derrota para Gengen: **CANON**;
- crise de fronteira com Gengen (revanchismo, refugiados, doutrina gydiana): **IMPLEMENTADO NESTA RODADA** — ver ramo "The Lost Border" em `common/national_focus/Thiryn.txt` (8 focos novos: `THK_RevanchistSentiment`, `THK_RefugeesFromTheWest`, `THK_VeteransCommittees`, `THK_MapsOfTheLostProvinces`, `THK_AcceptGydianPatronage`/`THK_RejectGydianPatronage`, `THK_PrepareTheClaim`, `THK_TowardGreatThiryn`). Variáveis reais `az_thk_upg_border_tension` e `az_gye_influence_thk` inicializadas por foco. Não inclui nenhum sistema do lado de UPG/GYE — apenas hooks seguros do lado de THK, conforme instruído;
- decisão `THK_ClaimLostProvinces` (namespace de decisão `THK_frontier_decisions_category`): **IMPLEMENTADO E CORRIGIDO NESTA RODADA**; usa `retake_core_state` sobre cada um dos três estados (86, 400, 409) que UPG ainda possua, já que são core de THK — preferido sobre `start_justifying_wargoal_against`/`create_wargoal_type` (tentativas anteriores, a segunda rejeitada pelo engine com `Unknown effect-type`). A decisão valida em `available`: `exists = UPG`, ausência de guerra e de wargoal já ativos contra UPG, e que UPG ainda possua ao menos um dos três estados; não fica mais permanentemente bloqueada por flag de uso único — usa `days_re_enable = 90` como cooldown, permitindo nova tentativa se a justificação anterior for cancelada ou expirar. **Ressalva de auditoria:** `retake_core_state` é minha melhor estimativa informada da sintaxe correta (não há exemplo funcional equivalente em nenhum outro arquivo deste repositório para confirmar por precedente, e não há acesso ao engine neste ambiente) — precisa de confirmação em teste real antes de ser tratado como definitivo;
- Great Thiryn: **IMPLEMENTADO E CORRIGIDO NESTA RODADA** (ver seção dedicada abaixo);
- Eldoria como epicentro geológico: **NÃO CONFIRMADO** (sem alteração nesta rodada).

## Dados técnicos

No snapshot:

- capital Eldoria (382);
- 7 estados;
- 6.904.586 de manpower;
- 75 focos;
- casa de Aurum;
- Rainha Elara Lorenthia.

## Grande Terremoto

Eldoria foi severamente atingida e contém o Shattered Quarter.

Não afirmar que foi o epicentro geológico sem validar a localisation original.

## Guerra contra Gengen

Thiryn perdeu:

- Doia (86);
- Haifa (400);
- Mominches (409).

População técnica combinada:

- 1.657.762;
- lore: aproximadamente 1,7 milhão.

## Consequências

- revanchismo;
- protestos;
- crise militar;
- perda de legitimidade;
- refugiados;
- pressão financeira;
- reconstrução.

## Gydian

Gydian pode oferecer a devolução dos territórios em troca de:

- adesão;
- acesso;
- submissão econômica;
- apoio na Grande Guerra.

## Caminhos

- aliança com Gydian;
- resistência com Gengen;
- neutralidade;
- nova guerra;
- política independente.

## Great Thiryn

Os estados coincidem com os territórios perdidos (86 Doia, 400 Haifa, 409 Mominches).

Estado técnico confirmado e corrigido nesta rodada:

- **fonte única do efeito**: a decisão `form_Great_Thiryn` em `common/decisions/formable_nation_decisions.txt` continua sendo a única responsável por aplicar `set_cosmetic_tag = THK_UNIF`; nenhum foco duplica esse efeito;
- **requisitos ampliados**: a decisão agora exige `owns_state` **e** `controls_state` para os três estados (não mais apenas `controls_state`, o que antes permitiria formar Great Thiryn durante uma simples ocupação militar sem paz assinada) e `is_subject = no`, além de `has_completed_focus = THK_TowardGreatThiryn` (foco final do ramo "The Lost Border") e `has_stability > 0.4`, tornando a formação um objetivo tardio de campanha, não algo obtido no primeiro dia, conforme exigido pelo canon;
- **flags renomeadas**: `form_test_flag`/`form_test_tt`/`created_country` (nomes de teste/placeholder) foram substituídos por `az_thk_great_thiryn_formed` (flag global), `az_thk_great_thiryn_completed` (flag de país) e `THK_form_great_thiryn_tt` (tooltip), seguindo a convenção `az_<tag>_<descrição>`;
- **localisation do cosmetic tag**: `THK_UNIF`, `THK_UNIF_DEF` e `THK_UNIF_ADJ` foram criadas (ausentes antes desta rodada) em `localisation/AZ_formables_l_english.yml`; a arte de bandeira própria para `THK_UNIF` continua **TBD**, pois a criação de novo `.dds` está fora do escopo desta rodada;
- **notícia**: `azarya_formables.1` (namespace próprio `azarya_formables`) continua sendo o evento correto e único, disparado depois do efeito (`hidden_effect`), conforme regra 3 do canon;
- **`news.59` — CONFIRMADO MORTO E REMOVIDO**: existia em `events/NewsEvents.txt` como um evento de notícia completo, com o comentário `# Formation of Great Thiryn` e três opções condicionadas a `original_tag = THK`, mas não era chamado por nenhum foco, decisão ou evento ativo. Era uma implementação anterior abandonada de Great Thiryn, coexistindo indevidamente com `azarya_formables.1` e reutilizando o namespace vanilla `news`, proibido pela regra 10 do canon. Removido nesta rodada;
- a formação continua representando apenas a recuperação dos três estados perdidos, sem ambição territorial maior — nenhum estado novo foi adicionado à formação.

## Lesc

Relação deliberadamente em aberto.

## TBD

- sucessão;
- família real;
- líderes militares;
- nome da guerra;
- tratado;
- origem da república de Gengen.
