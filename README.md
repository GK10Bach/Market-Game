# To Do
*Room Object*
Vars - Size, Position, Door Locations, Locked
CreateRoom - Pick Position/Size, Determine Doors
UnlockDoors - Locked=False, change doors to green

*Hallway Object*
Var - Start, End, Elbows
CreateHallway - Check if existing door is near; if yes, end=doorPos; if no, CreateRoom, end=doorPos