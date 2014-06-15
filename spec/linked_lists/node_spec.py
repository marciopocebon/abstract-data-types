from ivoire import describe, context
from expects import expect
from src.linked_lists.node import Node

with describe(Node) as it:
  @it.before
  def before(test):
    nextNode = Node(1)
    test.node = Node(2, nextNode)

  @it.after
  def after(test):
    test.node = None

  with context(Node.__init__):
    with it('assign a cargo value') as test:
      expect(test.node.cargo).to.be(2)
    with it('link to another Node object') as test:
      expect(test.node.next).to.be.a(Node)

  with context(Node.__str__):
    with it('set its representation to the cargo value') as test:
      expect(test.node.__str__()).to.equal(str(test.node.cargo))

  with context(Node.__cmp__):
    with it('compares its cargo value to another one') as test:
      expect(test.node).to.be.above(Node(1))

    with it('returns True when greater') as test:
      expect(test.node > Node(0)).to.be(True)

    with it('returns False when lesser') as test:
      expect(test.node > Node(3)).to.be(False)

    with it('returns False when equal') as test:
      expect(test.node > Node(2)).to.be(False)