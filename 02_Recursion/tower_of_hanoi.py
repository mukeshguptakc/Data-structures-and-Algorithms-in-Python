
def TowerOfHanoi(disk, _from, _to, aux):
    if(disk == 1):
        print("Move disk", disk ,"from", _from, "to", _to)
        return
    TowerOfHanoi(disk-1, _from, aux, _to)
    print("Move disk", disk,"from", _from, "to", _to)
    TowerOfHanoi(disk-1, aux, _to, _from)

if __name__=="__main__":
    disk = 4
    TowerOfHanoi(disk, "A", "B", "C")