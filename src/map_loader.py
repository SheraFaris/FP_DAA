import osmnx as ox


def load_road_graph(place_name):
    """
    Mengambil graph jalan dari OpenStreetMap menggunakan OSMnx.
    network_type='drive' berarti hanya jalan yang dapat dilalui kendaraan.
    """
    graph = ox.graph_from_place(
        place_name,
        network_type="drive",
        simplify=True
    )

    return graph


def get_nearest_node(graph, latitude, longitude):
    """
    Mencari node jalan terdekat dari koordinat latitude dan longitude.
    OSMnx memakai urutan longitude, latitude.
    """
    return ox.distance.nearest_nodes(graph, longitude, latitude)