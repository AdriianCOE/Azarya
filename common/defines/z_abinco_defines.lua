
--------------------------------------------------------------------------------------------------------------
-- AI AND COUNTRY CHANGES 
--------------------------------------------------------------------------------------------------------------

NDefines.NCountry.POPULATION_YEARLY_GROWTH_BASE = 0.036
NDefines.NCountry.LOCAL_MANPOWER_ACCESSIBLE_NON_CORE_FACTOR = 0.08
NDefines.NCountry.ARMY_IMPORTANCE_FACTOR = 10.0
NDefines.NCountry.TERRAIN_IMPORTANCE_FACTOR = 5.0
NDefines.NCountry.VICTORY_POINTS_IMPORTANCE_FACTOR = 5.0
NDefines.NCountry.BUILDING_IMPORTANCE_FACTOR = 1.0
NDefines.NCountry.RESOURCE_IMPORTANCE_FACTOR = 5.0

NDefines.NCountry.BASE_MAX_COMMAND_POWER = 230.0					-- base value for maximum command power
NDefines.NCountry.BASE_COMMAND_POWER_GAIN = 0.51

--------------------------------------------------------------------------------------------------------------
-- MILITARY EXPERIENCE 
--------------------------------------------------------------------------------------------------------------

NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 12
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 4
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 8

NDefines.NMilitary.MAX_ARMY_EXPERIENCE = 2500
NDefines.NMilitary.MAX_NAVY_EXPERIENCE = 1250
NDefines.NMilitary.MAX_AIR_EXPERIENCE = 1750

NDefines.NMilitary.ARMY_LEADER_XP_GAIN_PER_UNIT_IN_COMBAT = 0.15 --- MOD was 2.0 should half the increase

NDefines.NMilitary.TRAINING_MAX_DAILY_COUNTRY_EXP = 0.16			-- (Def: 0.08)*2 | Maximum army XP gained per day from training
NDefines.NMilitary.UNIT_EXPERIENCE_PER_TRAINING_DAY = 0.00225       -- (Def: 0.0015 *1.5 | No official documentation)
NDefines.NAir.AIR_WING_COUNTRY_XP_FROM_TRAINING_FACTOR = 0.0075 	-- (Def: 0.005)*1.5 | Factor on country Air XP gained from wing training
NDefines.NNavy.TRAINING_DAILY_COUNTRY_EXP_FACTOR = 0.0015			-- (Def: 0.001)*1.5 |Factor used to scale the Daily Country Navy XP gain

--------------------------------------------------------------------------------------------------------------
-- LAND COMBAT REWORK
--------------------------------------------------------------------------------------------------------------

NDefines.NMilitary.LAND_COMBAT_STR_ARMOR_DEFLECTION_FACTOR = 0.6
NDefines.NMilitary.LAND_COMBAT_ORG_ARMOR_DEFLECTION_FACTOR = 0.8
NDefines.NMilitary.RECON_SKILL_IMPACT = 7

NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_IMPACT = -0.50
NDefines.NMilitary.ANTI_AIR_TARGETTING_TO_CHANCE = 0.10
NDefines.NMilitary.TRAINING_MIN_STRENGTH = 0.2
NDefines.NMilitary.AIR_SUPPORT_BASE = 0.25
NDefines.NMilitary.PLAYER_ORDER_PLANNING_DECAY = 0.02


NDefines.NMilitary.COMBAT_STACKING_START = 10
NDefines.NMilitary.COMBAT_STACKING_EXTRA = 6
NDefines.NMilitary.COMBAT_STACKING_PENALTY = -0.08

NDefines.NMilitary.GARRISON_ORDER_ARMY_CAP_FACTOR = 4.0
NDefines.NMilitary.BASE_CAPTURE_EQUIPMENT_RATIO = 0.025

NDefines.NMilitary.HOURLY_ORG_MOVEMENT_IMPACT = -0.1 

NDefines.NMilitary.MIN_SUPPLY_CONSUMPTION = 0.01

NDefines.NMilitary.MULTIPLE_COMBATS_PENALTY = -0.25
NDefines.NMilitary.ENCIRCLED_PENALTY = -0.25

NDefines.NMilitary.TRAINING_ATTRITION = 0.01

---NDefines.NMilitary.COMBAT_OVER_WIDTH_PENALTY = -1	-- #MOD -- was -1.5,			-- over combat width penalty per %.
--#this means that exactly matching the combat width matters even less now. (1% penalty per 1% over combat width)

--- Speed ---
NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_SPEED_IMPACT = -0.0 -- #MOD -- was -0.3,     -- effect on speed due to enemy air superiority
NDefines.NMilitary.COMBAT_MOVEMENT_SPEED = 0.8 -- #MOD -- was 0.33,	               -- speed reduction base modifier in combat

NDefines.NMilitary.FUEL_CAPACITY_DEFAULT_HOURS = 144 -- #MOD -- was 96,				-- default capacity if not specified

--- Tactics and Recon ---
NDefines.NMilitary.INITIATIVE_PICK_COUNTER_ADVANTAGE_FACTOR  = 0.45 -- #MOD -- was 0.35, -- advantage per leader level for picking a counter

--- War Score ---
NDefines.NMilitary.WAR_SCORE_AIR_IC_LOSS_FACTOR = 0.008						-- war score gained for every IC of damage done to an enemy's air mission
NDefines.NMilitary.WAR_SCORE_LAND_DAMAGE_FACTOR = 0.01          				-- war score gained for every strengh damage done to an enemy's army
NDefines.NMilitary.WAR_SCORE_LAND_IC_LOSS_FACTOR = 0.008         				-- war score gained for every IC damage done to an enemy's army

NDefines.NMilitary.DIG_IN_FACTOR = 0.01 -- 0.02						   -- bonus factor for each dug-in level

NDefines.NMilitary.LAND_COMBAT_COLLATERAL_INFRA_FACTOR = 0.007

NDefines.NMilitary.FLANKED_PROVINCES_COUNT = 2

--------------------------------------------------------------------------------------------------------------
-- AIR COMBAT REWORK
--------------------------------------------------------------------------------------------------------------

NDefines.NAir.AIR_WING_FLIGHT_SPEED_MULT = 0.04
NDefines.NAir.AIR_WING_MAX_STATS_ATTACK = 200
NDefines.NAir.AIR_WING_MAX_STATS_DEFENCE = 200
NDefines.NAir.AIR_WING_MAX_STATS_AGILITY = 200
NDefines.NAir.AIR_WING_MAX_STATS_SPEED = 2000
NDefines.NAir.AIR_WING_MAX_STATS_BOMBING = 200
NDefines.NAir.BIGGEST_AGILITY_FACTOR_DIFF = 5.0
NDefines.NAir.AIR_DEPLOYMENT_DAYS = 1	-- #MOD-- was 2,				-- Days to deploy one air wing
--# I hate this so much!

NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_TRUCK_DAMAGE_FACTOR = 0.35
NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_TRAIN_DAMAGE_FACTOR = 0.065
NDefines.NAI.LAND_COMBAT_ANTI_LOGISTICS_PER_ENEMY_ARMY = 5     -- Amount of CAS planes requested per enemy army for anti-logistics
NDefines.NAir.ANTI_AIR_PLANE_DAMAGE_FACTOR = 0.5				-- Anti Air Gun Damage factor
NDefines.NAir.CAS_NIGHT_ATTACK_FACTOR = 0.5	-- #MOD-- was 0.1,			-- CAS damaged get multiplied by this in land combats at night
--#large buff to CAS. should result in 36% more CAS damage on average (1.5/1.1) (100% at day + 50% at night is 1.5 for mod, and 1.1 for vanilla)
--#also, CAS was apparently utter trash at night, which means that in timeszones with bad sortie timing, CAS was way weaker than elsewhere. Eastern France, Benelux, and Indian Ocean were such zones). This should now not matter anymore. Also, Land units get -50% at night, why would CAS get -90% instead?

NDefines.NAir.NAVAL_STRIKE_DAMAGE_TO_STR = 0.5					-- Balancing value to convert damage ( naval_strike_attack * hits ) to Strength reduction.
NDefines.NAir.NAVAL_STRIKE_DAMAGE_TO_ORG = 0.75					-- Balancing value to convert damage ( naval_strike_attack * hits ) to Organisation reduction.
NDefines.NAir.NAVAL_STRIKE_CARRIER_MULTIPLIER = 30.0              -- damage bonus when planes are in naval combat where their carrier is present (and can thus sortie faster and more effectively)
NDefines.NAir.NAVAL_STRIKE_TARGETTING_TO_AMOUNT = 0.5			-- Balancing value to convert the naval_strike_targetting equipment stats to chances of how many airplanes managed to do successfull strike.


--------------------------------------------------------------------------------------------------------------
-- NAVAL COMBAT REWORK
--------------------------------------------------------------------------------------------------------------

NDefines.NNavy.ANTI_AIR_TARGETTING_TO_CHANCE = 0.5		-- Balancing value to convert averaged equipment stats (anti_air_targetting and naval_strike_agility) to probability chances of airplane being hit by navies AA.
NDefines.NNavy.ANTI_AIR_ATTACK_TO_AMOUNT = 0.005			-- Balancing value to convert equipment stat anti_air_attack to the random % value of airplanes being hit.
NDefines.NNavy.NAVAL_COMBAT_RESULT_TIMEOUT_YEARS = 24							-- after that many years we clear the naval combat results so they don't get stuck forever in the memory.
NDefines.NNavy.CONVOY_LOSS_HISTORY_TIMEOUT_MONTHS = 24					-- after this many months remove the history of lost convoys to not bloat savegames and memory since there is no way to see them anyway
NDefines.NNavy.NAVAL_COMBAT_AIR_CAPITAL_TARGET_SCORE = 50
NDefines.NNavy.NAVAL_COMBAT_AIR_CARRIER_TARGET_SCORE = 100
NDefines.NNavy.HIGHER_SHIP_RATIO_POSITIONING_PENALTY_FACTOR	= 0.75 -- if one side has more ships than the other that side will get this penalty for each +100% ship ratio it has
NDefines.NNavy.SUB_DETECTION_CHANCE_BASE_SPOTTING_EFFECT = 1.0			-- effect of base spotting for initial spotting of pure submarine forces. this along with next value is added together and rolled against a random to start spotting
NDefines.NNavy.SUB_DETECTION_CHANCE_SPOTTING_SPEED_EFFECT = 4.0				-- effect of spotting speed for initial spotting of pure submarine forces. this along with prev value is added together and rolled against a random to start spotting
NDefines.NNavy.SUB_DETECTION_CHANCE_BASE_SPOTTING_POW_EFFECT = 3.0	

NDefines.NNavy.ANTI_AIR_POW_ON_INCOMING_AIR_DAMAGE = 0.2	-- received air damage is calculated using following: 1 - ( (ship_anti_air + fleet_anti_air * SHIP_TO_FLEET_ANTI_AIR_RATIO )^ANTI_AIR_POW_ON_INCOMING_AIR_DAMAGE ) * ANTI_AIR_MULT_ON_INCOMING_AIR_DAMAGE
NDefines.NNavy.ANTI_AIR_MULT_ON_INCOMING_AIR_DAMAGE	= 0.15
NDefines.NNavy.MAX_ANTI_AIR_REDUCTION_EFFECT_ON_INCOMING_AIR_DAMAGE = 0.5	-- damage reduction for incoming air attacks is clamped to this value at maximum.

NDefines.NNavy.AGGRESSION_SETTINGS_VALUES = { -- ships will use this values while deciding to attack enemies
		0,		-- do not engage
		1.0,	-- low
		1.5,	-- medium
		2.5,	-- high
		10000,	-- I am death incarnate!
	}
	
NDefines.NNavy.WAR_SCORE_GAIN_FOR_SUNK_SHIP_MANPOWER_FACTOR = 0.002			-- war score gained for every manpower killed when sinking a ship
NDefines.NNavy.WAR_SCORE_GAIN_FOR_SUNK_SHIP_PRODUCTION_COST_FACTOR = 0.01		-- war score gained for every IC of the sunk ship
NDefines.NNavy.EXPERIENCE_FACTOR_CARRIER_GAIN = 0.04							-- Xp gain by carrier ships in the combat

NDefines.NNavy.CARRIER_STACK_PENALTY = 8 -- The most efficient is 4 carriers in combat. 5+ brings the penalty to the amount of wings in battle.
NDefines.NNavy.ANTI_AIR_TARGETTING_TO_CHANCE = 0.07 -- Balancing value to convert averaged equipment stats (anti_air_targetting and naval_strike_agility) to probability chances of airplane being hit by navies AA.
NDefines.NNavy.ANTI_AIR_ATTACK_TO_AMOUNT = 0.005 -- Balancing value to convert equipment stat anti_air_attack to the random % value of airplanes being hit.

--------------------------------------------------------------------------------------------------------------
-- ARMOUR DAMAGE REWORK
--------------------------------------------------------------------------------------------------------------

NDefines.NMilitary.PIERCING_THRESHOLDS = {					-- Our piercing / their armor must be this value to deal damage fraction equal to the index in the array below [higher number = higher penetration]. If armor is 0, 1.00 will be returned.
		7.50,
		2.00,
		1.75,
		1.50,
		1.25,
		1.00,
		0.80,
		0.60,
		0.40,
		0.00, --there isn't much point setting this higher than 0
	}
	
NDefines.NMilitary.PIERCING_THRESHOLD_DAMAGE_VALUES = {	-- 0 armor will always receive maximum damage (so add overmatching at your own peril). the system expects at least 2 values, with no upper limit.
		1.00,
		2.00,
		1.75,
		1.50,
		1.25,
		1.00,
		0.75,
		0.50,
		0.30,
		0.20,
	}

NDefines.NMilitary.ARMOR_VS_AVERAGE = 0.2  -- 护甲和平均值的比例
NDefines.NMilitary.PEN_VS_AVERAGE = 0.2  -- 穿透和平均值的比例
NDefines.NMilitary.LAND_COMBAT_STR_ARMOR_ON_SOFT_DICE_SIZE = 6  -- 金盾状态下的hp伤害骰子数
NDefines.NMilitary.LAND_COMBAT_ORG_ARMOR_ON_SOFT_DICE_SIZE = 14  -- 金盾状态下的组织度伤害骰子数

--------------------------------------------------------------------------------------------------------------
-- STRATEGIC BOMBING DAMAGE REWORK
--------------------------------------------------------------------------------------------------------------

---NDefines.NCountry.BOMBING_WAR_SUPPORT_PENALTY_SCALE = -100.00 			-- Scaling of bomber damage to war support impact, will be added weekly as a war support penalty
---NDefines.NCountry.MAX_BOMBING_WEEKLY_WAR_SUPPORT_PENALTY = -0.50		-- Max penalty that will gained per week from bomber's damage
---NDefines.NCountry.BOMBING_WEEKLY_WAR_SUPPORT_PENALTY_DECAY = 0.10		-- Weekly decay of bomber damage war support penalty

NDefines.NAir.AIR_WING_BOMB_DAMAGE_FACTOR = 5					-- Used to balance the damage done while bombing.

NDefines.NAir.BOMBING_TARGETING_RANDOM_FACTOR = 0.15							-- % of picking the wrong target

NDefines.NAir.BASE_STRATEGIC_BOMBING_HIT_SHIP_CHANCE = 0.1		-- Chance to hit a ship in port when it is bombed.
NDefines.NAir.BASE_STRATEGIC_BOMBING_HIT_SHIP_DAMAGE_FACTOR = 50
NDefines.NAir.BASE_STRATEGIC_BOMBING_HIT_PLANE_CHANCE = 0.25		-- Chance to hit a plane in airbase when it is bombed.
NDefines.NAir.BASE_STRATEGIC_BOMBING_HIT_PLANE_DAMAGE_FACTOR = 50

--------------------------------------------------------------------------------------------------------------
-- STRATEGIC NAVAL BOMBARDEMENT REWORK
--------------------------------------------------------------------------------------------------------------

NDefines.NNavy.SHORE_BOMBARDMENT_CAP = 0.35
NDefines.NNavy.HEAVY_GUN_ATTACK_TO_SHORE_BOMBARDMENT = 0.1  -- heavy gun attack value is divided by this value * 100 and added to shore bombardment modifier
NDefines.NNavy.LIGHT_GUN_ATTACK_TO_SHORE_BOMBARDMENT = 0.05 -- light gun attack value is divided by this value * 100 and added to shore bombardment modifier

--------------------------------------------------------------------------------------------------------------
-- SUPPLY FLOW REWORK
--------------------------------------------------------------------------------------------------------------

NDefines.NSupply.VP_TO_SUPPLY_BASE = 0.2 -- Bonus to supply from a VP, no matter the level (Base is 0.2)
NDefines.NSupply.AVAILABLE_MANPOWER_STATE_SUPPLY = 0.5 --Factor for state supply from max manpower (population) (Base is 0.18, this is PER MILLION.)
NDefines.NSupply.VP_TO_SUPPLY_BONUS_CONVERSION = 0.05 -- Bonus to supply local supplies from Victory Points, multiplied by this aspect and rounded to closest integer (Base is 0.05)
NDefines.NSupply.CAPITAL_INITIAL_SUPPLY_FLOW = 5.0 -- starting supply from
NDefines.NSupply.CAPITAL_STARTING_PENALTY_PER_PROVINCE = 0.5 -- starting penalty that will be added as supply moves away from its origin (modified by stuff like terrain) (Default is 0.5)
NDefines.NSupply.CAPITAL_ADDED_PENALTY_PER_PROVINCE = 1.2 -- added penalty as we move away from origin (Default is 1.2)

-- defines that are used for supply reach for built nodes
NDefines.NSupply.NODE_INITIAL_SUPPLY_FLOW = 2.8
NDefines.NSupply.NODE_STARTING_PENALTY_PER_PROVINCE = 0.30 -- default is 0.5
NDefines.NSupply.NODE_ADDED_PENALTY_PER_PROVINCE = 0.50 -- default is 0.7

-- defines that are used for supply reach for dockyards
NDefines.NSupply.NAVAL_BASE_INITIAL_SUPPLY_FLOW = 3.3
NDefines.NSupply.NAVAL_BASE_STARTING_PENALTY_PER_PROVINCE = 0.84
NDefines.NSupply.NAVAL_BASE_ADDED_PENALTY_PER_PROVINCE = 1.1

--------------------------------------------------------------------------------------------------------------
-- EXPERIMENTAL DEFINES
--------------------------------------------------------------------------------------------------------------

NDefines.NMilitary.COMBAT_MINIMUM_TIME = 6
NDefines.NMilitary.COMBAT_VALUE_ORG_IMPORTANCE = 1.3		-- Multiplier on TotalOrganisation when determining the combat value of a division
NDefines.NMilitary.SPOTTING_QUALITY_DROP_HOURS = 5 	-- Each X hours the intel quality drops after unit was spotted.
NDefines.NMilitary.LAND_COMBAT_STR_DAMAGE_MODIFIER = 0.04        -- global damage modifier... but some equipment is returned at end of battles see : EQUIPMENT_COMBAT_LOSS_FACTOR
NDefines.NMilitary.LAND_COMBAT_ORG_DAMAGE_MODIFIER = 0.06        -- global damage modifier
NDefines.NMilitary.COMBAT_MOVEMENT_SPEED = 0.25	               -- speed reduction base modifier in combat
NDefines.NMilitary.UNIT_DIGIN_CAP = 7                           -- how "deep" you can dig you can dig in until hitting max bonus
NDefines.NMilitary.UNIT_DIGIN_SPEED = 0.9						   -- how "deep" you can dig a day.
NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_DEFENSE_STEEPNESS = 120 -- how quickly defense approaches the max impact diminishing returns curve
NDefines.NMilitary.ORG_LOSS_FACTOR_ON_CONQUER = 0.3              -- percentage of (max) org loss on takign enemy province


NDefines.NAir.COMBAT_MULTIPLANE_CAP = 2.0		-- How much bonus gives the airplanes amount advantage (2vs1) to winning the situation.
NDefines.NAir.HOURS_DELAY_AFTER_EACH_COMBAT = 7					-- How many hours needs the wing to be ready for the next combat. Use for tweaking if combats happens too often. (generally used as double because of roundtrip)
NDefines.NAir.CARRIER_HOURS_DELAY_AFTER_EACH_COMBAT = 8          -- how often carrier planes do battle inside naval combat
NDefines.NAir.AA_INDUSTRY_AIR_DAMAGE_FACTOR = -0.15				-- 5x levels = 60% defense from bombing
NDefines.NMilitary.LAND_AIR_COMBAT_MAX_PLANES_PER_ENEMY_WIDTH = 4 -- how many CAS/TAC can enter a combat depending on enemy width there


NDefines.NNavy.COMBAT_BASE_HIT_CHANCE = 0.05									-- base chance for hit
NDefines.NNavy.COMBAT_EVASION_TO_HIT_CHANCE = 0.025							-- we take ship evasion stats, and mult by this value, so it gives hit chance reduction. So if reduction is 0.025 and ship evasion = 10, then there will be 0.25 (25%) lower hit chance. (Fe. 50% base -25% from evasion +10% bcoz it's very close).
NDefines.NNavy.COMBAT_MIN_HIT_CHANCE = 0.03									-- never less hit chance then this?
NDefines.NNavy.COMBAT_EVASION_TO_HIT_CHANCE_TORPEDO_MULT = 50.0				-- the above evasion hit chance is multiplied by 400% if shooting with torpedos. Torpedoes are slow so evasion matters more.
NDefines.NNavy.COMBAT_TORPEDO_CRITICAL_DAMAGE_MULT = 3.0						-- multiplier to damage when got critical hit from torpedo. (Critical hits are devastating as usualy torpedo_attack are pretty high base values).
NDefines.NNavy.COMBAT_DAMAGE_TO_STR_FACTOR = 0.6								-- casting damage value to ship strength multiplier. Use it ot balance the game difficulty.
NDefines.NNavy.COMBAT_CHASE_RESIGNATION_HOURS = 10								-- Before we resign chasing enemy, give them some minimum time so the combat doesn't end instantly.
NDefines.NNavy.COMBAT_MAX_GROUPS = 2										-- Max amount of "Fire Exchange" groups (FEX).
NDefines.NNavy.NAVAL_SUPREMACY_CAN_INVADE = 0.6								-- required naval supremacy to perform invasions on an area
NDefines.NNavy.SUBMARINE_REVEAL_BASE_CHANCE = 0.04							-- Base chance for submarine detection. It's modified by the difference of a spootter's submarines detection vs submarine visibility. Use this variable for game balancing.


NDefines.NMilitary.ATTRITION_DAMAGE_ORG = 0.3
NDefines.NMilitary.ATTRITION_EQUIPMENT_LOSS_CHANCE = 0.005
NDefines.NMilitary.OUT_OF_SUPPLY_ATTRITION = 0.15                 -- max attrition when out of supply
NDefines.NMilitary.OUT_OF_SUPPLY_SPEED = -0.92                    -- max speed reduction from supply
NDefines.NMilitary.NON_CORE_SUPPLY_SPEED = -0.7				   -- we are not running on our own VP supply so need to steal stuff along the way
NDefines.NMilitary.OUT_OF_SUPPLY_MORALE = -0.3                   -- max org regain reduction from supply

NDefines.NMilitary.PARACHUTE_COMPLETE_ORG = 0.5				   -- Organisation value (in %) after unit being dropped regardless if failed disrupted or successful.


NDefines.NMilitary.RIVER_CROSSING_PENALTY_LARGE = -0.8           -- large river crossing
NDefines.NMilitary.RIVER_CROSSING_SPEED_PENALTY = -0.30           -- small river crossing
NDefines.NMilitary.RIVER_CROSSING_SPEED_PENALTY_LARGE = -0.7     -- large river crossing
NDefines.NMilitary.BASE_FORT_PENALTY = -0.20 					   -- fort penalty		#HOI4TGW ::: BASE_FORT_PENALTY = -0.15
NDefines.NMilitary.MULTIPLE_COMBATS_PENALTY = -0.6               -- defender penalty if attacked from multiple directions
