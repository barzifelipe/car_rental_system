SELECT 
    car.categoria,
    COUNT(loc.numero_reserva) AS total_reservas,
    SUM(car.valor_diaria) AS total_valor_diarias
FROM labdatabase.locacoes loc
JOIN labdatabase.carros car
    ON loc.id_carro = car.id_carro
GROUP BY car.categoria
ORDER BY total_valor_diarias DESC
