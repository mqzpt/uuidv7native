import uuid
import sys
uuid_object = uuid.uuid7()
print(uuid_object.time)
print(sys.getsizeof(uuid_object))
