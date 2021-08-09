from stack_queue.animal import AnimalShelter


def test_enqueue_animal():
  animal=AnimalShelter()
  animal.enqueue('cat')
  animal.enqueue('dog')
  assert str(animal) == "{cat}<-{dog}<-Null"

def test_dequeue_dog():
  animal=AnimalShelter()
  animal.enqueue('cat')
  animal.enqueue('dog')
  animal.dequeue('dog')
  assert str(animal) == "{cat}<-Null"

def test_dequeue_cat():
  animal=AnimalShelter()
  animal.enqueue('cat')
  animal.enqueue('dog')
  animal.dequeue('cat')
  assert str(animal) == "{dog}<-Null"

def test_dequeue_others():
  animal=AnimalShelter()
  animal.enqueue('cat')
  animal.enqueue('dog')
  assert animal.dequeue('x')=="null"
