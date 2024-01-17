SELECT n.nome, e.endereco
FROM nomes AS n
JOIN enderecos AS e ON n.id = e.id_nome
WHERE n.nome LIKE 'B%'