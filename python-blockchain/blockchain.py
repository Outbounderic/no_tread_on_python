from block import Block


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions.
    """

    def __init__(self) -> None:
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

    def __repr__(self) -> str:
        return f'Blockchain: {self.chain}'


def main():

    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')


if __name__ == '__main__':
    """
    Executes program iff executed directly from interpreter
    """
    main()
