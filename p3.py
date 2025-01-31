import networkx as nx
import heapq




def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    
    # купа для обробки вершин
    distances_heap = [(0, start)]   # (відстань, вершина)
    heapq.heapify(distances_heap)

    while distances_heap:
        # Витягуємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(distances_heap)

        # Якщо знайдена відстань більше поточної, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = current_distance + weight

            # Якщо знайдено коротший шлях, оновлюємо відстань і додаємо у купу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(distances_heap, (distance, neighbor))

    return distances



def kiev_metro():
    # граф київського метро
    graph = nx.Graph()

    graph.add_edges_from([
        # Червона лінія
        ("Akademmistechko", "Zhytomyrska", {"weight": 2}),
        ("Zhytomyrska", "Sviatoshyn", {"weight": 2}),
        ("Sviatoshyn", "Nyvky", {"weight": 2}),
        ("Nyvky", "Beresteiska", {"weight": 2}),
        ("Beresteiska", "Shuliavska", {"weight": 2}),
        ("Shuliavska", "Polytechnic Institute", {"weight": 2}),
        ("Polytechnic Institute", "Vokzalna", {"weight": 2}),
        ("Vokzalna", "University", {"weight": 1}),
        ("University", "Teatralna", {"weight": 1}),
        ("Teatralna", "Khreshchatyk", {"weight": 1}),
        ("Khreshchatyk", "Arsenalna", {"weight": 2}),
        ("Arsenalna", "Dnipro", {"weight": 2}),
        ("Dnipro", "Hidropark", {"weight": 3}),
        ("Hidropark", "Livoberezhna", {"weight": 2}),
        ("Livoberezhna", "Darnytsia", {"weight": 2}),
        ("Darnytsia", "Chernihivska", {"weight": 2}),
        ("Chernihivska", "Lisova", {"weight": 2}),

        # Синя лінія
        ("Heroiv Dnipra", "Minska", {"weight": 2}),
        ("Minska", "Obolon", {"weight": 2}),
        ("Obolon", "Pochaina", {"weight": 2}),
        ("Pochaina", "Tarasa Shevchenka", {"weight": 2}),
        ("Tarasa Shevchenka", "Kontraktova Ploshcha", {"weight": 1}),
        ("Kontraktova Ploshcha", "Poshtova Ploshcha", {"weight": 1}),
        ("Poshtova Ploshcha", "Maidan Nezalezhnosti", {"weight": 1}),
        ("Maidan Nezalezhnosti", "Ploshcha Lva Tolstoho", {"weight": 1}),
        ("Ploshcha Lva Tolstoho", "Olimpiiska", {"weight": 1}),
        ("Olimpiiska", "Palats Ukraina", {"weight": 2}),
        ("Palats Ukraina", "Lybidska", {"weight": 2}),
        ("Lybidska", "Demiivska", {"weight": 2}),
        ("Demiivska", "Holosiivska", {"weight": 2}),
        ("Holosiivska", "Vasylkivska", {"weight": 2}),
        ("Vasylkivska", "Vystavkovyi Tsentr", {"weight": 2}),
        ("Vystavkovyi Tsentr", "Ipodrom", {"weight": 2}),
        ("Ipodrom", "Teremky", {"weight": 2}),

        # Зелена лінія
        ("Syrets", "Dorohozhychi", {"weight": 2}),
        ("Dorohozhychi", "Lukianivska", {"weight": 2}),
        ("Lukianivska", "Zoloti Vorota", {"weight": 1}),
        ("Zoloti Vorota", "Palats Sportu", {"weight": 1}),
        ("Palats Sportu", "Klovska", {"weight": 1}),
        ("Klovska", "Pecherska", {"weight": 2}),
        ("Pecherska", "Druzhby Narodiv", {"weight": 2}),
        ("Druzhby Narodiv", "Vydubychi", {"weight": 2}),
        ("Vydubychi", "Slavutych", {"weight": 3}),
        ("Slavutych", "Osokorky", {"weight": 2}),
        ("Osokorky", "Pozniaky", {"weight": 2}),
        ("Pozniaky", "Kharkivska", {"weight": 2}),
        ("Kharkivska", "Boryspilska", {"weight": 2}),
        ("Boryspilska", "Chervony Khutir", {"weight": 2}),

        # Переходи
        ("Teatralna", "Zoloti Vorota", {"weight": 0}),
        ("Khreshchatyk", "Maidan Nezalezhnosti", {"weight": 0}),
        ("Ploshcha Lva Tolstoho", "Palats Sportu", {"weight": 0})

    ])
    return graph



def main():
    
    graph = kiev_metro()
   
    start_node = "Khreshchatyk"
 

    #  Алгоритм Дейкстри
    distances = dijkstra(graph, start_node)
    print(f"\nShortest paths from {start_node}:")
    for target, distance in distances.items():
        print(f"  To {target}: {distance}")

if __name__ == "__main__":
    main()



