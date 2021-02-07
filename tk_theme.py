import selecttheme as them

  
if them.custom == "true":
  import custom

if them.custom == "false":
  if them.theme == "default":
    size = 13
    font = "Times"
    textconf = ("Times", 25)
    wid = 50

  if them.theme == "old":
    wid = 45
    font = "Times"
    size = 13
    textconf = ("roman", 25)