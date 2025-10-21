SELECT 
    loc.numero_reserva,
    TO_CHAR(loc.data_inicio, 'DD/MM/YYYY') AS data_inicio,
    TO_CHAR(loc.data_fim, 'DD/MM/YYYY') AS data_fim,
    cli.nome AS nome_cliente,
    car.modelo AS modelo_carro,
    func.nome AS nome_funcionario
FROM labdatabase.locacoes loc
JOIN labdatabase.clientes cli 
    ON loc.cpf = cli.cpf
JOIN labdatabase.carros car 
    ON loc.id_carro = car.id_carro
JOIN labdatabase.funcionarios func 
    ON loc.id_funcionario = func.id_funcionario
ORDER BY loc.numero_reserva
/