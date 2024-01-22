# INFO ------------------------------------------------------------------------
# Copyright © 2023 Gunivers Community.

# Authors: Aksiome
# Contributors:

# Version: 1.0
# Created: 22/01/2024 (1.20.4)
# Last modification: 22/01/2024 (1.20.4)

# Documentation: https://bookshelf.docs.gunivers.net/en/latest/modules/position.html
# Dependencies:
# Note:

# CODE ------------------------------------------------------------------------

$execute store result storage bs:ctx x double $(scale) run scoreboard players get @s bs.pos.x
$execute store result storage bs:ctx y double $(scale) run scoreboard players get @s bs.pos.y
$execute store result storage bs:ctx z double $(scale) run scoreboard players get @s bs.pos.z
$execute store result storage bs:ctx h double $(scale) run scoreboard players get @s bs.rot.h
$execute store result storage bs:ctx v double $(scale) run scoreboard players get @s bs.rot.v
function bs.position:add/pos_and_rot/run with storage bs:ctx
