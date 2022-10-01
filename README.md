# Sistemas-Distribuidos

Lucas André Sardenberg Santos 769800

Thiago César Silva Barbieri 779807

  O arquivo 'loja.py' instancia objetos do tipo Loja com nome, id, e produtos que podem ser removidos (vendidos) ou adicionados (comprados da fábrica). O código foi configurado para que ele gere vendas aleatórias desses produtos e faça requests de novos produtos quando o estoque dessa classe de produto esteja abaixo de 25%.
  
  O arquivo 'fabrica.py' instancia objetos do tipo Fabrica com nome, id e produtos que podem ser adicionados (para setar os produtos com que eles trabalham) e removidos (enviados para o centro de distribuição).
  
  Toda vez que uma dessas ações vai acontecer entre a loja e a fábrica, na verdade elas são enviadas para o centro de distribuição (centro_dist.py), que verifica a possibilidade dessas compras e vendas, e busca em qual fábrica comprar e as entrega para seus respectivos clientes.
  
  Essas ações acontecem por meio dos métodos do mqtt_client, que são importados dos códigos 'pub.py' (para ações de publish) e o 'sub.py' (para ações de subscribe).
  
  Então sempre que há um novo pedido de produtos, eles são publicados e lidos pelo centro de distribuição através de sua inscrição nos tópicos da loja e da fábrica, que os redireciona para seus respectivos destinos através de suas respectivas inscrições nos tópicos do centro de distribuição.
