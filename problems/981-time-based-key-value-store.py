class TimeMap:

    def __init__(self):
        self.hashMap = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        newKey = key + str(timestamp)
        self.hashMap[newKey] = [value, timestamp]
        

    def get(self, key: str, timestamp: int) -> str:
        newKey = key + str(timestamp)
        if newKey in self.hashMap:
            return self.hashMap.get(newKey)[0]
        else: 
            while timestamp > 0:
                timestamp -= 1
                new = key + str(timestamp)
                if new in self.hashMap:
                    return self.hashMap.get(new)[0]
                else:
                    continue
        return ""

 

        

        
obj = TimeMap()
obj.set("foo","bar",1)
obj.set("foo","bar2",4)
param_2 = obj.get("foo",3)
print(param_2)