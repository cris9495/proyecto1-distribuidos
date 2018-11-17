
class hash_table:
    def __init__(self):
        self.table = [[] for _ in range(10)]
        #self.table = [None] * 15



    def Insert(self, key, value):

        hash_key = hash(key) % len(self.table)
        key_exists = False
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def Search(self, key):

        hash_key = hash(key) % len(self.table)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def  Delete(self, key):

         hash_key = hash(key) % len(self.table)
         key_exists = False
         bucket = self.table[hash_key]
         for i, kv in enumerate(bucket):
             k, v = kv
             if key == k:
                 key_exists = True
                 break
         if key_exists:
             del bucket[i]
             print ('Key {} deleted'.format(key))
         else:
             print ('Key {} not found'.format(key))






H = hash_table()
H.Insert("A","si")
H.Insert(90,8)


print(H.Search(90))
H.Delete(90)
print(H.Search("A"))

print(H.Search("B"))
