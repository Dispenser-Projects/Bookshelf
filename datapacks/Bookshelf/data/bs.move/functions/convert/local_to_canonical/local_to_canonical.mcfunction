# INFO ------------------------------------------------------------------------
# Copyright © 2024 Gunivers Community.

# Authors: Aksiome
# Contributors:

# Version: 1.0
# Created: 25/12/2023 (1.20.4)
# Last modification: 25/12/2023 (1.20.4)

# Documentation: https://bookshelf.docs.gunivers.net/en/latest/modules/move.html#local-to-canonical
# Dependencies:
# Note:

# CODE ------------------------------------------------------------------------

# sincos(h: Phi) & sincos(v: Theta)
execute as B5-0-0-0-1 run function bs.move:convert/local_to_canonical/sincos

# X' = Z * sin(h) + X * cos(h)
scoreboard players operation #move.local_to_canonical.x bs.data = @s bs.vel.z
scoreboard players operation #move.local_to_canonical.x bs.data *= #move.local_to_canonical.sin.h bs.data
scoreboard players operation #move.local_to_canonical bs.data = @s bs.vel.x
scoreboard players operation #move.local_to_canonical bs.data *= #move.local_to_canonical.cos.h bs.data
scoreboard players operation #move.local_to_canonical.x bs.data += #move.local_to_canonical bs.data
scoreboard players operation #move.local_to_canonical.x bs.data /= 1000 bs.const

# Y' = (z * cos(h) - x * sin(h)) * sin(v) + y * cos(v)
scoreboard players operation #move.local_to_canonical.y bs.data = @s bs.vel.z
scoreboard players operation #move.local_to_canonical.y bs.data *= #move.local_to_canonical.cos.h bs.data
scoreboard players operation #move.local_to_canonical bs.data = @s bs.vel.x
scoreboard players operation #move.local_to_canonical bs.data *= #move.local_to_canonical.sin.h bs.data
scoreboard players operation #move.local_to_canonical.y bs.data -= #move.local_to_canonical bs.data
execute store result score #move.local_to_canonical.z bs.data run scoreboard players operation #move.local_to_canonical.y bs.data /= 1000 bs.const
scoreboard players operation #move.local_to_canonical.y bs.data *= #move.local_to_canonical.sin.v bs.data
scoreboard players operation #move.local_to_canonical bs.data = @s bs.vel.y
scoreboard players operation #move.local_to_canonical bs.data *= #move.local_to_canonical.cos.v bs.data
scoreboard players operation #move.local_to_canonical.y bs.data += #move.local_to_canonical bs.data
scoreboard players operation #move.local_to_canonical.y bs.data /= 1000 bs.const

# Z' = (z * cos(h) - x * sin(h)) * cos(v) - y * sin(v)
scoreboard players operation #move.local_to_canonical.z bs.data *= #move.local_to_canonical.cos.v bs.data
scoreboard players operation #move.local_to_canonical bs.data = @s bs.vel.y
scoreboard players operation #move.local_to_canonical bs.data *= #move.local_to_canonical.sin.v bs.data
scoreboard players operation #move.local_to_canonical.z bs.data -= #move.local_to_canonical bs.data
scoreboard players operation #move.local_to_canonical.z bs.data /= 1000 bs.const

scoreboard players operation @s bs.vel.x = #move.local_to_canonical.x bs.data
scoreboard players operation @s bs.vel.y = #move.local_to_canonical.y bs.data
scoreboard players operation @s bs.vel.z = #move.local_to_canonical.z bs.data
