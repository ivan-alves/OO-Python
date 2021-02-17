from conta import Conta

conta = Conta( 1, "Ivan", 200.0, 1000.0)
conta2 = Conta(2, "Gisele", 100.0, 1000.0)


conta.transfere(50.0, conta2)
conta.extrato()
conta2.extrato()