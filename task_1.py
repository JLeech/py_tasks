import time
from itertools import count


class Snp:

	_snps_counter = 0

	def __init__(self, rs_id, pval):
		self.rs_id = rs_id
		self.pval = pval
		self.archived = False
		self.strange_id = type(self)._snps_counter
		type(self)._snps_counter += 1
		# насколько уникальны self.strange_id?
		# зачем вызывать type у self?
		# как можно переписать обращение к snps_counter?
		# а обязательно инкрементировать руками? может в питоне есть 
		# стандартный класс для этого?

	def __lt__(self, other_snp):
		return False

	def __gt__(self, other_snp):
		return False
		
	def __eq__(self, other_snp):
		# два снипа равны, если у них одинаковые rs_id и pval
		return False
	
	def __repr__(self):
		fmt = "RsID: {:5} | Pval: {:5} | Archived:{:5}|"
		return fmt.format(self.rs_id, self.pval, self.archived)


class SnpStorage:
	"""Класс-хранилище снипов
	Хранит все снипы которые мы в него добавили
	Он связан с базой, поиск по которой занимает некоторое время,
	но это можно кое-как оптимизировать (см задание со *)
	Снип можно удалить, при этом он помечается как archived,
	но остаётся в хранилище.
	Существует  операция которая удаляет
	все archived снипы """

	def __init__(self):
		self._snps = []
		# почему с одинарным подчёркиванием?

	def __contains__(self, snp):
		# считаем что снип содержится
		# если в хранилище есть снип с таким rs_id и pval
		# и он не удалён
		return False

	def __len__(self):
		# количество не удалённых снипов
		return 0

	def __getitem__(self, posititon):
		"""итерация выполняется по всему хранилищу, независимо
		удалён снип или нет
		*** задание со звёздочкой ***
		как мне ускорить получение элементов?
		tip: смотреть декораторы на букву m"""
		time.sleep(0.5) #имитирует задержку к базе
		return self._snps[posititon]

	def __repr__(self):
		# метод для красивой печати
		repr = "DB with {0} active elems.\n".format(len(self))
		for snp in self:
			repr += str(snp)+"\n"
		return repr

	def __not_deleted_snps(self):
		# получить список всех не удалённых снипов (1 строка)
		return []
		

	def add_elem(self, snp):
		self._snps.append(snp)

	def delete_archived_elems(self):
		# удалить все архивированные снипы (1 строка)
		self._snps = self._snps

	def __delitem__(self, rs_id):
		# помечает все снипы с этим rs_id как archived
		for snp in self:
			if snp.rs_id == rs_id:
				snp.archived = True
		# можно переписать компактнее?

	def count_doubles_rs(self):
		# результат словарь, где ключ: rs_id
		# значение: количество снипов с таким rs_id
		# например {0: 2, 3: 4}
		# задание со * а есть стандартные классы для этого?
		return {}

def test_all():
	# создаём три snp
	x = Snp(rs_id=1, pval=0.02)
	y = Snp(rs_id=2, pval=0.04)
	z = Snp(rs_id=3, pval=0.04)	

	# записываем их в базу
	store = SnpStorage()
	store.add_elem(z)
	store.add_elem(y)
	store.add_elem(x)	

	print(store)
	print("ПОЧЕМУ ТАК ДОЛГО-ТО?! см __getitem__ для SnpStorage")

	# проверяем что для снипов всё сделано правильно
	try:
		print("Snp.eq+") if (x == x) else print("Snp.eq operation implemented wrong")
		print("Snp.lt+") if (x < y) else print("Snp.lt operation implemented wrong")
		print("Snp.gt+") if (y > x) else print ("Snp.gt operation implemented wrong")	

	except:
		print ("Some Snp operations are wrong")	

	try:
		if x in store:
			print("SnpStorage.contains+")
		else:
			print("SnpStorage.contains implemented wrong")
		
		del store[2]
		
		if (len(store) == 2):
			print("SnpStorage.del+")
		else:
			print("SnpStorage.del implemented wrong")
		
		store.delete_archived_elems()

		if len([ x.rs_id for x in store]) == 2:
			print("SnpStorage.delete_archived_elems+")
		else:
			print("SnpStorage.delete_archived_elems implemented wrong")

		store.add_elem(x)
		store.add_elem(y)
		if (store.count_doubles_rs() == {1: 2, 2: 1, 3: 1}):
			print("SnpStorage.count_doubles_rs+")
		else:
			print("SnpStorage.count_doubles_rs implemented wrong")

		# как выбирать из store снипы в порядке сортировки по pval?
		# нужно что-то сделать над store, а не над массивом pval
		if ([ snp.pval for snp in store] == [0.02, 0.02, 0.04, 0.04]):
			print("Well done!")
		else:
			print("Wrong pval sort order")
			

	except Exception as error:
		print("some SnpStorage methods are not implemented: \n{0}".format(error))

test_all()

