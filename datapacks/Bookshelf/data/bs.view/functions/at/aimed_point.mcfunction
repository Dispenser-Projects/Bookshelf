# INFO ------------------------------------------------------------------------
# Copyright © 2024 Gunivers Community.

# Authors: Aksiome
# Contributors:

# Version: 1.0
# Created: 25/01/2024 (1.20.4)
# Last modification: 25/01/2024 (1.20.4)

# Documentation: https://bookshelf.docs.gunivers.net/en/latest/modules/view.html#aimed-point
# Dependencies:
# Note:

# CODE ------------------------------------------------------------------------

# run the raycast
data modify storage bs:data view.raycast set from storage bs:in raycast
data modify storage bs:in raycast merge value {block_collision:true,entity_collision:true}
execute at @s anchored eyes positioned ^ ^ ^ run function #bs.raycast:run
data modify storage bs:in raycast set from storage bs:data view.raycast

# run the command at the hit point that was found or return early
execute if score #raycast.distance bs.data matches 2147483647 run return 0
$data modify storage bs:ctx _ set value '$(run)'
data modify storage bs:ctx x set from storage bs:out raycast.hit_point[0]
data modify storage bs:ctx y set from storage bs:out raycast.hit_point[1]
data modify storage bs:ctx z set from storage bs:out raycast.hit_point[2]
execute at @s run function bs.view:at/run with storage bs:ctx
