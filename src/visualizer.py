import folium


def visualize_route(osmnx_graph, path, distance, output_file):
    """
    Membuat visualisasi rute pada peta HTML menggunakan Folium.
    """

    if not path:
        raise ValueError("Path kosong, rute tidak dapat divisualisasikan.")

    route_coordinates = []

    for node in path:
        latitude = osmnx_graph.nodes[node]["y"]
        longitude = osmnx_graph.nodes[node]["x"]
        route_coordinates.append((latitude, longitude))

    start_coordinate = route_coordinates[0]
    destination_coordinate = route_coordinates[-1]

    map_object = folium.Map(
        location=start_coordinate,
        zoom_start=15
    )

    folium.Marker(
        location=start_coordinate,
        popup="Start",
        icon=folium.Icon(color="green")
    ).add_to(map_object)

    folium.Marker(
        location=destination_coordinate,
        popup="Destination",
        icon=folium.Icon(color="red")
    ).add_to(map_object)

    folium.PolyLine(
        locations=route_coordinates,
        weight=5,
        opacity=0.8,
        popup=f"Distance: {distance:.2f} meters"
    ).add_to(map_object)

    map_object.save(output_file)