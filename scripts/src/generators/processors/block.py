import math
from generators.contracts import DataProcessor

ITEMS_DICT = {
    "minecraft:wall_torch": "minecraft:torch",
    "minecraft:soul_wall_torch": "minecraft:soul_torch",
    "minecraft:redstone_wall_torch": "minecraft:redstone_torch",
    "minecraft:oak_wall_sign": "minecraft:oak_sign",
    "minecraft:spruce_wall_sign": "minecraft:spruce_sign",
    "minecraft:birch_wall_sign": "minecraft:birch_sign",
    "minecraft:jungle_wall_sign": "minecraft:jungle_sign",
    "minecraft:acacia_wall_sign": "minecraft:acacia_sign",
    "minecraft:cherry_wall_sign": "minecraft:cherry_sign",
    "minecraft:dark_oak_wall_sign": "minecraft:dark_oak_sign",
    "minecraft:mangrove_wall_sign": "minecraft:mangrove_sign",
    "minecraft:bamboo_wall_sign": "minecraft:bamboo_sign",
    "minecraft:crimson_wall_sign": "minecraft:crimson_sign",
    "minecraft:warped_wall_sign": "minecraft:warped_sign",
    "minecraft:oak_wall_hanging_sign": "minecraft:oak_hanging_sign",
    "minecraft:spruce_wall_hanging_sign": "minecraft:spruce_hanging_sign",
    "minecraft:birch_wall_hanging_sign": "minecraft:birch_hanging_sign",
    "minecraft:jungle_wall_hanging_sign": "minecraft:jungle_hanging_sign",
    "minecraft:acacia_wall_hanging_sign": "minecraft:acacia_hanging_sign",
    "minecraft:cherry_wall_hanging_sign": "minecraft:cherry_hanging_sign",
    "minecraft:dark_oak_wall_hanging_sign": "minecraft:dark_oak_hanging_sign",
    "minecraft:mangrove_wall_hanging_sign": "minecraft:mangrove_hanging_sign",
    "minecraft:bamboo_wall_hanging_sign": "minecraft:bamboo_hanging_sign",
    "minecraft:crimson_wall_hanging_sign": "minecraft:crimson_hanging_sign",
    "minecraft:warped_wall_hanging_sign": "minecraft:warped_hanging_sign",
    "minecraft:tube_coral_wall_fan": "minecraft:tube_coral_fan",
    "minecraft:brain_coral_wall_fan": "minecraft:brain_coral_fan",
    "minecraft:bubble_coral_wall_fan": "minecraft:bubble_coral_fan",
    "minecraft:fire_coral_wall_fan": "minecraft:fire_coral_fan",
    "minecraft:horn_coral_wall_fan": "minecraft:horn_coral_fan",
    "minecraft:dead_tube_coral_wall_fan": "minecraft:dead_tube_coral_fan",
    "minecraft:dead_brain_coral_wall_fan": "minecraft:dead_brain_coral_fan",
    "minecraft:dead_bubble_coral_wall_fan": "minecraft:dead_bubble_coral_fan",
    "minecraft:dead_fire_coral_wall_fan": "minecraft:dead_fire_coral_fan",
    "minecraft:dead_horn_coral_wall_fan": "minecraft:dead_horn_coral_fan",
    "minecraft:white_wall_banner": "minecraft:white_banner",
    "minecraft:orange_wall_banner": "minecraft:orange_banner",
    "minecraft:magenta_wall_banner": "minecraft:magenta_banner",
    "minecraft:light_blue_wall_banner": "minecraft:light_blue_banner",
    "minecraft:yellow_wall_banner": "minecraft:yellow_banner",
    "minecraft:lime_wall_banner": "minecraft:lime_banner",
    "minecraft:pink_wall_banner": "minecraft:pink_banner",
    "minecraft:gray_wall_banner": "minecraft:gray_banner",
    "minecraft:light_gray_wall_banner": "minecraft:light_gray_banner",
    "minecraft:cyan_wall_banner": "minecraft:cyan_banner",
    "minecraft:purple_wall_banner": "minecraft:purple_banner",
    "minecraft:blue_wall_banner": "minecraft:blue_banner",
    "minecraft:brown_wall_banner": "minecraft:brown_banner",
    "minecraft:green_wall_banner": "minecraft:green_banner",
    "minecraft:red_wall_banner": "minecraft:red_banner",
    "minecraft:black_wall_banner": "minecraft:black_banner",
    "minecraft:player_wall_head": "minecraft:player_head",
    "minecraft:zombie_wall_head": "minecraft:zombie_head",
    "minecraft:creeper_wall_head": "minecraft:creeper_head",
    "minecraft:dragon_wall_head": "minecraft:dragon_head",
    "minecraft:piglin_wall_head": "minecraft:piglin_head",
    "minecraft:skeleton_wall_skull": "minecraft:skeleton_skull",
    "minecraft:wither_skeleton_wall_skull": "minecraft:wither_skeleton_skull",
    "minecraft:redstone_wire": "minecraft:redstone",
    "minecraft:tripwire": "minecraft:string",
    "minecraft:water": "minecraft:water_bucket",
    "minecraft:lava": "minecraft:lava_bucket",
    "minecraft:powder_snow": "minecraft:powder_snow_bucket",
    "minecraft:big_dripleaf_stem": "minecraft:big_dripleaf",
    "minecraft:wheat": "minecraft:wheat_seeds",
    "minecraft:cocoa": "minecraft:cocoa_beans",
    "minecraft:melon_stem": "minecraft:pumpkin_seeds",
    "minecraft:pumpkin_stem": "minecraft:pumpkin_seeds",
    "minecraft:attached_melon_stem": "minecraft:melon_seeds",
    "minecraft:attached_pumpkin_stem": "minecraft:melon_seeds",
    "minecraft:water_cauldron": "minecraft:cauldron",
    "minecraft:lava_cauldron": "minecraft:cauldron",
    "minecraft:powder_snow_cauldron": "minecraft:cauldron",
    "minecraft:carrots": "minecraft:carrot",
    "minecraft:potatoes": "minecraft:potato",
    "minecraft:torchflower_crop": "minecraft:torchflower_seeds",
    "minecraft:pitcher_crop": "minecraft:pitcher_pod",
    "minecraft:beetroots": "minecraft:beetroot_seeds",
    "minecraft:sweet_berry_bush": "minecraft:sweet_berries",
    "minecraft:cave_vines": "minecraft:glow_berries",
    "minecraft:cave_vines_plant": "minecraft:glow_berries",
}

def get_item(type: str, data) -> dict:
    value = ITEMS_DICT.get(type, type)
    return {"item":value} if value in data.items else {}


class CreateTagsFiles(DataProcessor):
    def process(self, data):
        print("\033[90m⚙️ Generating tags files\033[0m")

        file = self.target / "has_state.json"
        values = [block["type"] for block in data.types if block["group"] > 0]
        self.write_json(self.target / "has_state.json", { "values": values })

        for bit in range(math.floor(math.log2(len(data.types))) + 1):
            file = self.target / f"type/group_{2**bit}.json"
            values = [block["type"] for i, block in enumerate(data.types, 1) if (i >> bit) & 1]
            self.write_json(file, { "values": values })


class CreateBlockTableFile(DataProcessor):
    def process(self, data):
        print("\033[90m⚙️ Generating types table function\033[0m")

        self.write_text(self.target, [
            "# This file was automatically generated, do not edit it",
            (f"data modify storage bs:const block.table set value "
             f"{self.render(self.format(data))}"),
        ])

    def format(self, data) -> list:
        return [{
            "group": block["group"],
            "type": block["type"],
            **get_item(block["type"], data),
        } for block in data.types]


class CreateBlockTypesFile(DataProcessor):
    def process(self, data):
        print("\033[90m⚙️ Generating types table function\033[0m")

        self.write_text(self.target, [
            "# This file was automatically generated, do not edit it",
            (f"data modify storage bs:const block.types set value "
             f"{self.render(self.format(data))}"),
        ])

    def format(self, data):
        return {
            f'"{block["type"]}"': idx
            for idx, block in enumerate(data.types)
        } | {
            f'"{block["type"][10:]}"': idx
            for idx, block in enumerate(data.types)
        }


class CreateBlockItemsFile(DataProcessor):
    def process(self, data):
        print("\033[90m⚙️ Generating types table function\033[0m")

        self.write_text(self.target, [
            "# This file was automatically generated, do not edit it",
            (f"data modify storage bs:const block.items set value "
             f"{self.render(self.format(data))}"),
        ])

    def format(self, data):
        ret = {}
        for idx, block in enumerate(data.types):
            item = ITEMS_DICT.get(block["type"], block["type"])
            key = f'"{item}"'
            if item in data.items and key not in ret:
                ret[key] = idx
                ret[f'"{item[10:]}"'] = idx
        return ret


class CreateStatesFile(DataProcessor):
    def process(self, data):
        print("\033[90m⚙️ Generating states table function\033[0m")

        self.write_text(self.target, [
            "# This file was automatically generated, do not edit it",
            *[
                (f"data modify storage bs:const "
                 f"block.table[{{group:{str(group + 1)}}}]._ set value "
                 f"{self.render(self.format(states))}")
                for group, states in enumerate(data.groups[1:])
            ]
        ])

    def format(self, states: dict) -> list:
        return [{
            "n": name,
            "o": [{
                "i": index,
                "v": value,
                "s": {state_idx: f"{name}={value},"},
                "p": {name: value},
            } for index, value in enumerate(options)],
        } for state_idx, (name, options) in enumerate(states.items())]


class CreateRegistryFiles(DataProcessor):
    def process(self, data):
        print("\033[90m⚙️ Generating registry functions\033[0m")

        for group, states in enumerate(data.groups[1:]):
            self.write_text(self.target / f"{group + 1}.mcfunction", [
                "# This file was automatically generated, do not edit it",
                *[
                    (f'execute if block ~ ~ ~ #bs.block:has_state[{name}={value}] run '
                     f'data modify storage bs:out block._'
                     f'[{{n:"{name}"}}].o[{{v:"{value}"}}].c set value 1b')
                    for name, options in states.items() for value in options
                ]
            ])


class UpdateStorageFile(DataProcessor):
    def process(self, data):
        print("\033[90m⚙️ Updating storage file asset\033[0m")

        self.write_nbt(
            self.target,
            self.render(self.format(data)),
            ".data.contents.const.block",
        )

    def format(self, data) -> list:
        return [{
            "group": block["group"],
            "type": block["type"],
            **get_item(block["type"], data),
            "_": self.format_states(data.groups[block["group"]])
        } for block in data.types]

    def format_states(self, states: dict) -> list:
        return [{
            "n": name,
            "o": [{
                "i": index,
                "v": value,
                "s": f"{name}={value},",
                "p": {name: value},
            } for index, value in enumerate(options)],
        } for name, options in states.items()]
