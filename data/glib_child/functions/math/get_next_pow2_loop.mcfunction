scoreboard players operation @s glib.res0 *= 2 glib.const
scoreboard players add @s glib.res1 1
execute if score @s glib.res0 < @s glib.var0 run function glib_child:math/get_next_pow2_loop
