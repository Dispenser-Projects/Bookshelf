# INFO ------------------------------------------------------------------------
# Copyright © 2023 Gunivers Community.

# CODE ------------------------------------------------------------------------

kill B5-0-0-0-1
forceload remove 0 0

scoreboard objectives remove bs.in
scoreboard objectives remove bs.data
scoreboard objectives remove bs.const
scoreboard objectives remove bs.height
scoreboard objectives remove bs.width
scoreboard objectives remove bs.vel.x
scoreboard objectives remove bs.vel.y
scoreboard objectives remove bs.vel.z

data remove storage bs:in move
