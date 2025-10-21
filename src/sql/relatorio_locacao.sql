SELECT 
    l.numero_reserva,
    TO_CHAR(l.data_inicio, 'DD/MM/YYYY') AS data_inicio,
    TO_CHAR(l.data_fim, 'DD/MM/YYYY') AS data_fim,
    c.nome AS nome_cliente,
    car.modelo AS modelo_carro,
    f.nome AS nome_funcionario
FROM labdatabase.locacoes l
JOIN labdatabase.clientes c 
    ON l.cpf = c.cpf
JOIN labdatabase.carros car 
    ON l.id_carro = car.id_carro
JOIN labdatabase.funcionarios f 
    ON l.id_funcionario = f.id_funcionario
ORDER BY l.numero_reserva