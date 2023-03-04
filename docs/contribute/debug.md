---
html_theme.sidebar_secondary.remove: true
---

# 🪲 Debug

It is possible to add debug lines anywhere in the code. However, these must be subject to conditions. For the debug to be displayed to a player, that player must have the tag `bs.debug.<PATH>` where `<PATH>` is the path to the function. In the tags, this path is written ith `.` as separators. Example: `bs.vector:classic/get_ata` => `bs.debug.vector.classic.get_ata`

There is 3 different types of debug messages:
- Error: which display every critical situation
- Warning: for errors that can be managed by the libs
- Record: to let the user know what happen during the execution of the system

Every debug message must be visually opened using the following tellraws:

- **Error without source entity**
   ```
   tellraw @a[tag=bs.debug.<PATH>] [{"text":" > ","bold":true,"color":"gold"},{"text":"Glib","color":"dark_aqua"},{"text":" | ","color":"gold"},{"text":"ERROR in <PATH>","color":"red","clickEvent":{"action":"open_url","value":"tag @s remove bs.debug.<PATH>"},"hoverEvent":{"action":"show_text","contents":"Hide this debug"}}]
   ```

- **Warning without source entity**
   ```
   tellraw @a[tag=bs.debug.<PATH>] [{"text":" > ","bold":true,"color":"gold"},{"text":"Glib","color":"dark_aqua"},{"text":" | ","color":"gold"},{"text":"WARNING in <PATH>","color":"yellow","clickEvent":{"action":"open_url","value":"tag @s remove bs.debug.<PATH>"},"hoverEvent":{"action":"show_text","contents":"Hide this debug"}}]
   ```

- **Record without source entity**
   ```
   tellraw @a[tag=bs.debug.<PATH>] [{"text":" > ","bold":true,"color":"gold"},{"text":"Glib","color":"dark_aqua"},{"text":" | ","color":"gold"},{"text":"Record from <PATH>","color":"green","clickEvent":{"action":"open_url","value":"tag @s remove bs.debug.<PATH>"},"hoverEvent":{"action":"show_text","contents":"Hide this debug"}}]
   ```

Also, all debugs must end with

```
tellraw @a[tag=bs.debug.<PATH>] ["",{"text":" <","bold":true,"color":"gold"}]
```

⚠️ All debugs must be preceded by ``# Start Debug`` and followed by ``# End Debug`` in order to be automatically commented by a program.