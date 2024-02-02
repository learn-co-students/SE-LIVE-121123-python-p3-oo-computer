class Computer:

    all = []

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.memory_GB = 8
        self.storage_free = 1000
        self.__class__.all.append(self)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not hasattr(self, "brand"):
            self._brand = value
        else:
            raise Exception("Brand cannot be changed")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not hasattr(self, "model"):
            self._model = value
        else:
            raise Exception("Model cannot be changed")

    @property
    def memory_GB(self):
        return self._memory_GB

    @memory_GB.setter
    def memory_GB(self, value):
        self._memory_GB = value

    @property
    def storage_free(self):
        return self._storage_free

    @storage_free.setter
    def storage_free(self, value):
        if 0 <= value <= 1000:
            self._storage_free = value

    def upgrade_memory(self, RAM):
        self.memory_GB += RAM["size"]

    def is_disk_full(self, file_size):
        return file_size > self.storage_free

    def save_file(self, file):
        if not (self.is_disk_full(file["size"])):
            self.storage_free -= file["size"]
            return f'{file["name"]} has been saved!'
        else:
            return f'There is not enough space on disk to save {file["name"]}'

    def delete_file(self, file):
        self.storage_free += file["size"]
        return f'{file["name"]} has been deleted!'

    def specs(self):
        return f"{self.model} has {self.memory_GB} GB of memory and {self.storage_free} GB of available storage."

    @classmethod
    def brands(cls):
        return [*set([comp.brand for comp in Computer.all])]

    @classmethod
    def models(cls):
        return [*set([comp.model for comp in Computer.all])]

    @classmethod
    def largest_memory(cls):
        return max(Computer.all, key=lambda comp: comp.memory_GB)
        # curr_lg_comp = None
        # curr_lg_memory = 0
        # for comp in Computer.all:
        #     if comp.memory_GB > curr_lg_memory:
        #         curr_lg_comp = comp
        #         curr_lg_memory = comp.memory_GB
        # return curr_lg_comp


if __name__ == "__main__":

    mbp = Computer("apple", "macbook pro m1")
    air = Computer("apple", "mb air")
    air2 = Computer("apple", "mb air")
    acer = Computer("acer", "AX 213")
    print(mbp.brand)
    # mbp.brand = "hp"
    # mbp.model = "air"
    mbp.upgrade_memory({"model": "Samsung", "size": 8})
    print(mbp.specs())
    print(mbp.is_disk_full(1128))
    print(mbp.save_file({"name": "homework.py", "size": 128}))
    print(mbp.specs())
    print(mbp.save_file({"name": "memoir.py", "size": 1128}))
    print(mbp.delete_file({"name": "homework.py", "size": 128}))
    print(mbp.specs())
    print(Computer.brands())
    print(Computer.models())
    largest = Computer.largest_memory()
    print(largest.specs())
