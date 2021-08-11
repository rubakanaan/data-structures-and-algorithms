from stack_queue.bracket import validate_brackets

def test_balanced():
  string="()[[Extra Characters]]"
  assert validate_brackets(string)


def test_not_balanced():
  string="[({}]	"
  assert not validate_brackets(string)
