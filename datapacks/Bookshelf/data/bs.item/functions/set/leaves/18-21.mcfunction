execute if score @s bs.item.id matches 18 run summon item ~ ~ ~ {PickupDelay:999999,Tags:["bs.new"],"Item":{"id":"minecraft:allay_spawn_egg","Count":1b}}
execute if score @s bs.item.id matches 19 run summon item ~ ~ ~ {PickupDelay:999999,Tags:["bs.new"],"Item":{"id":"minecraft:allium","Count":1b}}
execute if score @s bs.item.id matches 20 run summon item ~ ~ ~ {PickupDelay:999999,Tags:["bs.new"],"Item":{"id":"minecraft:amethyst_block","Count":1b}}
execute if score @s bs.item.id matches 21 run summon item ~ ~ ~ {PickupDelay:999999,Tags:["bs.new"],"Item":{"id":"minecraft:amethyst_cluster","Count":1b}}
scoreboard players operation @e[type=item,tag=bs.new,limit=1,sort=nearest] bs.id.parent = @s bs.id