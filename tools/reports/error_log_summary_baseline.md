# Resumo do error.log

```
Log: C:\Users\drioj\Documents\Paradox Interactive\Hearts of Iron IV\logs\errornovo.log
Linhas brutas: 4437
Entradas logicas (apos mesclar continuacao multilinha): 3821
Assinaturas detalhadas unicas: 630
Primeiro timestamp: no_game_date 03:20:18
Ultimo timestamp: 1924.01.01.12 03:21:37

=== Top 50 assinaturas detalhadas ===
1596	[triggerimplementation.cpp:3153]	common/ai_strategy/doctrines.txt:N: has_tech: Invalid tech
152	[triggerimplementation.cpp:3047]	common/units/equipment/tank_chassis.txt:N: has_idea: BUL_army_restrictions_aat is not A valid Idea
115	[triggerimplementation.cpp:3047]	common/units/equipment/plane_airframes.txt:N: has_idea: BUL_army_restrictions_aat is not A valid Idea
113	[technologytemplate.cpp:874]	Technology has an invalid specialization "specialization_naval"
113	[technologytemplate.cpp:874]	Technology has an invalid specialization "specialization_land"
109	[technologytemplate.cpp:874]	Technology has an invalid specialization "specialization_air"
103	[triggerimplementation.cpp:3047]	common/units/equipment/ship_hull_submarine.txt:N: has_idea: BUL_army_restrictions_aat is not A valid Idea
78	[triggerimplementation.cpp:3047]	common/units/equipment/ship_hull_light.txt:N: has_idea: BUL_army_restrictions_aat is not A valid Idea
75	[triggerimplementation.cpp:3047]	common/units/equipment/ship_hull_heavy.txt:N: has_idea: BUL_army_restrictions_aat is not A valid Idea
70	[triggerimplementation.cpp:3047]	common/units/equipment/ship_hull_cruiser.txt:N: has_idea: BUL_army_restrictions_aat is not A valid Idea
37	[countrytag.cpp:135]	ENG - is not in the tag list
35	[countrytag.cpp:135]	GER - is not in the tag list
34	[countrytag.cpp:135]	USA - is not in the tag list
30	[countrytag.cpp:135]	ITA - is not in the tag list
28	[countrytag.cpp:135]	FRA - is not in the tag list
28	[countrytag.cpp:135]	JAP - is not in the tag list
20	[effectimplementation.cpp:5544]	history/countries/DKM - Duskmoor.txt:N: recruit_character: Unknown character
19	[persistent.cpp:67]	Error: "Breakthrough cost of specialization: specialization_naval is not a valid specialization: specialization_naval, near line: N" in file: "common/special_projects/projects/nava
18	[countrytag.cpp:135]	SOV - is not in the tag list
17	[countrytag.cpp:135]	HUN - is not in the tag list
15	[character_manager.cpp:283]	Large portrait path gfx/leaders/leader_unknown.dds has unexpected format, can't compute small portrait path
13	[technologytemplate.cpp:874]	Technology has an invalid specialization "specialization_nuclear"
10	[trigger.cpp:700]	Invalid trigger 'coal' in common/technologies/industry.txt line: N
10	[trigger.cpp:568]	Error: "Unknown trigger-type: coal, near line: N" in file: "common/technologies/industry.txt" near line: N
9	[persistent.cpp:67]	Error: "Breakthrough cost of specialization: specialization_land is not a valid specialization: specialization_land, near line: N" in file: "common/special_projects/projects/land_p
9	[persistent.cpp:67]	Error: "Unable to find item with id: sp_naval_generic_reward_scientist_xp_1: , near line: N | Unable to find item with id: sp_naval_generic_reward_scientist_xp_2: , near line: N | 
9	[trigger.cpp:700]	Invalid trigger 'PRC' in common/dynamic_modifiers/SEA_dynamic_modifiers.txt line: N
9	[trigger.cpp:568]	Error: "Unknown trigger-type: PRC, near line: N" in file: "common/dynamic_modifiers/SEA_dynamic_modifiers.txt" near line: N
9	[graphics.cpp:1351]	Failed to create gui object. Could not find sprite type [GFX_country_filter_entry]
8	[persistent.cpp:67]	Error: "Unexpected token: category_regimental_support_artillery, near line: N" in file: "common/doctrines/subdoctrines/land/infantry_subdoctrines.txt" near line: N
8	[graphics.cpp:1351]	Failed to create gui object. Could not find sprite type [GFX_unplayed_content_notification]
7	[effect.cpp:445]	Invalid effect 'bathe_in_hellfire_nuclear' in common/raids/nuclear_raids.txt line: N
7	[effect.cpp:358]	Error: "Unknown effect-type: bathe_in_hellfire_nuclear, near line: N" in file: "common/raids/nuclear_raids.txt" near line: N
7	[faction_template.cpp:34]	Faction goal not found in the database: faction_manifest_balkan_control
7	[trigger.cpp:700]	Invalid trigger 'NOR' in common/dynamic_modifiers/aat_dynamic_modifiers.txt line: N
7	[trigger.cpp:568]	Error: "Unknown trigger-type: NOR, near line: N" in file: "common/dynamic_modifiers/aat_dynamic_modifiers.txt" near line: N
7	[trigger.cpp:700]	Invalid trigger 'NOR_AAT' in common/dynamic_modifiers/aat_dynamic_modifiers.txt line: N
7	[trigger.cpp:568]	Error: "Unknown trigger-type: NOR_AAT, near line: N" in file: "common/dynamic_modifiers/aat_dynamic_modifiers.txt" near line: N
7	[database_scoped_variables.cpp:267]	invalid database object for effect/trigger: mobile_warfare. use var:var_name to explicitly use variables in effects/triggers
7	[database_scoped_variables.cpp:267]	invalid database object for effect/trigger: superior_firepower. use var:var_name to explicitly use variables in effects/triggers
7	[database_scoped_variables.cpp:267]	invalid database object for effect/trigger: trench_warfare. use var:var_name to explicitly use variables in effects/triggers
7	[database_scoped_variables.cpp:267]	invalid database object for effect/trigger: mass_assault. use var:var_name to explicitly use variables in effects/triggers
7	[effectimplementation.cpp:19542]	common/raids/nuclear_raids.txt:N: add_dynamic_modifier Invalid dynamic modifier fallout_atomic
6	[persistent.cpp:67]	Error: "Unable to find item with id: sp_rockets_scientist_xp_generic_reward: , near line: N | Unable to find item with id: sp_rockets_political_interference_generic_reward: , near 
6	[effect.cpp:445]	Invalid effect 'bathe_in_hellfire_thermonuclear' in common/raids/nuclear_raids.txt line: N
6	[scopedvariable.cpp:588]	sp:sp_air_axial_jet_engine does not match any Special Project in database
6	[persistent.cpp:67]	Error: "Unable to find item with id: faction_goal_industrial_expansion: , near line: N | Unable to find item with id: faction_goal_defeat_of_fascism: , near line: N" in file: "comm
6	[persistent.cpp:67]	Error: "invalid modifier: sp_air_intercontinental_bomber_speed_factor, near line: N" in file: "common/dynamic_modifiers/bba_dynamic_modifiers.txt" near line: N
6	[persistent.cpp:67]	Error: "invalid modifier: sp_air_mothership_aircraft_speed_factor, near line: N" in file: "common/dynamic_modifiers/bba_dynamic_modifiers.txt" near line: N
6	[effectimplementation.cpp:19542]	common/raids/nuclear_raids.txt:N: add_dynamic_modifier Invalid dynamic modifier fallout_thermonuclear

=== Top 20 arquivos de origem ===
1596	common/ai_strategy/doctrines.txt
358	countrytag.cpp:135
348	technologytemplate.cpp:874
152	common/units/equipment/tank_chassis.txt
115	common/units/equipment/plane_airframes.txt
104	database_scoped_variables.cpp:267
103	common/units/equipment/ship_hull_submarine.txt
78	common/units/equipment/ship_hull_light.txt
75	common/units/equipment/ship_hull_heavy.txt
70	common/units/equipment/ship_hull_cruiser.txt
69	faction_template.cpp:34
59	common/special_projects/projects/naval_projects.txt
53	common/raids/nuclear_raids.txt
40	common/dynamic_modifiers/aat_dynamic_modifiers.txt
35	common/special_projects/projects/land_projects.txt
30	common/factions/templates/unique_minor_factions.txt
30	common/dynamic_modifiers/SEA_dynamic_modifiers.txt
25	common/technologies/industry.txt
25	common/country_leader/00_traits.txt
21	scopedvariable.cpp:588

=== Familias amplas ===
1629	42.6%	invalid_technology_reference
593	15.5%	invalid_idea_reference
438	11.5%	invalid_specialization
358	9.4%	missing_country_tag
330	8.6%	outros
141	3.7%	invalid_faction_goal
91	2.4%	invalid_raid_reference
80	2.1%	missing_special_project_reward
66	1.7%	invalid_trigger_doctrine
23	0.6%	missing_texture_asset
18	0.5%	duplicate_entity
18	0.5%	missing_gfx_sprite
16	0.4%	duplicate_audio
14	0.4%	invalid_decision_reference
5	0.1%	invalid_technology_sharing
1	0.0%	localisation_issue

=== Detalhe por familia (top 5 assinaturas dentro de cada uma) ===

-- invalid_technology_reference --
  1596	[triggerimplementation.cpp:3153]	common/ai_strategy/doctrines.txt:N: has_tech: Invalid tech
  10	[trigger.cpp:700]	Invalid trigger 'coal' in common/technologies/industry.txt line: N
  10	[trigger.cpp:568]	Error: "Unknown trigger-type: coal, near line: N" in file: "common/technologies/industry.txt" near line: N
  5	[persistent.cpp:67]	Error: "Unknown modifier: local_resources_coal_factor, near line: N" in file: "common/technologies/industry.txt" near line: N
  4	[persistent.cpp:67]	Error: "Unknown modifier: always, near line: N" in file: "common/technologies/infantry.txt" near line: N

-- invalid_idea_reference --
  152	[triggerimplementation.cpp:3047]	common/units/equipment/tank_chassis.txt:N: has_idea: BUL_army_restrictions_aat is not A valid Idea
  115	[triggerimplementation.cpp:3047]	common/units/equipment/plane_airframes.txt:N: has_idea: BUL_army_restrictions_aat is not A valid Idea
  103	[triggerimplementation.cpp:3047]	common/units/equipment/ship_hull_submarine.txt:N: has_idea: BUL_army_restrictions_aat is not A valid Idea
  78	[triggerimplementation.cpp:3047]	common/units/equipment/ship_hull_light.txt:N: has_idea: BUL_army_restrictions_aat is not A valid Idea
  75	[triggerimplementation.cpp:3047]	common/units/equipment/ship_hull_heavy.txt:N: has_idea: BUL_army_restrictions_aat is not A valid Idea

-- invalid_specialization --
  113	[technologytemplate.cpp:874]	Technology has an invalid specialization "specialization_naval"
  113	[technologytemplate.cpp:874]	Technology has an invalid specialization "specialization_land"
  109	[technologytemplate.cpp:874]	Technology has an invalid specialization "specialization_air"
  19	[persistent.cpp:67]	Error: "Breakthrough cost of specialization: specialization_naval is not a valid specialization: specialization_naval, near line: N" in file: "common/
  13	[technologytemplate.cpp:874]	Technology has an invalid specialization "specialization_nuclear"

-- missing_country_tag --
  37	[countrytag.cpp:135]	ENG - is not in the tag list
  35	[countrytag.cpp:135]	GER - is not in the tag list
  34	[countrytag.cpp:135]	USA - is not in the tag list
  30	[countrytag.cpp:135]	ITA - is not in the tag list
  28	[countrytag.cpp:135]	FRA - is not in the tag list

-- outros --
  20	[effectimplementation.cpp:5544]	history/countries/DKM - Duskmoor.txt:N: recruit_character: Unknown character
  9	[trigger.cpp:700]	Invalid trigger 'PRC' in common/dynamic_modifiers/SEA_dynamic_modifiers.txt line: N
  9	[trigger.cpp:568]	Error: "Unknown trigger-type: PRC, near line: N" in file: "common/dynamic_modifiers/SEA_dynamic_modifiers.txt" near line: N
  7	[trigger.cpp:700]	Invalid trigger 'NOR' in common/dynamic_modifiers/aat_dynamic_modifiers.txt line: N
  7	[trigger.cpp:568]	Error: "Unknown trigger-type: NOR, near line: N" in file: "common/dynamic_modifiers/aat_dynamic_modifiers.txt" near line: N

-- invalid_faction_goal --
  7	[faction_template.cpp:34]	Faction goal not found in the database: faction_manifest_balkan_control
  6	[persistent.cpp:67]	Error: "Unable to find item with id: faction_goal_industrial_expansion: , near line: N | Unable to find item with id: faction_goal_defeat_of_fascism: 
  5	[faction_template.cpp:34]	Faction goal not found in the database: faction_manifest_spread_of_communism
  5	[persistent.cpp:67]	Error: "Unable to find item with id: faction_goal_industrial_expansion: , near line: N | Unable to find item with id: faction_goal_defeating_our_enemi
  4	[faction_template.cpp:34]	Faction goal not found in the database: faction_manifest_defense_of_democracy

-- invalid_raid_reference --
  7	[effect.cpp:445]	Invalid effect 'bathe_in_hellfire_nuclear' in common/raids/nuclear_raids.txt line: N
  7	[effect.cpp:358]	Error: "Unknown effect-type: bathe_in_hellfire_nuclear, near line: N" in file: "common/raids/nuclear_raids.txt" near line: N
  7	[effectimplementation.cpp:19542]	common/raids/nuclear_raids.txt:N: add_dynamic_modifier Invalid dynamic modifier fallout_atomic
  6	[effect.cpp:445]	Invalid effect 'bathe_in_hellfire_thermonuclear' in common/raids/nuclear_raids.txt line: N
  6	[effectimplementation.cpp:19542]	common/raids/nuclear_raids.txt:N: add_dynamic_modifier Invalid dynamic modifier fallout_thermonuclear

-- missing_special_project_reward --
  9	[persistent.cpp:67]	Error: "Unable to find item with id: sp_naval_generic_reward_scientist_xp_1: , near line: N | Unable to find item with id: sp_naval_generic_reward_sci
  6	[persistent.cpp:67]	Error: "Unable to find item with id: sp_rockets_scientist_xp_generic_reward: , near line: N | Unable to find item with id: sp_rockets_political_interf
  6	[scopedvariable.cpp:588]	sp:sp_air_axial_jet_engine does not match any Special Project in database
  6	[persistent.cpp:67]	Error: "invalid modifier: sp_air_intercontinental_bomber_speed_factor, near line: N" in file: "common/dynamic_modifiers/bba_dynamic_modifiers.txt" nea
  6	[persistent.cpp:67]	Error: "invalid modifier: sp_air_mothership_aircraft_speed_factor, near line: N" in file: "common/dynamic_modifiers/bba_dynamic_modifiers.txt" near li

-- invalid_trigger_doctrine --
  8	[persistent.cpp:67]	Error: "Unexpected token: category_regimental_support_artillery, near line: N" in file: "common/doctrines/subdoctrines/land/infantry_subdoctrines.txt"
  5	[persistent.cpp:67]	Error: "Unexpected token: category_regimental_support_artillery, near line: N" in file: "common/doctrines/subdoctrines/land/operations_subdoctrines.tx
  4	[persistent.cpp:67]	Error: "Unexpected token: category_regimental_support_battalions, near line: N" in file: "common/doctrines/grand_doctrines/land_grand_doctrines.txt" n
  4	[persistent.cpp:67]	Error: "Unexpected token: fire_support, near line: N" in file: "common/doctrines/subdoctrines/land/infantry_subdoctrines.txt" near line: N
  3	[persistent.cpp:67]	Error: "Unexpected token: category_tank_destroyer_regimental_support, near line: N" in file: "common/doctrines/subdoctrines/land/armor_subdoctrines.tx

-- missing_texture_asset --
  15	[character_manager.cpp:283]	Large portrait path gfx/leaders/leader_unknown.dds has unexpected format, can't compute small portrait path
  1	[texturehandler.cpp:160]	Texture Handler encountered missing texture file: gfx/leaders/AEI/Portrait_PLACEHOLDER_2_large.dds
  1	[texturehandler.cpp:216]	Couldn't find texture file: 'gfx/leaders/AEI/Portrait_PLACEHOLDER_2_large.dds'
  1	[character_manager.cpp:307]	Large portrait path gfx/leaders/THK/Thaddeus_Ironwood.dds has unexpected format, can't compute small portrait path
  1	[character_manager.cpp:319]	Result from converting gfx/leaders/THK/Adric_Von_Drachen.dds into small portrait does not exist

-- duplicate_entity --
  1	[pdx_entity.cpp:2172]	Duplicate of HOL_infantry_rider_entity added to entity system
  1	[pdx_entity.cpp:2172]	Duplicate of HOL_cavalry_entity added to entity system
  1	[pdx_entity.cpp:2172]	Duplicate of HOL_cavalry_rifle_combined_entity added to entity system
  1	[pdx_entity.cpp:2172]	Duplicate of HOL_infantry_mg_rider_entity added to entity system
  1	[pdx_entity.cpp:2172]	Duplicate of HOL_cavalry_mg_combined_entity added to entity system

-- missing_gfx_sprite --
  9	[graphics.cpp:1351]	Failed to create gui object. Could not find sprite type [GFX_country_filter_entry]
  8	[graphics.cpp:1351]	Failed to create gui object. Could not find sprite type [GFX_unplayed_content_notification]
  1	[graphics.cpp:1351]	Failed to create gui object. Could not find sprite type [GFX_subscription_widget_chinese]

-- duplicate_audio --
  1	[pdx_audio_sdl.cpp:963]	Sound with name 'sfx_ui_sd_module_turret_01' already added
  1	[assetfactory_audio.cpp:467]	Could not load sound file 'sound/menu/sfx_ui_sd_module_turrent_01.wav' in  file: sound/sound.asset line: N
  1	[pdx_audio_sdl.cpp:963]	Sound with name 'sfx_ui_sd_module_sonar_01' already added
  1	[assetfactory_audio.cpp:467]	Could not load sound file 'sound/menu/sfx_ui_sd_module_sonar_01.wav' in  file: sound/sound.asset line: N
  1	[pdx_audio_sdl.cpp:963]	Sound with name 'sfx_ui_sd_module_misc_01' already added

-- invalid_decision_reference --
  1	[effect.cpp:445]	Invalid effect 'THK_bop_very_low_increase_effect' in common/decisions/THK.txt line: N
  1	[effect.cpp:358]	Error: "Unknown effect-type: THK_bop_very_low_increase_effect, near line: N" in file: "common/decisions/THK.txt" near line: N
  1	[effect.cpp:445]	Invalid effect 'THK_bop_low_increase_effect' in common/decisions/THK.txt line: N
  1	[effect.cpp:358]	Error: "Unknown effect-type: THK_bop_low_increase_effect, near line: N" in file: "common/decisions/THK.txt" near line: N
  1	[effect.cpp:445]	Invalid effect 'THK_bop_high_increase_effect' in common/decisions/THK.txt line: N

-- invalid_technology_sharing --
  1	[technology_sharing_template.cpp:48]	There is no localization for the technology sharing group name:
  1	[trigger.cpp:700]	Invalid trigger 'HABSBURG_is_a_habsburg_viable_nation' in common/technology_sharing/12_wuw_tech_sharing_groups.txt line: N
  1	[trigger.cpp:568]	Error: "Unknown trigger-type: HABSBURG_is_a_habsburg_viable_nation, near line: N" in file: "common/technology_sharing/12_wuw_tech_sharing_groups.txt" 
  1	[trigger.cpp:700]	Invalid trigger 'BEL' in common/technology_sharing/12_wuw_tech_sharing_groups.txt line: N
  1	[trigger.cpp:568]	Error: "Unknown trigger-type: BEL, near line: N" in file: "common/technology_sharing/12_wuw_tech_sharing_groups.txt" near line: N

-- localisation_issue --
  1	[gameapplication.cpp:866]	The game has loc key collisions. Check logs/text.log for more details

Top 5 assinaturas = 54.7% do total (2089/3821)
```
